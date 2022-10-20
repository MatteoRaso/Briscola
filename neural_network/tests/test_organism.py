from organism import *

#Simulates a generation class, without having
#to actually implement the full class.
class mini_gen():
    def _init_(self):
        self.innovation_number = 0

    def new_innovation(self, y):
        return True

O = organism()
O._init_()

node_1 = node()
node_2 = node()
node_1._init_()
node_2._init_()

G = mini_gen()
G._init_()

O.add_connection(node_1, node_2, G)
assert O.connection_genes[0][-1] == 1
assert G.innovation_number == 1
assert O.connection_genes[0][2] == node_2.incoming[0][2]

node_3 = node()
node_3._init_()
node_4 = node()
node_4._init_()

y = [node_2, node_3, 1, G.innovation_number]
O.connection_genes.append(y)
node_3.incoming.append(y)

O.add_node(node_4, y, G)
assert y not in O.connection_genes
assert G.innovation_number == 3
assert [node_2, node_4, 1, 2] in O.connection_genes
assert [node_4, node_3, 1, 3] in O.connection_genes
assert len(O.connection_genes) >= 2

w = O.connection_genes[0][2]

O.mutate_weight(0)
assert w != O.connection_genes[0][2]
