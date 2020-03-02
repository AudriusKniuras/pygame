import pygame
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
    
    def show(self):
        pygame.draw.circle(self.screen, (255,255,255), (int(self.x), int(self.y)), 16)


    def think(self):

        inputs = [1.0, 0.5, 0.2, 0.3]
        output = self.brain.predict(inputs)

        if output[0] > 0.5:
            self.up()

    def update(self):
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