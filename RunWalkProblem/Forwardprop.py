import numpy as np
class MLP:
    def __init__(self,num_imputs=3,num_hidden=[3, 3],num_outputs=2):

        self.num_inputs = num_imputs # create num_inputs atribute
        self.num_hidden = num_hidden # create num_hidden atribute
        self.num_outputs = num_outputs # create num_outputs atribute

        # list that summarizes the number of nodes on each layer
        layers = [self.num_inputs] + self.num_hidden + [self.num_outputs] 
        
        weights = [] #create an empty list
        for i in range(len(layers)-1):
            w = np.random.rand(layers[i],layers[i+1]) # creates random matrices of weights
            self.weights.append(w) #appends those matrices to weights variable
        self.weigths = weights #creates weights atribute  

    def forward_propagate(self, inputs):
        """ 
        Method that calculate the forward propagation
            args:
                inputs (ndarray): input layer values (x1,x2,...,xn)
        """
        activations = inputs
        self.activations[0] = inputs

        for i,w in enumerate(self.weights):
            #calculate multiplication between input ndarray and the corresponding weight matrix
            net_inputs=np.dot(activations, w)

            #applies the activation function over the weighted input (h=xi*Wi)
            activations = self._sigmoid(net_inputs)
            self.activations[i+1] = activations
        return activations

    def _sigmoid(self,x):
        """ Method that implements the sigmoid function
            args:
                x (ndarray): input array (see Neural_network_from_scratch.pdf for further details)
        """
        return 1/(1+np.exp(-x))

if __name__ == "__main__":
    #call the Multi Layer Percerptron (MLP) class
    mlp = MLP()

    #create an input with random values
    inputs = np.random.rand(mlp.num_inputs)

    #execute the forward propagation.
    outputs = mlp.forward_propagate(inputs)

    #print results
    print(f"The network input is: {inputs}")
    print(f"The network output is: {outputs}")