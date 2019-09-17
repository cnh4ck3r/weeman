##
## complete.py - auto complete with readline
##
## Credit to (https://cnh4ck3r.blogspot.com)
##
## Written by cnh4ck3r 
##

import readline

array = ["set", "show", "help", "port", "url", "action_url", "user_agent","clear", "quit", "run", "banner"]

class auto(object):

    def __init__(self, options):
        self.options = sorted(options)

    def complete(self, text, state):
        if state == 0:
            if text:
                self.matches = [s for s in self.options
                                    if s and s.startswith(text)]
            else:
                self.matches = self.options[:]
        try:
            return self.matches[state]
        except IndexError:
            return None

def complete(array):
	completer = auto(array)
	readline.set_completer(completer.complete)
	readline.parse_and_bind('tab:complete')
