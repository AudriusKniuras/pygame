# Standard libraries
import random
import pygame

# My libraries
import sys
# Append path to be able to import neural network library
sys.path.append(r'C:\Users\knaud\Desktop\projects\repositories\pygame\neural_network2')
import nn

screen = pygame.display.set_mode((500, 500))
screen.fill((255,255,255))


training_data = [
    {
        "inputs": [0, 0],
        "targets": [0]
    },
    {
        "inputs": [0, 1],
        "targets": [1]
    },
    {
        "inputs": [1, 0],
        "targets": [1]
    },
    {
        "inputs": [1, 1],
        "targets": [0]
    },

]

neural_network = nn.NeuralNetwork(2, 4, 1)

resolution = 10
cols = screen.get_width() // resolution
rows = screen.get_height() // resolution

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    for i in range(100):
        data = random.choice(training_data)
        neural_network.train(data['inputs'], data['targets'])
    color = 10
    for i in range(cols):
        for j in range(rows):
            # color = int(random.random() * 255)
            x1 = i / cols
            x2 = j / rows
            inputs = [x1, x2]
            y = neural_network.predict(inputs)[0]
            # print(y)
            color = int(y*255)
            rgb = (color, color, color)

            rect = pygame.Rect(i*resolution, j*resolution, resolution, resolution)
            pygame.draw.rect(screen, rgb, rect)
    pygame.display.update()

print(neural_network.feedforward([1, 0]))
print(neural_network.feedforward([0, 1]))
print(neural_network.feedforward([0, 0]))
print(neural_network.feedforward([1, 1]))