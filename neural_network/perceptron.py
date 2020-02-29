import random

def sign(n):
    if n >= 0:
        return 1
    else:
        return -1

    

class Perceptron:
    weights = []
    learning_rate = 0.005

    def __init__(self, weights_length):
        # length-1, because the last weight is a bias, not random
        for i in range(weights_length-1):
            self.weights.append(round(random.uniform(-1,1), 2))
        # append bias - 1
        self.weights.append(1)
    
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

    def guessY(self, x):
        # line formula => mx+b
        # m - line slope, b - Y axis interception
        # m = self.weights[0] / self.weights[1]
        # b = self.weights[2]
        # return m*x+b
        w0 = self.weights[0]
        w1 = self.weights[1]
        w2 = self.weights[2]

        return round(-(w2/w1) - (w0/w1) * x, 2)

        