import math as math
import numpy as np
import matplotlib.pyplot as plt

class Perceptron:
    def __init__(self, inputs, weights):
        self.inputs = inputs
        self.weights = weights 

    def sigmoid(self,x):
        """
        Method that implements the sigmoid function
            args:
                x (array or list): it represents the inputs values weighted and summed (h=x*W)
        """
        return 1/(1+math.exp(-x))

    def ReLU(self,x):
        """
        Method that implements the Rectified Linear Unit function
            args:
                x (array or list): it represents the inputs values weighted and summed (h=x*W)
        """
        return max(0,x)

    def Identity(self,x):
        """
        Method that implements the identity function
            args:
                x (array or list): it represents the inputs values weighted and summed (h=x*W)
        """
        return x

    def BinaryStep(self,x):
        """
        Method that implements the Binary Step function
            args:
                x (array or list): it represents the inputs values weighted and summed (h=x*W)
        """
        if x<0:
            return 0
        else:
            return 1

    def Tanh(self,x):
        """
        Method that implements the Hyperbolic tangent function
            args:
                x (array or list): it represents the inputs values weighted and summed (h=x*W)
        """
        exp = math.exp
        return (exp(x)-exp(-x))/(exp(x)+exp(-x))

    def GELU(self,x):
        """
        Method that implements the Gaussian Error Linear Unit function
            args:
                x (array or list): it represents the inputs values weighted and summed (h=x*W)
        """
        return (0.5*x)*(1+math.erf(x/(2**(0.5))))

    def softplus(self,x):
        """
        Method that implements the Softplus function
            args:
                x (array or list): it represents the inputs values weighted and summed (h=x*W)
        """
        return math.log(1+math.exp(x))

    def ELU(self,x,alpha):
        """
        Method that implements the Exponential Linear Unit function
            args:
                x (array or list): it represents the inputs values weighted and summed (h=x*W)
        """
        if x>0: 
            return x
        else:
            return alpha*(math.exp(x)-1)

    def SELU(self,x):
        """
        Method that implements the Scaled Exponential Linear Unit function
            args:
                x (array or list): it represents the inputs values weighted and summed (h=x*W)
        """
        lambda_  = 1.0507
        alpha = 1.67326
        if x>0:
            return lambda_*x
        else:
            return lambda_*alpha*(math.exp(x)-1)

    def LeakyReLU(self,x):
        """
        Method that implements the Leaky Rectified Linear Unit function
            args:
                x (array or list): it represents the inputs values weighted and summed (h=x*W)
        """
        if x<0:
            return 0.01*x
        else:
            return x

    def PRReLU(self,x,alpha):
        """
        Method that implements the Parametric Rectified Linear Unit function
            args:
                x (array or list): it represents the inputs values weighted and summed (h=x*W)
        """
        if x<0:
            return alpha*x
        else:
            return x

    def SiLU(self,x):
        """
        Method that implements the Sigmoid Linear Unit function
            args:
                x (array or list): it represents the inputs values weighted and summed (h=x*W)
        """
        return x/(1+math.exp(-x))

    def Gaussian(self,x):
        """
        Method that implements the Gaussian function
            args:
                x (array or list): it represents the inputs values weighted and summed (h=x*W)
        """
        return math.exp((-1)*(x**2))

    def activation_function(self,inputs,weights,activation_function,alpha):
        """
        Method that implements the perceptron with its activation function.
            args:
                x (array or list): it represents the inputs values weighted and summed (h=x*W)
                weights (array or list): set of matrices of weights
                activation_function (string): 
        """
        h=0
        for x,w in zip(inputs, weights):
            h += x*w
        function_dic = {
            'sigmoid': self.sigmoid(h),
            'ReLU': self.ReLU(h),
            'Identity': self.Identity(h),
            'BinaryStep': self.BinaryStep(h),
            'Tanh': self.Tanh(h),
            'GELU': self.GELU(h),
            'softplus': self.softplus(h),
            'ELU': self.ELU(h,alpha),
            'SELU': self.SELU(h),
            'LeakyReLU': self.LeakyReLU(h),
            'PRReLU': self.PRReLU(h,alpha),
            'SiLU': self.SiLU(h),
            'Gaussian': self.Gaussian(h),
        }
        return function_dic[activation_function]

if __name__ == "__main__":
    inputs = [0.5,0.2,0.1]
    weights = [0.1,0.2,0.1]

    perceptron = Perceptron(inputs,weights)
    
    outputs = perceptron.activation_function(inputs,weights,'Tanh',alpha=0.5)
    print(f'The inputs are {inputs}')
    print(f'The output is {outputs}')
