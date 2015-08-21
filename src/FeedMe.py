import feedparser
import json
import msvcrt
import itertools
import webbrowser
import threading
import time
import textwrap
import os
from Util.Printer import Printer
from Util.ScrollableList import ScrollableList as Slist


class FeedMe():
    ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
    PROXY = 'HTTP://170.2.59.25:8080'
    p = Printer(80)
    
    def __init__(self):
        ### DAIMLER SPECIFIC PROXY INFO ###
        os.environ["HTTP_PROXY"] = self.PROXY
        os.environ["HTTPS_PROXY"] = self.PROXY
        ###
        self.LISTLOCATION = os.path.join(self.ROOT_DIR, 'feedList')
        self.viewed = []
        try:
            self.readFeedList()
            
        except (OSError, IOError):
            self.p.printText('Creating feedList file ')
            self.p.printText('Press a to add feeds to the list')
            self.feedList = {}
            self.writeFeedList
            
        except (ValueError):
            self.p.printText('Press a to add feeds to the list')
            self.feedList = {}
            listFile.write(json.dumps(self.feedList))
            
        
    
            
    def printFeedList(self):
        for feed in self.feedList.iteritems():
            print feed[0], ' @:' , feed[1]
            
    def addFeed(self):
        title = raw_input("Title: ")
        url = raw_input("Url: ")
        test = feedparser.parse(url.strip())
        if len(test.entries)>0:   
            self.feedList[title.strip()] = url.strip()
            self.writeFeedList()
            
        elif test['bozo'] == 1:
            self.p.printError(
                    'Unable to load rss, following error was returned.\n')
            print test['bozo_exception']
        else:
            self.p.printError('Unable to load rss, Unknown error occured')
    
    def removeFeed(self, feed):
        del self.feedList[feed]
        self.writeFeedList()
        
    def readFeedList(self):
        listFile = open(self.LISTLOCATION, 'r')
        self.feedList = json.loads(listFile.read())
        listFile.close()
    
    def writeFeedList(self):
        listFile = open(self.LISTLOCATION, 'w')
        listFile.write(json.dumps(self.feedList))
        listFile.close()
        
    def main(self):
        self.run = True
        self.mainMenu()
    
    def mainMenu(self):
        while self.run == True:
            self.p.printText('Welcome to Feed Me, Console RSS feed reader \n' +
                             'Version: 1.0.1 \n')
            self.p.printText(
                    'a: add rss '+ 'b: browse '+ 'v: view rss list '+ 'q: quit')
            command = ord(msvcrt.getch())
            if command == 97:
                self.addFeed()
            elif command == 98:
                self.browse()
            elif command == 118:
                self.printFeedList()
            elif command == 113 or command == 27:
                self.run = False
                
    def browse(self):
        feeds = Slist(self.feedList)
        self.browsing = True
        
        while self.browsing == True:
            self.p.printText(feeds.current())
                
            command = ord(msvcrt.getch())
            if command == 224:
                arrow = ord(msvcrt.getch())
                if arrow == 80:
                    feeds.next()
                elif arrow == 75:
                    self.browsing = False
                elif arrow == 77:
                    self.openFeed(feeds.current())
                elif arrow == 83:
                    self.removeFeed(feeds.current())
                    self.browse()
                elif arrow == 72:
                    feeds.previous()
            elif command == 113 or command == 27:
                self.browsing = False
                self.run = False
                
    def openFeed(self, key):
        self.feedOpen = True
        try:
            parsed = feedparser.parse(self.feedList[key])
            try:
                self.p.printText('Last modified: ' + parsed.modified)
                modifiedTag = True
            except:
                modifiedTag = False
            feed = Slist(parsed.entries)
        except:
            self.p.printError("Can't load feed, check your internet connection")
        while self.feedOpen == True:
            entry = feed.current()
            try:
                self.p.printLink(entry['title'], entry['title'] in self.viewed)
            except:
                self.p.printError('Unable to display title')
            command = ord(msvcrt.getch())
            if command == 224:
                arrow = ord(msvcrt.getch())
                if arrow == 80:
                    feed.next()
                if arrow == 75:
                    self.feedOpen = False
                elif arrow == 77:
                    self.openEntry(entry)
                elif arrow == 72:
                    feed.previous()
            elif command == 114:
                if modifiedTag:
                    updated=feedparser.parse(self.feedList[key],modified=parsed.modified)
                    if updated.status == 200:
                        feed = Slist(updated.entries)
                        self.p.printStatus('Feed Updated, Last Modified: ' + updated.modified)
                        parsed = updated
                    else:
                        self.p.printStatus('Feed is up to date')
                else:
                    updated=feedparser.parse(self.feedList[key])
                    feed = Slist(updated.entries)
                    self.p.printStatus('Feed refreshed')
                    parsed = updated
            elif command == 113 or command == 27:
                self.feedOpen = False
                self.browsing = False
                self.run = False
                  
                    
    def openEntry(self, entry):
        self.viewed.append(entry["title"])
        self.p.printEntry(entry)
        
        self.entryOpen = True
        while self.entryOpen == True:
            command = ord(msvcrt.getch())
            if command == 224:
                if ord(msvcrt.getch()) == 75:
                    self.entryOpen = False
            elif command == 13:
                webbrowser.open(entry['link'])       
            elif command == 113 or command == 27:
                self.entryOpen = False
                self.feedOpen = False
                self.browsing = False
                self.run = False
                
      

        
       
            
            