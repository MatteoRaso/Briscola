import numpy as np
from player import *
from briscola_game import *

players = []

for i in range(1, 20):
    players.append(player())
    players[i - 1]._init_()
    players[i - 1].initialize_policy_and_value()
    players[i - 1].gamma = 0.05 * i
    players[i - 1].training_iterations = 300000
    players[i - 1].train()

for i in range(0, len(players)):
    for j in range(i, len(players)):
        if i != j:
            for k in range(0, 1000):
                briscola_game(players[i], players[j])

players.sort(key = lambda x: x.wins, reverse = True)
print("The best gamma value is " + str(players[0].gamma))
np.save("players.npy", players)
