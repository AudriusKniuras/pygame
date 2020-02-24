import pygame

screen_width = 800
screen_height = 400

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Calculating PI with collisions")


# surface, color, Rect(left, top, width, height)
pygame.draw.rect(screen, (255,255,255), (400,300,100,100))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    pygame.display.update()