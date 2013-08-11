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


class Main(QtGui.QMainWindow):
    updateSignal = QtCore.pyqtSignal()
    def __init__(self):
        #Qt main window init
        QtGui.QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        
        self.ui.get_tweets_btn.clicked.connect(self.SearchTweets)
        self.updateSignal.connect(self.update_table)
        
        
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
            tweetdetails = [tweet['created_at'], tweet['user']['name'], tweet['user']['screen_name'], tweet['text']]
            
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
