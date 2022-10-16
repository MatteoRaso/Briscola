from decision import *
from deck import *
from node import *

node_1 = node()
node_2 = node()
node_3 = node()
node_4 = node()

node_1._init_()
node_2._init_()
node_3._init_()
node_4._init_()

node_1.value = 5
nodes = [node_1, node_2, node_3, node_4]
D = deck("B")

hand = [D[0], D[1], D[2]]
answer = decision(nodes, hand, "B")
assert answer == hand[0]

answer = decision(nodes, hand, "C")
assert answer == hand[0]
