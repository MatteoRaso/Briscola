import numpy as np
from activation_functions import linear
class node():
    def _init_(self):
        self.ID = 0
        self.value = 0
        self.incoming = []
        self.activation_function = linear

    def get_value(self):
        if len(self.incoming) == 0 or self.value != 0:
            return self.value

        else:
            for gene in self.incoming:
                self.value += gene[0].activation_function(gene[2] * gene[0].get_value())

            return self.value
