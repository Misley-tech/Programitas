import numpy as np
class MLP:
    def __init__(self,num_imputs,num_hidden,num_outputs,weights):
        self.num_inputs = num_imputs # num_inputs atribute is created 
        self.num_hidden = num_hidden # num_hidden atribute is created
        self.num_outputs = num_outputs # num_outputs atribute is created
        self.weights = weights # weights atribute is created

    def forward_propagate(self, inputs):
        """ 
        Method that implements the forward propagation 
        """
        activations = inputs
        for w in self.weights:
            net_inputs=np.dot(activations, w) #applies the dot product between weights and inputs  
            activations = self.sigmoid(net_inputs) #applies the activation function
        return activations

    def sigmoid(self,x):
        """
        Method that implements sigmoid function 
        """
        return 1/(1+np.exp(-x))

if __name__ == "__main__":
    #The Multi Layer Perceptron (MLP) parameters are provided
    num_imputs=3
    num_hidden=[3, 5]
    num_outputs=2
    weights = [[[0.2, 0.1, 0.9],
                [0.5, 0.1, 0.9],
                [0.1, 0.5, 0.6]],
               [[0.5, 0.1, 0.8, 0.6, 0.6],
                [0.9, 0.1, 0.9, 0.3, 0.8],
                [0.4, 0.9, 0.4, 0.8, 0.2]],
               [[0.9, 0.5],
                [0.4, 0.1],
                [0.1, 0.1],
                [0.7, 0.5],
                [0.8, 0.7]]]

    mlp = MLP(num_imputs,num_hidden,num_outputs,weights)
    inputs = [0.3,0.7,0.5]
    outputs = mlp.forward_propagate(inputs) #excute the forward propagation

    #imprimo los resultados
    print(f"The network input is: {inputs}")
    print(f"The network output is: {outputs}")
