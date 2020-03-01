import matrix
import nn


neural_network = nn.NeuralNetwork(2, 2, 2)
inputs = [1, 0]
targets = [1, 1]

neural_network.train(inputs, targets)

# m = matrix.fromArray(input)


# output = neural_network.feedforward(input)
# print(output)