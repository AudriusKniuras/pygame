# imported libraries
import pygame
import pygame.gfxdraw

# my libraries
import perceptron
import training
import other_stuff




# TODO:
# implement bias
#



p = perceptron.Perceptron(3)
points = []

screen = pygame.display.set_mode((500, 500))
screen.fill((255,255,255))
for i in range(100):
    points.append(training.Point(screen))
    points[i].show()

# pygame.draw.line(screen, (0,0,0), (0,screen.get_height()), (screen.get_width(), 0))
p1 = training.Point(screen, -1, other_stuff.line_function(-1))
p2 = training.Point(screen, 1, other_stuff.line_function(1))
pygame.draw.line(screen, (0,0,0), (p1.pixelX(),p1.pixelY()), (p2.pixelX(),p2.pixelY()))


running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255,255,255))
    for point in points:
        color = (255, 0, 0)
        inputs = [point.x, point.y, point.bias]
        target = point.label
        guess = p.guess(inputs)
        if guess == target:
            color = (0, 255, 0)
        point.show(color)
    pygame.display.update()
    
    p1 = training.Point(screen, -1, other_stuff.line_function(-1))
    p2 = training.Point(screen, 1, other_stuff.line_function(1))
    pygame.draw.line(screen, (0,0,0), (p1.pixelX(),p1.pixelY()), (p2.pixelX(),p2.pixelY()))

    for point in points:
        

        inputs = [point.x, point.y, point.bias]
        target = point.label

        # target is the known answer
        p.train(inputs, target)

        color = (255, 0, 0)
        guess = p.guess(inputs)
        if guess == target:
            color = (0, 255, 0)
        point.show(color)

        # get new points for the line, to see where the line is now
        p1 = training.Point(screen, -1, p.guessY(-1))
        p2 = training.Point(screen, 1, p.guessY(1))

        pygame.draw.line(screen, (0,0,0), (p1.pixelX(),p1.pixelY()), (p2.pixelX(),p2.pixelY()))
        pygame.time.wait(3)
        pygame.display.update()

    pygame.display.update()

    
