import numpy as np
from species import *

class generation():
    def _init_(self):
        self.innovation_number = 0
        self.species = []
        self.innovations = []
        self.total_members = 0
        self.disjoint_coef = 3
        self.weight_coef = 3
        self.distance_threshold = 5

    def passed_distance_threshold(self, member, s):
        if len(member.connection_genes) < 20:
            N = 1

        else:
            N = max(len(member.connection_genes), len(s.reference_member.connection_genes))

        W = abs(abs(member.total_weight) - abs(s.reference_member.total_weight))
        W /= max(len(member.connection_genes), len(s.reference_member.connection_genes))

        D = abs(len(member.connection_genes) - len(s.reference_member.connection_genes))

        if (self.disjoint_coef * D / N + self.weight_coef * W) > self.distance_threshold:
            return True

        else:
            return False

    def moved_to_new_species(self, member, specie):
        for s in self.species:
            if not self.passed_distance_threshold(member, s):
                s.members.append(member)
                specie.members.remove(member)
                #This kills the function, so we won't
                #have to worry about the "return False"
                return True

        return False

    def create_new_species(self):
        n_s = species()
        n_s._init_()
        for s in self.species:
            n_s.members = s.members.copy()
            n_s.reference_member = s.reference_member
            for i in range(0, len(n_s.members)):
                if self.passed_distance_threshold(n_s.members[i], n_s):
                    if not self.moved_to_new_species(n_s.members[i], n_s):
                        try:
                            s.members.remove(n_s.members[i])
                            new_species = species()
                            new_species._init_()
                            new_species.allowed_members = 15
                            new_species.reference_member = n_s.members[i]
                            new_species.members.append(n_s.members[i])
                            self.species.append(new_species)

                        except ValueError:
                            pass

    def assign_allowed_members(self):
        total_fitness = 0
        for s in self.species:
            total_fitness += s.average_adjusted_fitness

        #TODO: Find a way to do this without the double for loop
        for s in self.species:
            #Might end up being a little higher or lower than
            #total_members, but it's not a huge deal.
            s.allowed_members = int(self.total_members * s.average_adjusted_fitness / total_fitness)

    def new_innovation(self, connection):
        trunacated_connection = [connection[0], connection[1]]
        if trunacated_connection in self.innovations:
            return False

        return True
