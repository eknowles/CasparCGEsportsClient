#!/usr/bin/python

# pyodbc, twython
# MySQL-python @ http://sourceforge.net/projects/mysql-python/files/mysql-python/1.2.3/MySQL-python-1.2.3.win32-py2.7.msi/download

import sys
import logging
import socket
import re
import elementtree.ElementTree as ET
import xml.etree.ElementTree as xml
import MySQLdb
from PyQt4 import QtGui, QtCore, QtSql
from twython import Twython

from windowUi import Ui_MainWindow
from Rundown import Ui_Rundown


logging.basicConfig(level=logging.DEBUG, format='[%(asctime)s] %(levelname)s: %(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p',
                    handlers=[logging.FileHandler("console.log"), logging.StreamHandler()])
logging.info('Program Launched')

class Database():
    def __init__(self):
        self.db_host = ""
        self.db_user = ""
        self.db_pass = ""
        self.db_name = ""

    def openConn(self):
        self.db = MySQLdb.connect(self.db_host, self.db_user, self.db_pass, self.db_name)

    def closeConn(self):
        self.db.close()

    def writeValues(self, sql):
        self.openConn()
        self.cursor = self.db.cursor()
        self.cursor.execute(sql)
        ret = self.cursor.fetchall()
        self.closeConn()
        return ret

class RundownDialog(QtGui.QDialog):
    def __init__(self, parent=None):
        super(RundownDialog, self).__init__(parent)

        # Set up the user interface from Designer.
        self.ui = Ui_Rundown()
        self.ui.setupUi(self)

    def accept(self):
        if self.ui.title.text() == '':
            title = 'NULL'
        else:
            title = "'" + str(self.ui.title.text()) + "'"
        self.sql = "SELECT * FROM events"
        #self.sql = "INSERT INTO admin_escg.schedule (start, channel_id, event_id, team1_id, team2_id, title, caster1_id, caster2_id) VALUES ('2013-08-26 12:00:00', '1', '1', '1', '2', "+title+", '1', '2');"
        self.submitForm()
        super(RundownDialog, self).accept()

    def submitForm(self):
        db = Database()
        db.writeValues(self.sql)


