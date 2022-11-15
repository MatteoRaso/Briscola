from generation import *
from briscola_game import *

print("Initializing...")

G = generation()
G._init_()
G.total_members = 200
num_games = 100
batch = True
batch_size = 10

S = species()
S._init_()
S.allowed_members = G.total_members

R = organism()
R._init_()
N_0 = node()
N_1 = node()
N_2 = node()
N_3 = node()
N_0._init_()
N_1._init_()
N_2._init_()
N_3._init_()
R.output_nodes.append(N_0)
R.output_nodes.append(N_1)
R.output_nodes.append(N_2)
R.output_nodes.append(N_3)
for i in range(0, 45):
    N = node()
    N._init_()
    R.input_nodes.append(N)
    R.connection_genes.append([R.input_nodes[-1], R.output_nodes[0], np.random.random(), G.innovation_number])
    G.innovation_number += 1
    R.output_nodes[0].incoming.append(R.connection_genes[-1])
    R.connection_genes.append([R.input_nodes[-1], R.output_nodes[1], np.random.random(), G.innovation_number])
    G.innovation_number += 1
    R.output_nodes[1].incoming.append(R.connection_genes[-1])
    R.connection_genes.append([R.input_nodes[-1], R.output_nodes[2], np.random.random(), G.innovation_number])
    G.innovation_number += 1
    R.output_nodes[2].incoming.append(R.connection_genes[-1])
    R.connection_genes.append([R.input_nodes[-1], R.output_nodes[3], np.random.random(), G.innovation_number])
    G.innovation_number += 1
    R.output_nodes[3].incoming.append(R.connection_genes[-1])

S.reference_member = R
G.innovations = R.connection_genes.copy()

for i in range(0, G.total_members):
    O = organism()
    O._init_()
    O.input_nodes = R.input_nodes.copy()
    O.output_nodes = R.output_nodes.copy()
    O.connection_genes = R.connection_genes.copy()
    O.add_name()
    O.get_total_weight()

    if np.random.random() < O.mutate_weight_chance:
        O.mutate_weight(np.random.randint(0, len(O.connection_genes)))

    if np.random.random() < O.mutate_activation_chance:
        O.mutate_activation_function()

    if np.random.random() < O.add_node_chance:
        N = node()
        N._init_()
        C = O.connection_genes[np.random.randint(0, len(O.connection_genes))]
        O.add_node(N, C, G)

        if np.random.random() < O.add_connection_chance:
            potential_node_1 = np.append(O.input_nodes, np.append(O.hidden_nodes, O.output_nodes))
            potential_node_2 = np.append(O.hidden_nodes, O.output_nodes)

            node_1 = potential_node_1[np.random.randint(0, len(potential_node_1))]
            node_2 = potential_node_2[np.random.randint(0, len(potential_node_2))]
            O.add_connection(node_1, node_2, G)

    S.members.append(O)

G.species.append(S)

print("Initialization complete")

eval_array = [R]
counter = 0

while True:
    if len(G.species) > 1:
        G.total_members = 300
        num_games = 200

    if batch:
        for s in G.species:
            for i in range(0, len(s.members)):
                new_array = s.members.copy()
                new_array.remove(s.members[i])
                opponents = np.random.choice(new_array, 10, False)
                for j in range(0, len(opponents)):
                    if i != j:
                        for k in range(0, num_games // 2):
                            briscola_game(s.members[i], opponents[j])
                            briscola_game(opponents[j], s.members[i])

    else:
        for s in G.species:
            for i in range(0, len(s.members)):
                for j in range(0, len(s.members)):
                    if i != j:
                        for k in range(0, num_games // 2):
                            briscola_game(s.members[i], s.members[j])

    species_copy = G.species.copy()
    for s in G.species:
        s.get_adjusted_fitness()
        s.get_average_adjusted_fitness()
        s.sort_by_adjusted_fitness()
        s.purge()

        if len(s.members) == 0:
            species_copy.remove(s)

    G.species = species_copy.copy()
    G.assign_allowed_members()
    G.create_new_species()
    for s in G.species:
        while len(s.members) < s.allowed_members:
            mom = s.members[np.random.randint(0, len(s.members))]
            dad = s.members[np.random.randint(0, len(s.members))]
            s.breed(mom, dad, G)

    s = G.species[np.random.randint(0, len(G.species))]
    m = s.members[np.random.randint(0, len(s.members))]

    new_eval_member = organism()
    new_eval_member._init_()
    new_eval_member.input_nodes = m.input_nodes.copy()
    new_eval_member.hidden_nodes = m.hidden_nodes.copy()
    new_eval_member.output_nodes = m.output_nodes.copy()
    new_eval_member.connection_genes = m.connection_genes.copy()

    eval_array[-1].fitness = 0

    for i in range(0, 500):
        try:
            briscola_game(eval_array[-1], new_eval_member)
            briscola_game(new_eval_member, eval_array[-1])

        except IndexError:
            print(len(eval_array[-1].input_nodes))
            print(len(new_eval_member.input_nodes))

    eval_rating = new_eval_member.fitness / (eval_array[-1].fitness + new_eval_member.fitness)
    eval_array.append(new_eval_member)
    print("The evaluation rating for generation " + str(counter) + " is " + str(eval_rating * 100) + "%.")

    np.save("Generation_" + str(counter) + ".npy", np.array([G.species]))
    if len(eval_array) % 10 == 0:
        np.save("eval_array.npy", eval_array)

    counter += 1
