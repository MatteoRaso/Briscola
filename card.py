#!/usr/bin/python

class card():
    def _init_(self):
        self.suit = ''
        self.is_briscola = False
        #A bit useless since we have the points attribute,
        #but we'll need to know the card value if we want to make a GUI.
        self.value = 0
        self.points = 0
        #Too long to explain this one here - see commit message
        self.index = -1

    def set_briscola(self, briscola):
        if self.suit == briscola:
            self.is_briscola = True
