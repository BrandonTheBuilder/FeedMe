from HTMLStripper import MLStripper
from colorama import Fore
import textwrap

class Printer():
    def __init__(self, wrap):
        self.WRAP = wrap
        self.HS = MLStripper()
    
    def printText(self, text):
        print Fore.WHITE + text
        
    def printLink(self, text, viewed):
        if not viewed:
            print Fore.WHITE + text
        else:
            print Fore.MAGENTA + text
            
    def printEntry(self, entry):
        print '\n'
        try:
            summary = entry['summary']
            try:
                print Fore.WHITE + textwrap.fill(
                        self.HS.strip_tags(summary[:summary.find('<br')]),80)
                print '\n'
            except:
                print Fore.WHITE + textwrap.fill((summary + '\n'),80)
        except:
            pass
        try:
            print Fore.WHITE + entry['author'] 
        except:
            pass
        try:
            print Fore.WHITE + entry['published'] 
        except:
            pass
        print '\n\n'
            
    def printError(self, text):
        print Fore.RED + text