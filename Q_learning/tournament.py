"""
This file is part of Briscola.

Briscola is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

Briscola is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with Briscola. If not, see <https://www.gnu.org/licenses/>.
"""
import numpy as np
from player import *
from briscola_game import *

players = []

for i in range(1, 20):
    players.append(player())
    players[i - 1]._init_()
    players[i - 1].gamma = 0.05 * i
    players[i - 1].learning_rate = 0.05

#Training
for i in range(0, len(players)):
    for j in range(i, len(players)):
        if i != j:
            for k in range(0, 1000000):
                briscola_game(players[i], players[j])

            print("Training round complete. Beginning another training round.")
    print("Training for " + str(i) + " complete.")

for i in range(1, len(players)):
    if len(players[i].Q_values) != len(players[i - 1].Q_values):
        raise ValueError("Lengths don't match. Increase number of training games.")

    else:
        players[i].wins = 0

#Evaluation
for i in range(0, len(players)):
    for j in range(i, len(players)):
        if i != j:
            for k in range(0, 100):
                briscola_game(players[i], players[j])

players.sort(key = lambda x: x.wins, reverse = True)
print("The best gamma value is " + str(players[0].gamma))
for i in range(0, len(players)):
    print("Player with gamma " + str(players[i].gamma) + " had " + str(players[i].wins) + " wins.")

np.save("players.npy", players)
