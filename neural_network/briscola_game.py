"""
This file is part of Briscola.
Briscola is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License
as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
Briscola is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty
 of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
You should have received a copy of the GNU General Public License along with Briscola. If not, see <https://www.gnu.org/licenses/>.
"""

#Simulates a single game of Briscola.

from deck import *
from decision import *
from better_card import *
import numpy as np

def briscola_game(player_1, player_2):
    player_1.clear_nodes()
    player_2.clear_nodes()
    player_1_best = False
    for i in range(0, len(player_1.input_nodes)):
        player_1.input_nodes[i].value_1 = 0
        player_2.input_nodes[i].value_1 = 0
        player_1.input_nodes[i].value_2 = 0
        player_2.input_nodes[i].value_2 = 0

    briscola_dict = {"B": 40, "C": 41, "D": 42, "S": 43}
    playing_deck = deck()
    np.random.shuffle(playing_deck)
    revealed_card = playing_deck[0]
    #Letting the AI know which suit is the Briscola
    player_1.input_nodes[revealed_card.index].value_1 = 2
    player_2.input_nodes[revealed_card.index].value_2 = 2
    player_1.input_nodes[briscola_dict[revealed_card.suit]].value_1 = 1
    player_2.input_nodes[briscola_dict[revealed_card.suit]].value_2 = 1
    player_1.hand = playing_deck[1:4]
    player_2.hand = playing_deck[4:7]
    for i in range(0, 3):
        player_1.input_nodes[player_1.hand[i].index].value_1 = 1
        player_2.input_nodes[player_2.hand[i].index].value_2 = 1

    for i in range(0, 4):
        player_1.output_nodes[i].get_value_1()
        player_2.output_nodes[i].get_value_2()

    card_1 = decision(player_1.output_nodes, player_1.hand, revealed_card.suit, True)
    player_1.input_nodes[card_1.index].value_1 = -1
    player_2.input_nodes[card_1.index].value_2 = -1
    for i in range(0, 4):
        player_2.output_nodes[i].get_value_2()

    card_2 = decision(player_2.output_nodes, player_2.hand, revealed_card.suit, False)
    player_1.input_nodes[card_2.index].value_1 = -1
    player_2.input_nodes[card_2.index].value_2 = -1
    del playing_deck[0:7]
    points = better_card(card_1, card_2, revealed_card.suit)

    if points > 0:
        player_1.input_nodes[44].value_1 += points
        player_1_best = True

    elif points < 0:
        player_2.input_nodes[44].value_2 -= points
        player_1_best = False

    player_1.hand.remove(card_1)
    player_2.hand.remove(card_2)

    while len(playing_deck) >= 2:
        player_1.clear_nodes()
        player_2.clear_nodes()
        #In Briscola, whoever has the best card draws and plays first.
        if player_1_best:
            player_1.hand.append(playing_deck[0])
            player_1.input_nodes[playing_deck[0].index].value_1 = 1
            playing_deck.pop(0)
            player_2.hand.append(playing_deck[0])
            player_2.input_nodes[playing_deck[0].index].value_2 = 1
            playing_deck.pop(0)

            for i in range(0, 4):
                player_1.output_nodes[i].get_value_1()

            card_1 = decision(player_1.output_nodes, player_1.hand, revealed_card.suit, True)
            player_1.input_nodes[card_1.index].value_1 = -1
            player_2.input_nodes[card_1.index].value_2 = -1

            for i in range(0, 4):
                player_2.output_nodes[i].get_value_2()

            card_2 = decision(player_2.output_nodes, player_2.hand, revealed_card.suit, False)
            player_1.input_nodes[card_2.index].value_1 = -1
            player_2.input_nodes[card_2.index].value_2 = -1

        else:
            player_2.hand.append(playing_deck[0])
            player_2.input_nodes[playing_deck[0].index].value_2 = 1
            playing_deck.pop(0)
            player_1.hand.append(playing_deck[0])
            player_1.input_nodes[playing_deck[0].index].value_1 = 1
            playing_deck.pop(0)

            for i in range(0, 4):
                player_2.output_nodes[i].get_value_2()

            card_2 = decision(player_2.output_nodes, player_2.hand, revealed_card.suit, False)
            player_1.input_nodes[card_2.index].value_1 = -1
            player_2.input_nodes[card_2.index].value_2 = -1

            for i in range(0, 4):
                player_1.output_nodes[i].get_value_1()

            card_1 = decision(player_1.output_nodes, player_1.hand, revealed_card.suit, True)
            player_1.input_nodes[card_1.index].value_1 = -1
            player_2.input_nodes[card_1.index].value_2 = -1

        points = better_card(card_1, card_2, revealed_card.suit)

        player_1.hand.remove(card_1)
        player_2.hand.remove(card_2)

        if points > 0:
            player_1.input_nodes[44].value_1 += points
            player_1_best = True

        elif points < 0:
            player_2.input_nodes[44].value_2 -= points
            player_1_best = False

    if player_1_best:
        player_1.hand.append(revealed_card)
        player_2.hand.append(playing_deck[0])

    else:
        player_2.hand.append(revealed_card)
        player_1.hand.append(playing_deck[0])

    playing_deck.pop(0)

    for i in range(0, 3):
        player_1.clear_nodes()
        player_2.clear_nodes()

        if player_1_best:
            for j in range(0, 4):
                player_1.output_nodes[i].get_value_1()

            card_1 = decision(player_1.output_nodes, player_1.hand, revealed_card.suit, True)
            player_1.input_nodes[card_1.index].value_1 = -1
            player_2.input_nodes[card_1.index].value_2 = -1

            for j in range(0, 4):
                player_2.output_nodes[i].get_value_2()

            card_2 = decision(player_2.output_nodes, player_2.hand, revealed_card.suit, False)
            player_1.input_nodes[card_2.index].value_1 = -1
            player_2.input_nodes[card_2.index].value_2 = -1
            points = better_card(card_1, card_2, revealed_card.suit)

            player_1.hand.remove(card_1)
            player_2.hand.remove(card_2)

        else:
            for j in range(0, 4):
                player_2.output_nodes[i].get_value_2()

            card_2 = decision(player_2.output_nodes, player_2.hand, revealed_card.suit, False)
            player_1.input_nodes[card_2.index].value_1 = -1
            player_2.input_nodes[card_2.index].value_2 = -1

            for j in range(0, 4):
                player_1.output_nodes[i].get_value_1()

            card_1 = decision(player_1.output_nodes, player_1.hand, revealed_card.suit, True)
            player_1.input_nodes[card_1.index].value_1 = -1
            player_2.input_nodes[card_1.index].value_2 = -1
            points = better_card(card_1, card_2, revealed_card.suit)

            player_1.hand.remove(card_1)
            player_2.hand.remove(card_2)

        if points > 0:
            player_1.input_nodes[44].value_1 += points
            player_1_best = True

        elif points < 0:
            player_2.input_nodes[44].value_2 -= points
            player_1_best = False

    if player_1.input_nodes[44].value_1 >= 60:
        player_1.fitness += 1

    else:
        player_2.fitness += 1

