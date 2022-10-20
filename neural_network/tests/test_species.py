from species import *

class mini_gen():
    def _init_(self):
        self.innovation_number = 0

    def new_innovation(self, y):
        return True

S = species()
S._init_()

for i in range(0, 5):
    O = organism()
    O._init_()
    S.members.append(O)

S.allowed_members = 3

S.purge()
assert len(S.members) == 0

S.allowed_members = 30

for i in range(0, 20):
    O = organism()
    O._init_()
    O.fitness = 1
    S.members.append(O)

S.purge()
assert len(S.members) == 10

S.get_adjusted_fitness()
assert S.members[0].adjusted_fitness == 1 / 9

S.get_average_adjusted_fitness()
#Floating point error, but otherwise very accurate.
assert abs(S.average_adjusted_fitness - 1 / 9) < 1e-6

G = mini_gen()
G._init_()
node_1 = node()
node_2 = node()
node_3 = node()
node_1._init_()
node_2._init_()
node_3._init_()
S.members[0].fitness = 2
S.members[0].connection_genes = [[node_1, node_2, 1, G.innovation_number],
                                 [node_2, node_3, 1, G.innovation_number],
                                 [node_1, node_3, 1, G.innovation_number]]
S.members[1].connection_genes = [[node_1, node_2, 1, G.innovation_number],
                                 [node_2, node_3, 1, G.innovation_number]]

S.breed(S.members[0], S.members[1], G)
assert len(S.members[-1].connection_genes) == 3
