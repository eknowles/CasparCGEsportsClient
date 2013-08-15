#!/usr/bin/python
import os
import sys
import shutil
import errno
import logging
import datetime
import webbrowser
import subprocess
import json
import socket
import urllib2
from time import time
from PIL import Image
from PyQt4 import QtCore, QtGui
from windowUi import Ui_MainWindow
from ConfigParser import SafeConfigParser
from twython import Twython
import oauth2 as oauth

#======================================================================
# Setup logging
#======================================================================
#logging.basicConfig(filename='gnb.log', level=logging.DEBUG, format='[%(asctime)s] %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
logging.basicConfig(level=logging.DEBUG, format='[%(asctime)s] %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', handlers=[logging.FileHandler("console.log"), logging.StreamHandler()])
logging.info('Program Launched')

class Tweet:
    def __init__(self, data):
        time = ''
        fullname = ''
        nickname = ''
        content = ''
        

class Main(QtGui.QMainWindow):
    updateSignal = QtCore.pyqtSignal()
    def __init__(self):
        #Qt main window init
        QtGui.QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        
        self.ui.get_tweets_btn.clicked.connect(self.SearchTweets)
        self.updateSignal.connect(self.update_table)


    def sendCommand(self, command=""):
        commands = command.split("|*|")
        self.loadSettings()
        bufferSize = 16384
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        try:
            s.connect(("127.0.0.1", "5250"))
        except socket.error, msg:
            s = None

        if s is None:
            """WARNING!!! NOT CONNECTED"""
            return None
        else:
            data = ""
            for i in range(len(commands)):
                message=commands[i] + "\r\n"
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
        tweetcount = self.ui.tweetspinBox.value()
        search = twitter.search(q=term, result_type='recent', count=tweetcount)
        
        self.ui.tweet_table.setRowCount(tweetcount)

        
        #for tweet in search['statuses']:
        for tweetnum, tweet in enumerate(search['statuses']):
            # {u'contributors': None, u'truncated': False, u'text': u'In our third of five LCS games this week, we face scoreboard leaders Cloud 9 http://t.co/Hg1ouV1Ihn', u'in_reply_to_status_id': None, u'id': 368076075248545792L, u'favorite_count': 0, u'source': u'web', u'retweeted': False, u'coordinates': None, u'entities': {u'symbols': [], u'user_mentions': [], u'hashtags': [], u'urls': [{u'url': u'http://t.co/Hg1ouV1Ihn', u'indices': [77, 99], u'expanded_url': u'http://www.team-dignitas.net/articles/news/League-of-Legends/3794/LCS-Team-Dignitas-vs.-Cloud-9/', u'display_url': u'team-dignitas.net/articles/news/\u2026'}]}, u'in_reply_to_screen_name': None, u'in_reply_to_user_id': None, u'retweet_count': 0, u'id_str': u'368076075248545792', u'favorited': False, u'user': {u'follow_request_sent': None, u'profile_use_background_image': True, u'default_profile_image': False, u'id': 20734751, u'verified': False, u'profile_text_color': u'0C3E53', u'profile_image_url_https': u'https://si0.twimg.com/profile_images/958663238/fullcolor-head_normal.jpg', u'profile_sidebar_fill_color': u'FFF7CC', u'entities': {u'url': {u'urls': [{u'url': u'http://t.co/9oS5fsRQyt', u'indices': [0, 22], u'expanded_url': u'http://www.team-dignitas.net', u'display_url': u'team-dignitas.net'}]}, u'description': {u'urls': []}}, u'followers_count': 45843, u'profile_sidebar_border_color': u'000000', u'id_str': u'20734751', u'profile_background_color': u'BADFCD', u'listed_count': 486, u'profile_background_image_url_https': u'https://si0.twimg.com/profile_background_images/378800000040895525/bde7e8dc3837d2737376336a13fb0dac.jpeg', u'utc_offset': 3600, u'statuses_count': 13908, u'description': u'Team Dignitas - The official twitter page for one of the worlds leading professional gaming companies.', u'friends_count': 430, u'location': u'Surrey', u'profile_link_color': u'FF0000', u'profile_image_url': u'http://a0.twimg.com/profile_images/958663238/fullcolor-head_normal.jpg', u'following': None, u'geo_enabled': True, u'profile_banner_url': u'https://pbs.twimg.com/profile_banners/20734751/1352062186', u'profile_background_image_url': u'http://a0.twimg.com/profile_background_images/378800000040895525/bde7e8dc3837d2737376336a13fb0dac.jpeg', u'screen_name': u'TeamDignitas', u'lang': u'en', u'profile_background_tile': False, u'favourites_count': 25, u'name': u'Team Dignitas', u'notifications': None, u'url': u'http://t.co/9oS5fsRQyt', u'created_at': u'Fri Feb 13 00:20:50 +0000 2009', u'contributors_enabled': False, u'time_zone': u'London', u'protected': False, u'default_profile': False, u'is_translator': False}, u'geo': None, u'in_reply_to_user_id_str': None, u'possibly_sensitive': False, u'lang': u'en', u'created_at': u'Thu Aug 15 18:25:49 +0000 2013', u'in_reply_to_status_id_str': None, u'place': None, u'metadata': {u'iso_language_code': u'en', u'result_type': u'recent'}}
            print tweet
            #print tweet['iso_language_code']
#            print tweet
#            print tweet['created_at']
#            print tweet['metadata']['iso_language_code']
#            print tweet['user']['screen_name']
#            print tweet['user']['name']
#            print tweet['user']['profile_image_url']
#            print tweet['user']['created_at']
#            print tweet['text']
            tweetdetails = []
            tweetdetails = [tweet['created_at'], tweet['user']['name'], '@' + tweet['user']['screen_name'], tweet['text']]
            
            for index, detail in enumerate(tweetdetails):
                #print tweetnum, index, detail
                self.ui.tweet_table.setItem(tweetnum, index, QtGui.QTableWidgetItem(detail))
            
            
        #self.ui.tweet_table.setRowCount(len(search))
            
        self.updateSignal.emit()

    def update_table(self):
        self.ui.tweet_table.sortItems(0,QtCore.Qt.DescendingOrder)
        
        
def main():
    app = QtGui.QApplication(sys.argv)
    window = Main()
    #window.showMaximized()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
