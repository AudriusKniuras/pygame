import matrix
import math


def sigmoid(x):
    return 1 / (1 + math.exp(-x))

class NeuralNetwork():
    def __init__(self, input_nodes, hidden_nodes, output_nodes):
        self.input_nodes = input_nodes
        self.hidden_nodes = hidden_nodes
        self.output_nodes = output_nodes

        # weights_ih => weights of inputs between input and hidden layer
        self.weights_ih = matrix.Matrix(self.hidden_nodes, self.input_nodes)
        # weights_ho => weights of inputs between hidden and output layer
        self.weights_ho = matrix.Matrix(self.output_nodes, self.hidden_nodes)
        self.weights_ih.randomize()
        self.weights_ho.randomize()

        self.bias_h = matrix.Matrix(self.hidden_nodes, 1)
        self.bias_o = matrix.Matrix(self.output_nodes, 1)
        self.bias_h.randomize()
        self.bias_o.randomize()

    

    def feedforward(self, input_array):

        # Generating the hidden outputs
        inputs = matrix.fromArray(input_array)
        hidden = matrix.multiply(self.weights_ih, inputs)
        hidden.add(self.bias_h)
        # activation function
        hidden.map(sigmoid)

        # Generating the output layer's output
        output = matrix.multiply(self.weights_ho, hidden)
        output.map(sigmoid)

        return output.toArray()