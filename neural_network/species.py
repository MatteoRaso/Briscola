from organism import *

class species():
    def _init_(self):
        self.average_adjusted_fitness = 0
        self.members = []
        self.reference_member = None
        self.allowed_members = 0

    def purge(self):
        excess = len(self.members) - self.allowed_members
        if excess > 0:
            self.members = self.members[:-excess]

        #Even when we have an acceptable number of
        #members, we still need to purge the weak.
        self.members = self.members[:-10]

    def get_adjusted_fitness(self):
        for member in self.members:
            member.adjusted_fitness = member.fitness / (len(self.members) - 1)


    def get_average_adjusted_fitness(self):
        for member in self.members:
            self.average_adjusted_fitness += member.adjusted_fitness

        self.average_adjusted_fitness /= len(self.members)

    def sort_by_adjusted_fitness(self):
        self.members.sort(key = lambda x: x.adjusted_fitness, reverse = True)

    def breed(self, member_1, member_2, generation):
        child = organism()
        child._init_()
        child.add_name()
        child.mother = member_1.name
        child.father = member_2.name
        #Matching genes should have the same innovation number.
        member_1.connection_genes.sort(key = lambda x: x[-1])
        member_2.connection_genes.sort(key = lambda x: x[-1])

        for i in range(0, min(len(member_1.connection_genes), len(member_2.connection_genes))):
            if member_1.connection_genes[i][-1] == member_2.connection_genes[i][-1]:
                if np.random.random() < 0.5:
                    child.connection_genes.append(member_1.connection_genes[i])

                else:
                    child.connection_genes.append(member_2.connection_genes[i])

            else:
                break

        #Excess/disjoint genes can only come from the fitter parent.
        if len(member_1.connection_genes) > len(member_2.connection_genes) and member_1.fitness > member_2.fitness:
            for i in range(0, len(member_1.connection_genes) - len(member_2.connection_genes)):
                if np.random.random() < 0.5:
                    child.connection_genes.append(member_1.connection_genes[i])

        elif len(member_2.connection_genes) > len(member_1.connection_genes) and member_2.fitness > member_1.fitness:
            for i in range(0, len(member_2.connection_genes) - len(member_1.connection_genes)):
                if np.random.random() < 0.5:
                    child.connection_genes.append(member_2.connection_genes[i])

        if np.random.random() < child.add_node_chance:
            new_node = node()
            new_node._init_()
            connection = child.connection_genes[np.random.randint(0, len(child.connection_genes))]
            child.add_node(new_node, connection, generation)

        if np.random.random() < child.add_connection_chance:
            potential_node_1 = np.append(child.input_nodes, np.append(child.hidden_nodes, child.output_nodes))
            #We don't want to connect from a node to an input node.
            potential_node_2 = np.append(child.hidden_nodes, child.output_nodes)

            node_1 = potential_node_1[np.random.randint(0, len(potential_node_1))]
            node_2 = potential_node_2[np.random.randint(0, len(potential_node_2))]

            child.add_connection(node_1, node_2, generation)

        if np.random.random() < child.mutate_weight_chance:
            index = np.random.randint(0, len(child.connection_genes))
            child.mutate_weight(index)

        if np.random.random() < child.mutate_activation_chance:
            child.mutate_activation_function()

        self.members.append(child)
