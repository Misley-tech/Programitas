import numpy as np
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
            self.weights.append(w)
        self.weigths = weights

    def forward_propagate(self, inputs):
        """ 
        Metodo que calcula la forward propagation 
        """
        activations = inputs
        self.activations[0] = inputs

        for i,w in enumerate(self.weights):
            #calculate net inputs
            net_inputs=np.dot(activations, w)

            #calculate the activations
            activations = self._sigmoid(net_inputs)
            self.activations[i+1] = activations

        return activations

    def _sigmoid(self,x):
        return 1/(1+np.exp(-x))

if __name__ == "__main__":
    #creo el Multi Layer Perceptron (MLP) y defino la forma que tiene la red neural
    mlp = MLP()

    #creo los inputs
    inputs = np.random.rand(mlp.num_inputs)

    #ejecuto la forward propagation
    outputs = mlp.forward_propagate(inputs)

    #imprimo los resultados
    print(f"The network input is: {inputs}")
    print(f"The network output is: {outputs}")