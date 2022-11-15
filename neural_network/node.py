import numpy as np
from activation_functions import linear
class node():
    def _init_(self):
        self.ID = 0
        self.value_1 = 0
        self.value_2 = 0
        self.incoming = []
        self.activation_function = linear

    def get_value_1(self):
        if len(self.incoming) == 0 or self.value_1 != 0:
            return self.value_1

        else:
            for gene in self.incoming:
                self.value_1 += gene[0].activation_function(gene[2] * gene[0].get_value_1())

            return self.value_1

    def get_value_2(self):
        if len(self.incoming) == 0 or self.value_2 != 0:
            return self.value_2

        else:
            for gene in self.incoming:
                self.value_2 += gene[0].activation_function(gene[2] * gene[0].get_value_2())

            return self.value_2
