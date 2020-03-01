import matrix
import math


def sigmoid(x):
    return 1 / (1 + math.exp(-x))

# derivative of sigmmoid function
def dsigmoid(y):
    # return sigmoid(x) * (1 - sigmoid(x))
    # we are using output which was already passed to the sigmoid fuction, so no need to do it again
    return y * (1 - y)

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

        self.learning_rate = 0.1
    

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

    def train(self, input_array, target_array):
        # Generating the hidden outputs
        inputs = matrix.fromArray(input_array)
        hidden = matrix.multiply(self.weights_ih, inputs)
        hidden.add(self.bias_h)
        # activation function
        hidden.map(sigmoid)
        # Generating the output layer's output
        outputs = matrix.multiply(self.weights_ho, hidden)
        outputs.map(sigmoid)


        targets = matrix.fromArray(target_array)

        output_errors = matrix.subtract(targets, outputs)

        # gradient = outputs * (1 - outputs)
        # Calculate gradient
        gradients = matrix.map(outputs, dsigmoid)
        # get hadamard product
        gradients.multiply(output_errors)
        # perform scalar multiplication
        gradients.multiply(self.learning_rate)

        # Calculate deltas
        hidden_t = matrix.transpose(hidden)
        weight_ho_deltas = matrix.multiply(gradients, hidden_t)

        # Change weights by the calculated deltas
        self.weights_ho.add(weight_ho_deltas)
        # Adjust bias by the gradient
        self.bias_o.add(gradients)

        # after output errors are calculated, they are backpropagated to hidden layers for hidden layer error calculation
        weights_ho_t = matrix.transpose(self.weights_ho)
        hidden_errors = matrix.multiply(weights_ho_t, output_errors)

        # Calculate hidden gradient
        hidden_gradient = matrix.map(hidden, dsigmoid)
        # hadamard product
        hidden_gradient.multiply(hidden_errors)
        hidden_gradient.multiply(self.learning_rate)

        # Calculate input->hidden deltas
        inputs_t = matrix.transpose(inputs)
        weight_ih_deltas = matrix.multiply(hidden_gradient, inputs_t)

        self.weights_ih.add(weight_ih_deltas)
        self.bias_h.add(hidden_gradient)