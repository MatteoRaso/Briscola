from generation import *

S = species()
G = generation()
S._init_()
G._init_()

R = organism()
M = organism()
R._init_()
M._init_()
#Only looking at length, doesn't need to be accurate
R.connection_genes.append([0, 1, 1, 1, 1])
R.total_weight = 3
for i in range(0, 50):
    M.connection_genes.append([0, 1, 1, 1, 1])
M.total_weight = 50
S.reference_member = R

#print(G.passed_distance_threshold(M, S))
assert G.passed_distance_threshold(M, S)
M.total_weight = 3
#print(G.passed_distance_threshold(M, S))
assert not G.passed_distance_threshold(M, S)

G.innovations = R.connection_genes
assert not G.new_innovation(R.connection_genes[0])
assert G.new_innovation([0, 2, 1, 1, 1])

P = species()
P._init_()
P.reference_member = R
S.members.append(M)
N = organism()
N._init_()
N.connection_genes.append([4, 5, 1, 2, 3])
N.total_weight = 100
P.members.append(N)

G.species.append(P)
G.species.append(S)
G.create_new_species()
assert len(G.species) == 3
