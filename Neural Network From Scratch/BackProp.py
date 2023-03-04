import numpy as np
from random import random
#save activation and derivatives Done
#implement backpropagation
#implement gradient descent
#implement train 
#train our net with some dummy dataset
#make some predictions

class MLP:
    def __init__(self,num_imputs=3,num_hidden=[3, 3],num_outputs=2):

        self.num_inputs = num_imputs # creo el atributo num_inputs 
        self.num_hidden = num_hidden # creo el atributo num_hidden
        self.num_outputs = num_outputs # creo el atributo num_outputs

        layers = [self.num_inputs] + self.num_hidden + [self.num_outputs]
        
        #create random weights
        weights = [] #creo una lista vacia
        for i in range(len(layers)-1):
            w = np.random.rand(layers[i],layers[i+1])
            weights.append(w)
        self.weigths = weights

        activations = []
        for i in range(len(layers)):
            a = np.zeros(layers[i])
            activations.append(a)
        self.activations = activations

        derivatives = []
        for i in range(len(layers)-1):
            d = np.zeros((layers[i],layers[i+1]))
            derivatives.append(d)
        self.derivatives = derivatives

    def forward_propagate(self, inputs):
        """ 
        Metodo que calcula la forward propagation 
        """
        activations = inputs
        self.activations[0] = inputs

        for i,w in enumerate(self.weigths):
            #calculate net inputs
            net_inputs=np.dot(activations, w)

            #calculate the activations
            activations = self._sigmoid(net_inputs)
            self.activations[i+1] = activations

        return activations

    def back_propagate(self,error,verbose=False):
        """
        dE/dW_i = (y-a_[i+1]) s'(h_[i+1]) a_i
        s'(h_[i+1]) = s(h_[i+1])(1-s(h_[i+1]))
        s(h_[i+1]) = a_[i+1]

        dE/dW_[i-1] = (y-a_[i+1]) s'(h_[i+1]) W_i s'(h_i) a_[i-1]
        """
        for i in reversed(range(len(self.derivatives))):
            activations = self.activations[i+1]
            delta = error * self._sigmoid_derivative(activations) #ndarray([0.1,0.2])-->ndarray([[0.1, 0.2]])
            delta_reshaped = delta.reshape(delta.shape[0], -1).T
            current_activations = self.activations[i] #ndarray([0.1, 0.2]) --> ndarray([[0.1, 0.2]])
            current_activations_reshaped = current_activations.reshape(current_activations.shape[0], -1)
            self.derivatives[i] = np.dot(current_activations_reshaped,delta_reshaped)
            error = np.dot(delta,self.weigths[i].T)
        if verbose:
            print(f'Derivatives for W{i} = {self.derivatives[i]}')
        return error
    
    def gradient_descent(self, learning_rate):
        for i in range(len(self.weigths)):
            weights = self.weigths[i]
            derivatives = self.derivatives[i]
            weights += derivatives*learning_rate
    def train(self,inputs,targets, epochs, learning_rate):
        for i in range(epochs):
            sum_error = 0
            for input,target in zip(inputs, targets):
                output = self.forward_propagate(input)
                error = target-output
                self.back_propagate(error)
                self.gradient_descent(learning_rate)

                sum_error += self._mse(target,output)
            #report error
            print(f'Error: {sum_error/len(inputs)} at epoch {i}')

    def _mse(self, target, output):
        return np.average((target-output)**2)

    def _sigmoid_derivative(self,x):
        return x*(1.0-x)

    def _sigmoid(self,x):
        return 1.0/(1+np.exp(-x))

if __name__ == "__main__":
    #create MLP
    mlp = MLP(2,[5],1)

    inputs = np.array([[random() / 2 for _ in range(2)] for _ in range(1000)]) #array([[0.1,0.2],[0.3,0.4]])
    targets = np.array([[i[0]+i[1]] for i in inputs]) #array([[0.3],[0.7]])

    mlp.train(inputs, targets, 50, 0.1)

    #create dummy data
    input = np.array([0.1,0.2])
    target = np.array([0.3])
