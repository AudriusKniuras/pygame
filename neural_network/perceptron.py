import random

def sign(n):
    if n >= 0:
        return 1
    else:
        return -1

    

class Perceptron:
    weights = []
    learning_rate = 0.1

    def __init__(self):
        for i in range(2):
            self.weights.append(round(random.uniform(-1,1), 2))
        # self.weights.append
    
    def guess(self, inputs):
        sum = 0
        for i in range(len(self.weights)):
            sum += inputs[i] * self.weights[i]
        
        output = sign(sum)
        return output
    
    def train(self, inputs, target):
        guess = self.guess(inputs)
        
        # if the guess != target, try to modify the weight
        error = target - guess
        for i, weight in enumerate(self.weights):
            self.weights[i] += error * inputs[i] * self.learning_rate