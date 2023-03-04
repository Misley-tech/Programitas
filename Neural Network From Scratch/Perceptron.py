import math as math
import numpy as np
import matplotlib.pyplot as plt

def sigmoid(x):
    y = 1/(1+math.exp(-x))
    return y

def ReLU(x):
    return max(0,x)

def Identity(x):
    return x

def BinaryStep(x):
    if x<0:
        return 0
    else:
        return 1

def Tanh(x):
    exp = math.exp
    return (exp(x)-exp(-x))/(exp(x)+exp(-x))

def GELU(x):
    erf = (0.5*x)*(1+math.erf(x/(2**(0.5))))
    return erf

def softplus(x):
    return math.log(1+math.exp(x))

def ELU(x,alpha):
    if x>0: 
        return x
    else:
        return alpha*(math.exp(x)-1)

def SELU(x):
    lambda_  = 1.0507
    alpha = 1.67326
    if x>0:
        return lambda_*x
    else:
        return lambda_*alpha*(math.exp(x)-1)

def LeakyReLU(x):
    if x<0:
        return 0.01*x
    else:
        return x

def PRReLU(x,alpha):
    if x<0:
        return alpha*x
    else:
        return x

def SiLU(x):
    return x/(1+math.exp(-x))

def Gaussian(x):
    return math.exp((-1)*(x**2))

inputs = [0.5,0.2,0.1]
weights = [0.1,0.2,0.1]

def activation_function(inputs,weights):
    h = 0
    for x,w in zip(inputs, weights):
        h += x*w
    return GELU(h)

print(activation_function(inputs,weights))