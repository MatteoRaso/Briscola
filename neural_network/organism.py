#A class for neural networks, which will
#be evolved by using the NEAT algorithm.
import numpy as np
import string
import random
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
        self.mother = ""
        self.father = ""
        self.name = ""
        self.hand = []
        self.excess_genes = 0
        self.total_weight = 0
        self.add_node_chance = 0.05
        self.add_connection_chance = 0.05
        self.mutate_weight_chance = 0.05
        self.mutate_activation_chance = 0.05
        self.fitness = 0
        self.adjusted_fitness = 0

    def add_name(self):
         self.name = ''.join(random.choices(string.ascii_letters, k = 52))

    def add_connection(self, node_1, node_2, gen):
        y = [node_1, node_2, np.random.random(), gen.innovation_number]
        if gen.new_innovation(y):
            y[-1] += 1
            gen.innovation_number += 1
            gen.innovations.append([y[0], y[1]])

        self.total_weight += y[2]
        node_2.incoming.append(y)
        self.connection_genes.append(y)

    def add_node(self, new_node, connection, gen):
        self.connection_genes.remove(connection)
        connection[1].incoming.remove(connection)
        connection_1 = [connection[0], new_node, 1, gen.innovation_number]
        self.total_weight += 1

        if gen.new_innovation(connection_1):
            connection_1[-1] += 1
            gen.innovation_number += 1
            gen.innovations.append([connection_1[0], connection_1[1]])

        connection_2 = [new_node, connection[1], connection[2], gen.innovation_number]

        if gen.new_innovation(connection_2):
            connection_2[-1] += 1
            gen.innovation_number += 1
            gen.innovations.append([connection_2[0], connection_2[1]])

        new_node.incoming.append(connection_1)
        connection[1].incoming.append(connection_2)
        self.connection_genes.append(connection_1)
        self.connection_genes.append(connection_2)
        self.hidden_nodes.append(new_node)

    def mutate_weight(self, index):
        self.total_weight -= self.connection_genes[index][2]
        self.connection_genes[index][2] = np.random.normal(loc = self.connection_genes[index][2])
        self.total_weight += self.connection_genes[index][2]

    def mutate_activation_function(self):
        functions = [linear, relu, heaviside, sigmoid, gaussian]
        f = np.random.randint(0, len(functions))

        if np.random.random() < (len(self.input_nodes) / (len(self.input_nodes) + len(self.hidden_nodes))):
            i = np.random.randint(0, len(self.input_nodes))
            self.input_nodes[i].activation_function = functions[f]

        else:
            i = np.random.randint(0, len(self.hidden_nodes))
            self.hidden_nodes[i].activation_function = functions[f]

    def get_total_weight(self):
        for gene in self.connection_genes:
            self.total_weight += gene[2]

    def clear_nodes(self):
        for i in range(0, len(self.hidden_nodes)):
            self.hidden_nodes[i].value = 0

        for i in range(0, len(self.output_nodes)):
            self.output_nodes[i].value = 0
