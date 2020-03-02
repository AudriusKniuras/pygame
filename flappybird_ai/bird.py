import pygame
import math
import sys
# Append path to be able to import neural network library
sys.path.append(r'C:\Users\audrius.kniuras\OneDrive - R1\Python\pygame\neural_network2')
import nn

class Bird():
    def __init__(self, screen):
        self.screen = screen
        self.height = screen.get_height()
        self.width = screen.get_width()

        self.y = int(self.height/2)
        self.x = 25

        self.gravity = 0.2
        self.velocity = 0
        self.lift = -5

        # AI stuff
        # inputs - 4 (y of bird; x of pipe's left edge, y of bottom pipe, y of top pipe)
        # hidden layer - 4 (random), output - 1 (number between 0 and 1; more than 0.5 => jump)
        self.brain = nn.NeuralNetwork(4,4,1)
        self.score = 0
        # probability to be picked in the next generation
        self.fitness = 0
    
    def show(self):
        pygame.draw.circle(self.screen, (255,255,255), (int(self.x), int(self.y)), 16)


    def think(self, pipes):

        # Find the closest pipe
        closest_pipe = None
        closest_distance = math.inf
        for pipe in pipes:
            d = pipe.x - self.x
            if d < closest_distance and d > 0:
                closest_distance = d
                closest_pipe = pipe

        inputs = []
        inputs.append(self.y / self.height)
        inputs.append(closest_pipe.top / self.height)
        inputs.append(closest_pipe.bottom / self.height)
        inputs.append(closest_pipe.x / self.width)

        output = self.brain.predict(inputs)
        print(output)

        if output[0] > 0.5:
            self.up()

    def update(self):
        # AI stuff
        self.score += 1


        # Speed and other calculations
        self.velocity += self.gravity
        self.y += self.velocity
        # add some air resistance
        self.velocity *+ 0.9


        if self.y > self.height:
            self.y = self.height
            self.velocity = 0
        if self.y < 0:
            self.y = 0
            self.velocity = 0

    def up(self):
        if self.velocity > 0:
            self.velocity = 0
        self.velocity += self.lift
    # TODO mutations and other stuff
    def mutate(self):
