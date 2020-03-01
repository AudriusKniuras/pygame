import matrix
import nn


neural_network = nn.NeuralNetwork(2, 2, 1)
input = [1, 0]

# m = matrix.fromArray(input)


output = neural_network.feedforward(input)
print(output)