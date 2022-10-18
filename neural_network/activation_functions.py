import numpy as np

def linear(x):
    return x

def relu(x):
    return max(0, x)

def sigmoid(x):
    y = 1 / (1 + np.exp(-x))
    return y

def heaviside(x):
    y = 0
    if x > 0:
            y = 1

    return y

def gaussian(x):
    return np.exp(-(x ** 2))
