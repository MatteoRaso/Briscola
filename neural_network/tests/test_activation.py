from node import *
from activation_functions import *

N = node()
N._init_()
N.activation_function = linear

assert N.activation_function(-3) == -3

N.activation_function = relu

assert N.activation_function(-3) == 0
assert  N.activation_function(3) == 3

N.activation_function = sigmoid

assert N.activation_function(0) == 0.5
assert (1 - N.activation_function(100)) < 1e-6
assert N.activation_function(-100) < 1e-6

N.activation_function = heaviside

assert N.activation_function(-3) == 0
assert N.activation_function(3) == 1

N.activation_function = gaussian

assert N.activation_function(0) == 1
assert N.activation_function(10) < 1e-3
assert N.activation_function(10) == N.activation_function(-10)
