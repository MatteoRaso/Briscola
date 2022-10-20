#A class for neural networks, which will
#be evolved by using the NEAT algorithm.
import numpy as np
from activation_functions import *
from node import *

class organism():
    def _init_(self):
        #Each connection node should be an array-like
        #recording the in-node, out-node, weight,
        #and an innovation number.
        self.connection_genes = []
        self.hidden_nodes = []
        self.input_nodes = []
        self.output_nodes = []
        self.excess_genes = 0
        self.add_node_chance = 0.05
        self.add_connection_chance = 0.05
        self.mutate_weight_chance = 0.05
        self.mutate_activation_chance = 0.05
        self.fitness = 0
        self.adjusted_fitness = 0

    def add_connection(self, node_1, node_2, gen):
        y = [node_1, node_2, np.random.random(), gen.innovation_number]
        if gen.new_innovation(y):
            y[-1] += 1
            gen.innovation_number += 1

        node_2.incoming.append(y)
        self.connection_genes.append(y)

    def add_node(self, new_node, connection, gen):
        self.connection_genes.remove(connection)
        connection[1].incoming.remove(connection)
        connection_1 = [connection[0], new_node, 1, gen.innovation_number]

        if gen.new_innovation(connection_1):
            connection_1[-1] += 1
            gen.innovation_number += 1

        connection_2 = [new_node, connection[1], connection[2], gen.innovation_number]

        if gen.new_innovation(connection_2):
            connection_2[-1] += 1
            gen.innovation_number += 1

        new_node.incoming.append(connection[0])
        connection[1].incoming.append(new_node)
        self.connection_genes.append(connection_1)
        self.connection_genes.append(connection_2)
        self.hidden_nodes.append(new_node)

    def mutate_weight(self, index):
        self.connection_genes[index][2] = np.random.normal(loc = self.connection_genes[index][2])

    def mutate_activation_function(self):
        functions = [linear, relu, heaviside, sigmoid, gaussian]
        f = np.random.randint(0, len(functions))

        if np.random.random() < (len(self.input_nodes) / (len(self.input_nodes) + len(self.hidden_nodes))):
            i = np.random.randint(0, len(self.input_nodes))
            self.input_nodes[i].activation_function = functions[f]

        else:
            i = np.random.randint(0, len(self.hidden_nodes))
            self.hidden_nodes[i].activation_function = functions[f]
