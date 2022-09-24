#!/usr/bin/python
#Simulates a single game of Briscola.

from deck import *
from better_card import *
import numpy as np

def briscola_game(player_1, player_2):
    index = np.random.randint(0, 4)
    briscola = ['B', 'C', 'D', 'S'][index]
    playing_deck = deck(briscola)
    np.random.shuffle(playing_deck)
    player_1.hand = playing_deck[0:3]
    player_2.hand = playing_deck[3:6]
    player_1.points = 0
    player_2.points = 0
    card_1 = player_1.play_card(player_2)
    card_2 = player_2.play_card(player_1)
    del playing_deck[0:6]
    player_1, player_2 = better_card(card_1, card_2, player_1, player_2, briscola)

    while len(playing_deck) > 0:
        #In Briscola, whoever has the best card draws and plays first.
        if player_1.best:
            player_1.hand.append(playing_deck[0])
            playing_deck.remove(0)
            player_2.hand.append(playing_deck[0])
            playing_deck.remove(0)
            player_1, player_2 = better_card(card_1, card_2, player_1, player_2, briscola)

        else:
            player_2.hand.append(playing_deck[0])
            playing_deck.remove(0)
            player_1.hand.append(playing_deck[0])
            playing_deck.remove(0)
            player_2, player_1 = better_card(card_1, card_2, player_2, player_1, briscola)

    if player_1.points >= player_2.points:
        player_1.wins += 1

    else:
        player_2.wins += 1
