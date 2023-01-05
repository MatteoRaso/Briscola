"""
This file is part of Briscola.

Briscola is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

Briscola is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with Briscola. If not, see <https://www.gnu.org/licenses/>. 
"""
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
    player_1.state_array = [120]
    player_2.state_array = [120]
    player_1_action = max(0, player_1.get_best_action(player_1.state_array))
    player_2_action = max(0, player_2.get_best_action(player_2.state_array))
    card_1 = player_1.play_card(player_2, briscola)
    card_2 = player_2.play_card(player_1, briscola)
    del playing_deck[0:6]
    player_1, player_2 = better_card(card_1, card_2, player_1, player_2, briscola)
    player_1.hand.remove(card_1)
    player_2.hand.remove(card_2)
    player_1_reward = player_1.points - player_2.points
    player_2_reward = -player_1_reward
    player_1_new_state = player_1.state_array[-1] + player_1_reward
    player_2_new_state = player_2.state_array[-1] + player_2_reward
    player_1.learn(player_1_reward, player_1_new_state, player_1_action)
    player_2.learn(player_2_reward, player_2_new_state, player_2_action)

    while len(playing_deck) > 0:
        #In Briscola, whoever has the best card draws and plays first.
        if player_1.best:
            player_1.hand.append(playing_deck[0])
            playing_deck.pop(0)
            player_2.hand.append(playing_deck[0])
            playing_deck.pop(0)
            player_1_action = max(0, player_1.get_best_action(player_1.state_array))
            player_2_action = max(0, player_2.get_best_action(player_2.state_array))
            card_1 = player_1.play_card(player_2, briscola)
            card_2 = player_2.play_card(player_1, briscola)
            player_1, player_2 = better_card(card_1, card_2, player_1, player_2, briscola)
            player_1_reward = player_1.points - player_2.points
            player_2_reward = -player_1_reward
            player_1_new_state = player_1.state_array[-1] + player_1_reward
            player_2_new_state = player_2.state_array[-1] + player_2_reward
            player_1.learn(player_1_reward, player_1_new_state, player_1_action)
            player_2.learn(player_2_reward, player_2_new_state, player_2_action)

        else:
            player_2.hand.append(playing_deck[0])
            playing_deck.pop(0)
            player_1.hand.append(playing_deck[0])
            playing_deck.pop(0)
            player_1_action = max(0, player_1.get_best_action(player_1.state_array))
            player_2_action = max(0, player_2.get_best_action(player_2.state_array))
            card_1 = player_1.play_card(player_2, briscola)
            card_2 = player_2.play_card(player_1, briscola)
            player_2, player_1 = better_card(card_1, card_2, player_2, player_1, briscola)
            player_1_reward = player_1.points - player_2.points
            player_2_reward = -player_1_reward
            player_1_new_state = player_1.state_array[-1] + player_1_reward
            player_2_new_state = player_2.state_array[-1] + player_2_reward
            player_1.learn(player_1_reward, player_1_new_state, player_1_action)
            player_2.learn(player_2_reward, player_2_new_state, player_2_action)

        player_1.hand.remove(card_1)
        player_2.hand.remove(card_2)

    for i in range(0, 2):
        if player_1.best:
            player_1_action = max(0, player_1.get_best_action(player_1.state_array))
            player_2_action = max(0, player_2.get_best_action(player_2.state_array))
            card_1 = player_1.play_card(player_2, briscola)
            card_2 = player_2.play_card(player_1, briscola)
            player_1, player_2 = better_card(card_1, card_2, player_1, player_2, briscola)
            player_1_reward = player_1.points - player_2.points
            player_2_reward = -player_1_reward
            player_1_new_state = player_1.state_array[-1] + player_1_reward
            player_2_new_state = player_2.state_array[-1] + player_2_reward
            player_1.learn(player_1_reward, player_1_new_state, player_1_action)
            player_2.learn(player_2_reward, player_2_new_state, player_2_action)

        else:
            player_1_action = max(0, player_1.get_best_action(player_1.state_array))
            player_2_action = max(0, player_2.get_best_action(player_2.state_array))
            card_1 = player_1.play_card(player_2, briscola)
            card_2 = player_2.play_card(player_1, briscola)
            player_2, player_1 = better_card(card_1, card_2, player_2, player_1, briscola)
            player_1_reward = player_1.points - player_2.points
            player_2_reward = -player_1_reward
            player_1_new_state = player_1.state_array[-1] + player_1_reward
            player_2_new_state = player_2.state_array[-1] + player_2_reward
            player_1.learn(player_1_reward, player_1_new_state, player_1_action)
            player_2.learn(player_2_reward, player_2_new_state, player_2_action)

        player_1.hand.remove(card_1)
        player_2.hand.remove(card_2)

    if player_1.points >= player_2.points:
        player_1.wins += 1

    else:
        player_2.wins += 1
