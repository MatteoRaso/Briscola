#!/usr/bin/python

import numpy as np

class player():
    def _init_(self):
        self.hand = []
        self.points = 0
        self.fitness = 0
        #Binary, every known card is flipped to a 1.
        self.known_cards = np.zeros([1, 40])
        self.input = []

    def create_input(self):
        #This creates the input for the NN.
        self.input = [self.hand[0].suit, self.hand[1].suit, self.hand[2].suit,
                      self.hand[0].value, self.hand[1].value, self.hand[2].value]

      self.input.append(self.known_cards)

  def bin(self):
    #We need to put the output of the NN into one of three bins, since it
    #can only play one of the three hands in its hand.

    if self.NN.output >= 2:
        self.NN.output = 2

    elif self.NN.output <= 0:
        self.NN.output = 0

    else:
        self.NN.output = 1


