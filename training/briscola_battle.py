#!/usr/bin/python
#Since Briscola is somewhat RNG-based, we can't judge an AI off of one game.
#I don't know what the ideal number of games we need the AI to play,
#but 200 games seems like more than enough.

from briscola_game import *

num_of_games = 200

def presquilla_battle(player_1, player_2):
    #Half will be with player_1 going first
    for i in range(0, num_of_games / 2):
        briscola_game(player_1, player_2)

    for i in range(0, num_of_games / 2):
        briscola_game(player_2, player_1)
