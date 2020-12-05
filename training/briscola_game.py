#!/usr/bin/python
#Simulates a single game of Briscola.

from deck import *
from better_card import *
import numpy as np

def briscola_game(player_1, player_2):
    index = np.random.randint(0, 4)
    briscola = ['bastone', 'coppa', 'dinadi', 'spade'][index]
    shuffle(deck)
    deal_deck(player_1, player_2)
    player_1.points = 0
    player_2.points = 0
    card_1 = player_1.play_card()
    card_2 = player_2.play_card()

    player_1, player_2 = better_card(card_1, card_2, player_1, player_2)

    while len(deck) > 0:
        #In Briscola, whoever has the best card draws and plays first.
        if player_1.best:
            player_1.hand.append(deck[0])
            deck.remove(0)
            player_2.hand.append(deck[0])
            deck.remove(0)
            player_1, player_2 = better_card(card_1, card_2, player_1, player_2)

        else:
            player_2.hand.append(deck[0])
            deck.remove(0)
            player_1.hand.append(deck[0])
            deck.remove(0)
            player_2, player_1 = better_card(card_1, card_2, player_2, player_1)

    #There are 120 points in a deck,
    player_1.fitness += player_1.points / 120
    player_2.fitness += player_2.points / 120
