import random

def sign(n):
    if n >= 0:
        return 1
    else:
        return -1

class Perceptron:
    weights = []

    def __init__(self):
        for i in range(2):
            self.weights.append(random.uniform(-1,1))
    
    def guess(self, inputs):
        sum = 0
        for i in range(len(self.weights)):
            sum += inputs[i] * self.weights[0]
        
        output = sign(sum)
        return output