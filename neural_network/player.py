"""
This file is part of Briscola.

Briscola is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

Briscola is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with Briscola. If not, see <https://www.gnu.org/licenses/>.
"""
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


