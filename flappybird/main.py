import pygame
import bird, pipe


screen = pygame.display.set_mode((600, 600))
screen.fill((0,0,0))

bird = bird.Bird(screen)
pipes = []
pipes.append(pipe.Pipe(screen))


running = True
clock = pygame.time.Clock()
thousands_ticks = 1000
while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird.up()


    screen.fill((0,0,0))

    for p in pipes:
        p.show()
        p.update()
        
        p.hit(bird)

        
        


    bird.show()
    bird.update()

    ticks = pygame.time.get_ticks()
    if ticks > thousands_ticks:
        pipes.append(pipe.Pipe(screen))
        thousands_ticks += 1000
    pygame.display.update()

    for p in pipes:
        if p.offscreen():
            pipes.remove(p)

    clock.tick(60)

    