class Main(QtGui.QMainWindow):
    # class variables
    # constructor
    def __init__(self):
        #Qt main window init
        QtGui.QMainWindow.__init__(self)
        # instance variables
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # sshFile="Default.css"
        # with open(sshFile,"r") as fh:
        #     self.setStyleSheet(fh.read())

        self.LastCG = 0

        self.APIurl = "http://eknowles.com/api/"
        self.PlayersXML = self.APIurl + "playerslist.php?export=xml"
        self.TeamsXML = self.APIurl + "teamslist.php?export=xml"
        self.EventsXML = self.APIurl + "eventslist.php?export=xml"
        self.Team_EventXML = self.APIurl + "link_team_eventlist.php?export=xml"
        self.Player_TeamXML = self.APIurl + "link_player_teamlist.php?export=xml"


        QtCore.QObject.connect(self.ui.get_tweets_btn, QtCore.SIGNAL('clicked()'), self.SearchTweets)

        # self.ui.get_tweets_btn.clicked.connect(self.SearchTweets)
        QtCore.QObject.connect(self.ui.console_go, QtCore.SIGNAL('clicked()'), self.ConsoleCommand)
        QtCore.QObject.connect(self.ui.Console_ComingUp, QtCore.SIGNAL('clicked()'), lambda: self.ProcessCommand(1))
        QtCore.QObject.connect(self.ui.Console_Sponsors, QtCore.SIGNAL('clicked()'), lambda: self.ProcessCommand(2))
        QtCore.QObject.connect(self.ui.Console_TweetFeed, QtCore.SIGNAL('clicked()'), lambda: self.ProcessCommand(3))
        QtCore.QObject.connect(self.ui.Console_TweetSingle, QtCore.SIGNAL('clicked()'), lambda: self.ProcessCommand(4))
        QtCore.QObject.connect(self.ui.Console_TeamMatch, QtCore.SIGNAL('clicked()'), lambda: self.ProcessCommand(5))
        QtCore.QObject.connect(self.ui.Console_Players1, QtCore.SIGNAL('clicked()'), lambda: self.ProcessCommand(6))
        QtCore.QObject.connect(self.ui.Console_Players2, QtCore.SIGNAL('clicked()'), lambda: self.ProcessCommand(7))

        #Schedule Signals
        QtCore.QObject.connect(self.ui.Schedule_Add, QtCore.SIGNAL('clicked()'), self.AddRundown)
        QtCore.QObject.connect(self.ui.Schedule_Remove, QtCore.SIGNAL('clicked()'), self.Schedule_Remove)

        # Event Signals
        QtCore.QObject.connect(self.ui.UpdateEvents, QtCore.SIGNAL('clicked()'), self.UpdateEvents)


        self.ui.actionReload_Client.triggered.connect(self.LoadSettings)
        self.ui.actionQuit.triggered.connect(self.Quit)

        # Load Primary Settings (First load)
        self.LoadSettings()


        self.clocktimer = QtCore.QTimer(self)
        self.clocktimer.timeout.connect(self.showTime)
        self.clocktimer.start(1000)

        self.showTime()
        self.ModifyRundown = RundownDialog(self)

        escg = QtSql.QSqlDatabase.addDatabase("QMYSQL")
        escg.setHostName("eknowles.com")
        escg.setDatabaseName("admin_escg")
        escg.setUserName("admin_escg")
        escg.setPassword("p4e9@;FImZ8[")
        escg.open()

        self.eventsmodel = QtSql.QSqlRelationalTableModel(self.ui.Event_Table)
        self.eventsmodel.setTable("events")
        self.eventsmodel.setRelation(7, QtSql.QSqlRelation("games", "id", "name"))
        self.eventsmodel.setRelation(6, QtSql.QSqlRelation("players", "id", "handle"))
        self.eventsmodel.setHeaderData(0, QtCore.Qt.Horizontal, QtCore.QVariant(""))
        self.eventsmodel.setHeaderData(1, QtCore.Qt.Horizontal, QtCore.QVariant("Name"))
        self.eventsmodel.setHeaderData(2, QtCore.Qt.Horizontal, QtCore.QVariant("Start"))
        self.eventsmodel.setHeaderData(3, QtCore.Qt.Horizontal, QtCore.QVariant("End"))
        self.eventsmodel.setHeaderData(4, QtCore.Qt.Horizontal, QtCore.QVariant("Location"))
        self.eventsmodel.setHeaderData(5, QtCore.Qt.Horizontal, QtCore.QVariant("Shortname"))
        self.eventsmodel.setHeaderData(6, QtCore.Qt.Horizontal, QtCore.QVariant("Added By"))
        self.eventsmodel.setHeaderData(7, QtCore.Qt.Horizontal, QtCore.QVariant("Game"))
        self.eventsmodel.select()
        self.ui.Event_Table.setModel(self.eventsmodel)
        self.ui.Event_Table.setColumnHidden(0,1)
        self.ui.Event_Table.setColumnWidth(0, 30)
        self.ui.Event_Table.setAlternatingRowColors(True)
        self.ui.Event_Table.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.ui.Event_Table.horizontalHeader().setStretchLastSection(True)
        self.ui.Event_Table.verticalHeader().setVisible(False)

        self.TeamsTableModel = QtSql.QSqlRelationalTableModel(self.ui.Teams_Table)
        self.TeamsTableModel.setTable("teams")
        self.TeamsTableModel.setRelation(7, QtSql.QSqlRelation("players", "id", "handle"))
        self.TeamsTableModel.setHeaderData(0, QtCore.Qt.Horizontal, QtCore.QVariant(""))
        self.TeamsTableModel.setHeaderData(1, QtCore.Qt.Horizontal, QtCore.QVariant(""))
        self.TeamsTableModel.setHeaderData(2, QtCore.Qt.Horizontal, QtCore.QVariant("Team Name"))
        self.TeamsTableModel.setHeaderData(3, QtCore.Qt.Horizontal, QtCore.QVariant("Tag"))
        self.TeamsTableModel.setHeaderData(4, QtCore.Qt.Horizontal, QtCore.QVariant("Short Tag"))
        self.TeamsTableModel.setHeaderData(5, QtCore.Qt.Horizontal, QtCore.QVariant("Website"))
        self.TeamsTableModel.setSort(1, 0) # Sorting by Col 1 and 0 for AAA
        self.TeamsTableModel.select()
        self.ui.Teams_Table.setModel(self.TeamsTableModel)
        self.ui.Teams_Table.setColumnHidden(0,1)
        self.ui.Teams_Table.setColumnHidden(4,1)
        self.ui.Teams_Table.setColumnHidden(6,1)
        self.ui.Teams_Table.setColumnHidden(7,1)
        self.ui.Teams_Table.setColumnWidth(0, 30)
        self.ui.Teams_Table.setColumnWidth(1, 30)
        self.ui.Teams_Table.setAlternatingRowColors(True)
        self.ui.Teams_Table.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.ui.Teams_Table.horizontalHeader().setStretchLastSection(True)
        self.ui.Teams_Table.verticalHeader().setVisible(False)

        self.PlayersTableModel = QtSql.QSqlRelationalTableModel(self.ui.Players_Table)
        self.PlayersTableModel.setTable("players")
        self.PlayersTableModel.setRelation(8, QtSql.QSqlRelation("games", "id", "shortname"))
        self.PlayersTableModel.setHeaderData(0, QtCore.Qt.Horizontal, QtCore.QVariant("ID"))
        self.PlayersTableModel.setHeaderData(1, QtCore.Qt.Horizontal, QtCore.QVariant("Handle"))
        self.PlayersTableModel.setHeaderData(2, QtCore.Qt.Horizontal, QtCore.QVariant("First Name"))
        self.PlayersTableModel.setHeaderData(3, QtCore.Qt.Horizontal, QtCore.QVariant("Last Name"))
        self.PlayersTableModel.setHeaderData(4, QtCore.Qt.Horizontal, QtCore.QVariant("Date of Birth"))
        self.PlayersTableModel.setHeaderData(5, QtCore.Qt.Horizontal, QtCore.QVariant("Country"))
        self.PlayersTableModel.setHeaderData(6, QtCore.Qt.Horizontal, QtCore.QVariant("Twitter"))
        self.PlayersTableModel.setHeaderData(8, QtCore.Qt.Horizontal, QtCore.QVariant("Game"))
        self.PlayersTableModel.setSort(1, 0) # Sorting by Col 1 and 0 for AAA
        self.PlayersTableModel.select()
        self.ui.Players_Table.setModel(self.PlayersTableModel)


        self.ui.Players_Table.setColumnHidden(0,1)
        self.ui.Players_Table.setColumnHidden(7,1)
        self.ui.Players_Table.setColumnHidden(9,1)
        self.ui.Players_Table.setColumnHidden(10,1)
        self.ui.Players_Table.setColumnHidden(11,1)
        self.ui.Players_Table.setColumnHidden(12,1)
        self.ui.Players_Table.setColumnHidden(13,1)
        self.ui.Players_Table.setColumnHidden(14,1)
        self.ui.Players_Table.setColumnHidden(15,1)
        self.ui.Players_Table.setAlternatingRowColors(True)
        self.ui.Players_Table.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.ui.Players_Table.horizontalHeader().setStretchLastSection(True)
        self.ui.Players_Table.verticalHeader().setVisible(False)


        self.RundownModel = QtSql.QSqlRelationalTableModel(self.ui.Schedule_Table)
        self.RundownModel.setTable("rundown")
        self.RundownModel.setHeaderData(0, QtCore.Qt.Horizontal, QtCore.QVariant(""))
        self.RundownModel.setHeaderData(1, QtCore.Qt.Horizontal, QtCore.QVariant("Title"))
        self.RundownModel.setHeaderData(2, QtCore.Qt.Horizontal, QtCore.QVariant("Team 1"))
        self.RundownModel.setHeaderData(3, QtCore.Qt.Horizontal, QtCore.QVariant("Team 2"))
        self.RundownModel.setHeaderData(4, QtCore.Qt.Horizontal, QtCore.QVariant("Start Time"))
        self.RundownModel.setHeaderData(5, QtCore.Qt.Horizontal, QtCore.QVariant("Game"))
        self.RundownModel.setHeaderData(6, QtCore.Qt.Horizontal, QtCore.QVariant("Event"))
        self.RundownModel.setHeaderData(7, QtCore.Qt.Horizontal, QtCore.QVariant("Channel"))
        self.RundownModel.setHeaderData(8, QtCore.Qt.Horizontal, QtCore.QVariant("Status"))
        self.RundownModel.setRelation(5, QtSql.QSqlRelation("games", "id", "shortname"))
        self.RundownModel.setRelation(2, QtSql.QSqlRelation("teams", "id", "name"))
        self.RundownModel.setRelation(3, QtSql.QSqlRelation("teams", "id", "name"))
        self.RundownModel.setRelation(6, QtSql.QSqlRelation("events", "id", "name"))
        self.RundownModel.setSort(1, 0) # Sorting by Col 1 and 0 for AAA
        self.RundownModel.select()
        self.ui.Schedule_Table.setModel(self.RundownModel)
        self.ui.Schedule_Table.setColumnHidden(0,1)
        self.ui.Schedule_Table.setColumnWidth(0, 30)
        self.ui.Schedule_Table.setColumnWidth(1, 300)
        self.ui.Schedule_Table.setColumnWidth(5, 60)
        self.ui.Schedule_Table.setColumnWidth(4, 128)
        self.ui.Schedule_Table.setColumnWidth(7, 60)
        self.ui.Schedule_Table.setAlternatingRowColors(True)
        self.ui.Schedule_Table.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.ui.Schedule_Table.horizontalHeader().setStretchLastSection(True)
        self.ui.Schedule_Table.verticalHeader().setVisible(False)

        self.UpdateEvents()

    @QtCore.pyqtSlot()
    def AddRundown(self):
        self.ModifyRundown.exec_()

    def UpdateEvents(self):
        # sql = "SELECT * FROM events"
        # self.db = Database()
        # eventlist = db.writeValues(sql)
        # for event in eventlist:
        #     print event
        print "MOO"



    def Schedule_Remove(self):
        response = QtGui.QMessageBox.warning(self
            , "Remove Rundown Item"
            , "Are you sure you want to permanently remove this item?"
            , QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
        if response == QtGui.QMessageBox.Yes:
            pass
        return

    def showTime(self):
        time = QtCore.QTime.currentTime()
        text = time.toString('h:mm:ss A')
        # if (time.second() % 2) == 0:
        #     text = text[:2] + ' ' + text[3:]

        self.ui.schedule_clock.setText(text)

    def LoadSettings(self):
        self.BGVideo = ""
        self.BUG = "BUG"
        self.ProcessCommand(self.LastCG)
        # PLAY 1-1 " + self.BGVideo + " LOOP
        self.sendCommand("CLEAR 1\r\nPLAY 1-10 BODY LOOP\r\n")
        self.TweetList = []

    def Quit(self):
        self.ProcessCommand(self.LastCG)
        self.sendCommand("CLEAR 1")
        exit()


    def ProcessCommand(self, cmdnum=0):
        # print cmdnum
        # print self.LastCG
        # if self.LastCG == 0:
            # Hide Nothing
            # print "NO LAST BUTTON"

        if self.LastCG == 1:
            cmd = "MIXER 1-10 FILL 0 0 1 1 25 easeinoutback"
            self.ui.Console_ComingUp.setChecked(0)
            self.sendCommand(str(cmd))

        if self.LastCG == 2:
            cmd = "MIXER 1-10 FILL 0 0 1 1 25 easeinoutback\r\nMIXER 1-10 OPACITY 1 25 easeinoutback"
            self.ui.Console_Sponsors.setChecked(0)
            self.sendCommand(str(cmd))

        if self.LastCG == 3:
            cmd = "MIXER 1-9 OPACITY 0 25 easeinoutback\r\nCG 1 STOP 20 \"DEMO\" 1\r\nMIXER 1-10 FILL 0 0 1 1 25 easeinoutback"
            self.ui.Console_TweetFeed.setChecked(0)
            self.sendCommand(str(cmd))

        if self.LastCG == 4:
            cmd = "CG 1 STOP 20 \"SINGLE\" 1"
            self.ui.Console_TweetSingle.setChecked(0)
            self.sendCommand(str(cmd))

        if self.LastCG == 5:
            cmd = "CG 1 STOP 20 \"TEAMMATCH\" 1"
            self.ui.Console_TeamMatch.setChecked(0)
            self.sendCommand(str(cmd))

        if self.LastCG == 6:
            self.ui.Console_Players1.setChecked(0)
            if cmdnum == 6:
                cmd = "CG 1 STOP 20 \"DEMO\" 1\r\nPLAY 1-11 LINEUPOUT"
            elif not cmdnum == 7:
                cmd = "CG 1 STOP 20 \"DEMO\" 1\r\nSTOP 1-11"
            else:
                cmd = "CG 1 STOP 20 \"DEMO\" 1\r\n"
            self.sendCommand(str(cmd))

        if self.LastCG == 7:
            self.ui.Console_Players2.setChecked(0)
            if cmdnum == 7:
                cmd = "CG 1 STOP 20 \"DEMO\" 1\r\nPLAY 1-11 LINEUPOUT"
            elif not cmdnum == 6:
                cmd = "CG 1 STOP 20 \"DEMO\" 1\r\nSTOP 1-11"
            else:
                cmd = "CG 1 STOP 20 \"DEMO\" 1\r\n"
            self.sendCommand(str(cmd))

        if not cmdnum == self.LastCG:

            if cmdnum == 0:
                self.LastCG = cmdnum

            if cmdnum == 1:
                self.ui.Console_ComingUp.setChecked(1)
                cmd = "MIXER 1-10 FILL 0 0 0.8 0.8 25 easeinoutback"
                self.sendCommand(str(cmd))
                self.LastCG = cmdnum

            if cmdnum == 2:
                self.ui.Console_Sponsors.setChecked(1)
                cmd = "MIXER 1-10 FILL 0.3 0.2 0.4 0.4 25 easeinoutback\r\nMIXER 1-10 OPACITY 1 25 easeinoutback"
                self.sendCommand(str(cmd))
                self.LastCG = cmdnum

            if cmdnum == 3:
                self.ui.Console_TweetFeed.setChecked(1)
                cmd = "MIXER 1-10 FILL 0.05 0.2 0.6 0.6 25 easeinoutback\r\nMIXER 1-9 OPACITY 1 25 easeinoutback\r\nPLAY 1-9 FEEDBG\r\nCG 1 ADD 20 \"DEMO\" 1"
                self.sendCommand(str(cmd))
                self.LastCG = cmdnum

            if cmdnum == 4:
                self.ui.Console_TweetSingle.setChecked(1)
                cmd = "CG 1 ADD 20 \"SINGLE\" 1"
                self.sendCommand(str(cmd))
                self.LastCG = cmdnum

            if cmdnum == 5:
                self.ui.Console_TeamMatch.setChecked(1)
                cmd = "CG 1 ADD 20 \"TEAMMATCH\" 1"
                self.sendCommand(str(cmd))
                self.LastCG = cmdnum

            if cmdnum == 6:
                self.ui.Console_Players1.setChecked(1)
                if self.LastCG == 7:
                    cmd = "PLAY 1-11 LINEUPSWAP\r\nCG 1 ADD 20 \"DEMO\" 1"
                else:
                    cmd = "PLAY 1-11 LINEUPIN\r\nCG 1 ADD 20 \"DEMO\" 1"
                self.sendCommand(str(cmd))
                self.LastCG = cmdnum

            if cmdnum == 7:
                self.ui.Console_Players2.setChecked(1)
                if self.LastCG == 6:
                    cmd = "PLAY 1-11 LINEUPSWAP\r\nCG 1 ADD 20 \"DEMO\" 1"
                else:
                    cmd = "PLAY 1-11 LINEUPIN\r\nCG 1 ADD 20 \"DEMO\" 1"
                self.sendCommand(str(cmd))
                self.LastCG = cmdnum

        else:
            self.LastCG = 0

    def ConsoleCommand(self):
        cmd = self.ui.console_text.text()
        if not cmd == '':
            print
            cmd = cmd + "\r\n"
            self.sendCommand(str(cmd))
            return
        else:
            return

    def sendCommand(self, command=""):
        commands = command.split("|*|")
        #self.loadSettings()
        bufferSize = 16384
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            s.connect(("127.0.0.1", 5250))
        except socket.error, msg:
            s = None

        if s is None:
            return None

        else:
            data = ""
            for i in range(len(commands)):
                message = commands[i] + "\r\n"
                s.send(message.encode('utf-8'))
                data = data + s.recv(bufferSize).decode('utf-8')
            return data

    def SearchTweets(self):
        APP_KEY = 'PpFTrSSEFiW8QD6CrQTjw'
        APP_SECRET = 'ka6YXiNPGNDLYqdpAaTqFb70Rp6qVqzZCLLiK7tSKI'
        twitter = Twython(APP_KEY, APP_SECRET, oauth_version=2)
        ACCESS_TOKEN = twitter.obtain_access_token()
        twitter = Twython(APP_KEY, access_token=ACCESS_TOKEN)

        term = str(self.ui.tweet_search_line.text())
        if not term == '':
            tweetcount = self.ui.tweetspinBox.value()
            search = twitter.search(q=term, result_type='recent', count=tweetcount)
            #for tweet in search['statuses']:
            for tweetnum, tweet in enumerate(search['statuses']):
                print tweet
                # {u'contributors': None, u'truncated': False, u'text': u'In our third of five LCS games this week, we face scoreboard leaders Cloud 9 http://t.co/Hg1ouV1Ihn', u'in_reply_to_status_id': None, u'id': 368076075248545792L, u'favorite_count': 0, u'source': u'web', u'retweeted': False, u'coordinates': None, u'entities': {u'symbols': [], u'user_mentions': [], u'hashtags': [], u'urls': [{u'url': u'http://t.co/Hg1ouV1Ihn', u'indices': [77, 99], u'expanded_url': u'http://www.team-dignitas.net/articles/news/League-of-Legends/3794/LCS-Team-Dignitas-vs.-Cloud-9/', u'display_url': u'team-dignitas.net/articles/news/\u2026'}]}, u'in_reply_to_screen_name': None, u'in_reply_to_user_id': None, u'retweet_count': 0, u'id_str': u'368076075248545792', u'favorited': False, u'user': {u'follow_request_sent': None, u'profile_use_background_image': True, u'default_profile_image': False, u'id': 20734751, u'verified': False, u'profile_text_color': u'0C3E53', u'profile_image_url_https': u'https://si0.twimg.com/profile_images/958663238/fullcolor-head_normal.jpg', u'profile_sidebar_fill_color': u'FFF7CC', u'entities': {u'url': {u'urls': [{u'url': u'http://t.co/9oS5fsRQyt', u'indices': [0, 22], u'expanded_url': u'http://www.team-dignitas.net', u'display_url': u'team-dignitas.net'}]}, u'description': {u'urls': []}}, u'followers_count': 45843, u'profile_sidebar_border_color': u'000000', u'id_str': u'20734751', u'profile_background_color': u'BADFCD', u'listed_count': 486, u'profile_background_image_url_https': u'https://si0.twimg.com/profile_background_images/378800000040895525/bde7e8dc3837d2737376336a13fb0dac.jpeg', u'utc_offset': 3600, u'statuses_count': 13908, u'description': u'Team Dignitas - The official twitter page for one of the worlds leading professional gaming companies.', u'friends_count': 430, u'location': u'Surrey', u'profile_link_color': u'FF0000', u'profile_image_url': u'http://a0.twimg.com/profile_images/958663238/fullcolor-head_normal.jpg', u'following': None, u'geo_enabled': True, u'profile_banner_url': u'https://pbs.twimg.com/profile_banners/20734751/1352062186', u'profile_background_image_url': u'http://a0.twimg.com/profile_background_images/378800000040895525/bde7e8dc3837d2737376336a13fb0dac.jpeg', u'screen_name': u'TeamDignitas', u'lang': u'en', u'profile_background_tile': False, u'favourites_count': 25, u'name': u'Team Dignitas', u'notifications': None, u'url': u'http://t.co/9oS5fsRQyt', u'created_at': u'Fri Feb 13 00:20:50 +0000 2009', u'contributors_enabled': False, u'time_zone': u'London', u'protected': False, u'default_profile': False, u'is_translator': False}, u'geo': None, u'in_reply_to_user_id_str': None, u'possibly_sensitive': False, u'lang': u'en', u'created_at': u'Thu Aug 15 18:25:49 +0000 2013', u'in_reply_to_status_id_str': None, u'place': None, u'metadata': {u'iso_language_code': u'en', u'result_type': u'recent'}}
                tweetitem = Tweet(tweet['created_at'], tweet['user']['name'], tweet['user']['screen_name'],
                                  tweet['text'], tweet['entities']['hashtags'], tweet['id_str'], tweet['user']['id'],
                                  tweet['metadata']['iso_language_code'], tweet['user']['profile_image_url'])
                if tweet['metadata']['iso_language_code'] == 'en':
                    print 'nope'
                    self.TweetList.append(tweetitem)
                # for index, detail in enumerate(tweetdetails):
                #     print tweetnum, index, detail
                #
                # self.ui.tweet_table.setItem(tweetnum, index, QtGui.QTableWidgetItem(detail))

            #print Tweet.get_tweet_count()
            #print tweetlist
            # self.ui.tweet_table.setRowCount(len(search))

            # self.updateSignal.emit()
            self.BuildTweetXML()

    def BuildTweetXML(self):
        tweets = 0
        TweetXML = '<templateData>'
        for SingleTweet in self.TweetList:
            TweetXML = TweetXML + """
    <componentData id=\"fullname""" + str(tweets) + """\"><data id="text" value=\"""" + SingleTweet.FullName + """\"/></componentData>
	<componentData id="nickname""" + str(tweets) + """\"><data id="text" value=\"@""" + SingleTweet.Nick + """\"/></componentData>
	<componentData id="tweet""" + str(tweets) + """\"><data id="text" value=\"""" + SingleTweet.TweetContent + """\"/></componentData>
	<componentData id="imageContainer""" + str(tweets) + """\"><data id="image" value=\"""" + SingleTweet.BiggerImage + """\"/></componentData>\n"""
            tweets = tweets + 1
        TweetXML = TweetXML + '\n</templateData>'
        with open("templates/tweets.xml", "wb") as f:
            f.write(TweetXML.encode("UTF-8"))
            print "XML SAVED"


class Tweet:
    # class variables
    __tweet_count = 0
    # constructor
    def __init__(self, created_at="", fullname="", nickname="", tweetcontent="", hashtags=[], id_str="", user_id=0,
                 lang="", profileimg="", shown=False):
        # instance variables
        self.CreatedAt = created_at
        self.FullName = fullname
        self.Nick = nickname
        self.TweetContent = tweetcontent
        self.HashTags = hashtags
        self.StringID = id_str
        self.UserID = user_id
        self.shown = shown
        self.lang = lang
        self.ProfileImage = profileimg
        self.BiggerImage = re.sub('_normal', '_bigger', self.ProfileImage)
        self.TweetID = Tweet.__tweet_count + 1
        Tweet.__tweet_count += 1

    # static methods
    @staticmethod
    def get_tweet_count():
        return Tweet.__tweet_count


    def getUID(self):
        return self.TweetID

    # instance methods
    def hasShown(self):
        return self.shown

    def show(self):
        if self.shown:
            # if we try and show a tweet that has already been shown it will return False
            return False
        else:
            # if it hasn't been shown it will set shown to True and return True
            self.shown = True
            return True

    def getId(self):
        return self.StringID

    def getLang(self):
        return self.lang

    def PrintTweet(self):
        print self.TweetContent


def main():
    app = QtGui.QApplication(sys.argv)
    window = Main()
    #window.showMaximized()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
