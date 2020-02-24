import pygame
import random
import math

pygame.init()

screen_width = 400
screen_height = 400


screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Approximate PI")

radius = 200
circle_color = (255,255,255)


rect = screen.get_rect()


#screen.blit(screen, (screen_width - screen.get_width()//2, screen_height - screen.get_height() // 2))
circle = pygame.draw.circle(screen,circle_color,(200,200),radius, 2)

total = 0
circle = 0

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    pygame.display.update()

    # for i in range(1,1000):
    x = random.randrange(0, screen_width)
    y = random.randrange(0, screen_height)

    distance = pygame.Vector2(rect.center).distance_to(pygame.Vector2((x,y)))

    if (distance < radius):
        circle += 1
        screen.set_at((x,y), (0,0,255))
    else:
        screen.set_at((x,y), (255,0,255))
    total += 1

    pi = 4*circle / total
    print(pi)
    