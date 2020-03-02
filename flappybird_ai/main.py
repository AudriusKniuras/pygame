import pygame
import bird, pipe, ga


screen = pygame.display.set_mode((600, 600))
screen.fill((0,0,0))

POPULATION = 150
birds = []
saved_birds = []
for i in range(POPULATION):
    birds.append(bird.Bird(screen))

pipes = []
pipes.append(pipe.Pipe(screen))


running = True
clock = pygame.time.Clock()
thousands_ticks = 1000
while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # if event.type == pygame.KEYDOWN:
        #     if event.key == pygame.K_SPACE:
        #         bird.up()


    screen.fill((0,0,0))

    for p in reversed(pipes):
        p.show()
        p.update()
        
        for b in birds:
            if p.hit(b):
                saved_birds.append(b)
                birds.remove(b)



    if len(birds) == 0:
        birds = ga.nextGeneration(screen, birds, POPULATION, saved_birds)
        saved_birds = []

        
    for bird in birds:
        bird.think(pipes)
        bird.update()
        bird.show()
        

    ticks = pygame.time.get_ticks()
    if ticks > thousands_ticks:
        pipes.append(pipe.Pipe(screen))
        thousands_ticks += 1000
    pygame.display.update()

    for p in pipes:
        if p.offscreen():
            pipes.remove(p)

    clock.tick(60)

    