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



p = perceptron.Perceptron()
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


inputs = [-1, 0.5]
guess = p.guess(inputs)
print(guess)

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    for point in points:
        inputs = [point.x, point.y]
        target = point.label

        # target is the known answer
        p.train(inputs, target)

        color = (255, 0, 0)
        guess = p.guess(inputs)
        if guess == target:
            color = (0, 255, 0)
        
        
        # pygame.gfxdraw.filled_circle(screen, point.x, point.y, 4, color)
        pygame.gfxdraw.filled_circle(screen, point.pixelX(), point.pixelY(), 4, color)
        
        # pygame.time.wait(3)
        pygame.display.update()


    pygame.display.update()
