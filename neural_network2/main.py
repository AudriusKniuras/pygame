import matrix
import nn

import random


training_data = [
    {
        "inputs": [0, 1],
        "targets": [1]
    },
    {
        "inputs": [1, 0],
        "targets": [1]
    },
    {
        "inputs": [0, 0],
        "targets": [0]
    },
    {
        "inputs": [1, 1],
        "targets": [0]
    },

]

neural_network = nn.NeuralNetwork(2, 2, 1)

for i in range(50000):
    data = random.choice(training_data)
    neural_network.train(data["inputs"], data["targets"])


print(neural_network.feedforward([1, 0]))
print(neural_network.feedforward([0, 1]))
print(neural_network.feedforward([0, 0]))
print(neural_network.feedforward([1, 1]))
