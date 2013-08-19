#!/usr/bin/python
import sys
import logging
import socket
import re

from PyQt4 import QtGui, QtCore
from twython import Twython

from windowUi import Ui_MainWindow


logging.basicConfig(level=logging.DEBUG, format='[%(asctime)s] %(levelname)s: %(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p',
                    handlers=[logging.FileHandler("console.log"), logging.StreamHandler()])
logging.info('Program Launched')


class Main(QtGui.QMainWindow):
    # class variables
    # constructor
    def __init__(self):
        #Qt main window init
        QtGui.QMainWindow.__init__(self)
        # instance variables
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.LastCG = 0

        QtCore.QObject.connect(self.ui.get_tweets_btn, QtCore.SIGNAL('clicked()'), self.SearchTweets)

        # self.ui.get_tweets_btn.clicked.connect(self.SearchTweets)
        self.ui.console_go.clicked.connect(self.ConsoleCommand)
        self.ui.Console_ComingUp.clicked.connect(lambda: self.ProcessCommand(1))
        self.ui.Console_Sponsors.clicked.connect(lambda: self.ProcessCommand(2))
        self.ui.Console_TweetFeed.clicked.connect(lambda: self.ProcessCommand(3))
        self.ui.actionReload_Client.triggered.connect(self.LoadSettings)
        self.ui.actionQuit.triggered.connect(self.Quit)

        # Load Primary Settings (First load)
        self.LoadSettings()

    def LoadSettings(self):
        self.BGVideo = "HEATHD"
        self.BUG = "BUG"
        self.ProcessCommand(self.LastCG)
        self.sendCommand("CLEAR 1\r\nPLAY 1-1 " + self.BGVideo + " LOOP\r\nPLAY 1-10 CSGO LOOP")
        self.TweetList = []

    def Quit(self):
        self.ProcessCommand(self.LastCG)
        self.sendCommand("CLEAR 1")
        exit()


    def ProcessCommand(self, cmdnum=0):
        if self.LastCG == 0:
            # Hide Nothing
            print "NO LAST BUTTON"

        if self.LastCG == 1:
            cmd = "MIXER 1-10 FILL 0 0 1 1 25 easeinoutback"
            self.ui.Console_ComingUp.setChecked(0)
            self.sendCommand(str(cmd))

        if self.LastCG == 2:
            cmd = "MIXER 1-10 FILL 0 0 1 1 25 easeinoutback\r\nMIXER 1-10 OPACITY 1 25 easeinoutback\r\nMIXER 1-10 BLEND NORMAL"
            self.ui.Console_Sponsors.setChecked(0)
            self.sendCommand(str(cmd))

        if self.LastCG == 3:
            cmd = "MIXER 1-10 FILL 0 0 1 1 25 easeinoutback\r\nSTOP 1-9\r\nCG 1 STOP 20 \"DEMO\" 1"
            self.ui.Console_TweetFeed.setChecked(0)
            self.sendCommand(str(cmd))

        if not cmdnum == self.LastCG:

            if cmdnum == 0:
                self.LastCG = cmdnum

            if cmdnum == 1:
                # Coming Up Next
                self.ui.Console_ComingUp.setChecked(1)
                cmd = "MIXER 1-10 FILL 0 0 0.8 0.8 25 easeinoutback"
                self.sendCommand(str(cmd))
                self.LastCG = cmdnum

            if cmdnum == 2:
                # Show Sponsors
                self.ui.Console_Sponsors.setChecked(1)
                cmd = "MIXER 1-10 FILL 0.3 0.2 0.4 0.4 25 easeinoutback\r\nMIXER 1-10 OPACITY 1 25 easeinoutback\r\nMIXER 1-10 BLEND OVERLAY"
                self.sendCommand(str(cmd))
                self.LastCG = cmdnum

            if cmdnum == 3:
                # Show Sponsors
                self.ui.Console_TweetFeed.setChecked(1)
                cmd = "MIXER 1-10 FILL 0.05 0.2 0.6 0.6 25 easeinoutback\r\nPLAY 1-9 FEEDBG\r\nCG 1 ADD 20 \"DEMO\" 1"
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
                # {u'contributors': None, u'truncated': False, u'text': u'In our third of five LCS games this week, we face scoreboard leaders Cloud 9 http://t.co/Hg1ouV1Ihn', u'in_reply_to_status_id': None, u'id': 368076075248545792L, u'favorite_count': 0, u'source': u'web', u'retweeted': False, u'coordinates': None, u'entities': {u'symbols': [], u'user_mentions': [], u'hashtags': [], u'urls': [{u'url': u'http://t.co/Hg1ouV1Ihn', u'indices': [77, 99], u'expanded_url': u'http://www.team-dignitas.net/articles/news/League-of-Legends/3794/LCS-Team-Dignitas-vs.-Cloud-9/', u'display_url': u'team-dignitas.net/articles/news/\u2026'}]}, u'in_reply_to_screen_name': None, u'in_reply_to_user_id': None, u'retweet_count': 0, u'id_str': u'368076075248545792', u'favorited': False, u'user': {u'follow_request_sent': None, u'profile_use_background_image': True, u'default_profile_image': False, u'id': 20734751, u'verified': False, u'profile_text_color': u'0C3E53', u'profile_image_url_https': u'https://si0.twimg.com/profile_images/958663238/fullcolor-head_normal.jpg', u'profile_sidebar_fill_color': u'FFF7CC', u'entities': {u'url': {u'urls': [{u'url': u'http://t.co/9oS5fsRQyt', u'indices': [0, 22], u'expanded_url': u'http://www.team-dignitas.net', u'display_url': u'team-dignitas.net'}]}, u'description': {u'urls': []}}, u'followers_count': 45843, u'profile_sidebar_border_color': u'000000', u'id_str': u'20734751', u'profile_background_color': u'BADFCD', u'listed_count': 486, u'profile_background_image_url_https': u'https://si0.twimg.com/profile_background_images/378800000040895525/bde7e8dc3837d2737376336a13fb0dac.jpeg', u'utc_offset': 3600, u'statuses_count': 13908, u'description': u'Team Dignitas - The official twitter page for one of the worlds leading professional gaming companies.', u'friends_count': 430, u'location': u'Surrey', u'profile_link_color': u'FF0000', u'profile_image_url': u'http://a0.twimg.com/profile_images/958663238/fullcolor-head_normal.jpg', u'following': None, u'geo_enabled': True, u'profile_banner_url': u'https://pbs.twimg.com/profile_banners/20734751/1352062186', u'profile_background_image_url': u'http://a0.twimg.com/profile_background_images/378800000040895525/bde7e8dc3837d2737376336a13fb0dac.jpeg', u'screen_name': u'TeamDignitas', u'lang': u'en', u'profile_background_tile': False, u'favourites_count': 25, u'name': u'Team Dignitas', u'notifications': None, u'url': u'http://t.co/9oS5fsRQyt', u'created_at': u'Fri Feb 13 00:20:50 +0000 2009', u'contributors_enabled': False, u'time_zone': u'London', u'protected': False, u'default_profile': False, u'is_translator': False}, u'geo': None, u'in_reply_to_user_id_str': None, u'possibly_sensitive': False, u'lang': u'en', u'created_at': u'Thu Aug 15 18:25:49 +0000 2013', u'in_reply_to_status_id_str': None, u'place': None, u'metadata': {u'iso_language_code': u'en', u'result_type': u'recent'}}
                tweetitem = Tweet(tweet['created_at'], tweet['user']['name'], tweet['user']['screen_name'],
                                  tweet['text'], tweet['entities']['hashtags'], tweet['id_str'], tweet['user']['id'],
                                  tweet['metadata']['iso_language_code'], tweet['user']['profile_image_url'])
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
            print SingleTweet.HashTags
            TweetXML = TweetXML + """
    <componentData id=\"fullname""" + str(tweets) + """\">
		<data id="text" value=\"""" + SingleTweet.FullName + """\"/>
	</componentData>
	<componentData id="nickname""" + str(tweets) + """\">
		<data id="text" value=\"@""" + SingleTweet.Nick + """\"/>
	</componentData>
	<componentData id="tweet""" + str(tweets) + """\">
		<data id="text" value=\"""" + SingleTweet.TweetContent + """\"/>
	</componentData>
	<componentData id="imageContainer""" + str(tweets) + """\">
		<data id="image" value=\"""" + SingleTweet.BiggerImage + """\"/>
	</componentData>"""
            tweets = tweets + 1
        TweetXML = TweetXML + '\n</templateData>'
        with open("templates/data.xml", "wb") as f:
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
