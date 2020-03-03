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



# initiate fonts for displaying scores
current_score = 0
max_score = 0
pygame.font.init()
myfont = pygame.font.SysFont('calibri', 20)
score_surface = myfont.render(f'Score: {current_score}', False, (255,255,255))
max_score_surface = myfont.render(f'Max Score: {max_score}', False, (255,255,255))

# create buttons
plus_button = pygame.image.load('plus.png').convert_alpha()
minus_button = pygame.image.load('minus.png').convert_alpha()
plus_b = screen.blit(plus_button, (screen.get_width() - 140, 20))
minus_b = screen.blit(minus_button, (screen.get_width() - 140, 40))



counter = 0
cycles = 1
running = True
clock = pygame.time.Clock()
thousands_ticks = 1000
while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            pos = pygame.mouse.get_pos()
            if plus_b.collidepoint(pos):
                cycles += 1
            elif minus_b.collidepoint(pos):
                cycles -= 1
        # if event.type == pygame.KEYDOWN:
        #     if event.key == pygame.K_SPACE:
        #         bird.up()


    for cycle in range(cycles):
                

        if counter % 60 == 0:
            pipes.append(pipe.Pipe(screen))
        counter += 1

        for p in reversed(pipes):
            p.update()
            
            for b in birds:
                if p.hit(b):
                    saved_birds.append(b)
                    birds.remove(b)
        if len(birds) == 0:
            birds = ga.nextGeneration(screen, birds, POPULATION, saved_birds)
            saved_birds = []
            pipes = []
            current_score = 0
            counter = 0
            score_surface = myfont.render(f'Score: {current_score}', True, (255,255,255))
            pipes.append(pipe.Pipe(screen))

        for bird in birds:
            bird.think(pipes)
            bird.update()


        for p in pipes:
            if p.offscreen():
                pipes.remove(p)
                current_score += 1
                if current_score >= max_score:
                    max_score = current_score
            
    

    screen.fill((0,0,0))

    score_surface = myfont.render(f'Score: {current_score}', True, (255,255,255))
    max_score_surface = myfont.render(f'Max Score: {max_score}', True, (255,255,255))
    screen.blit(score_surface, (screen.get_width() - 120, 20))
    screen.blit(max_score_surface, (screen.get_width() - 120, 40))

    # create buttons
    plus_b = screen.blit(plus_button, (screen.get_width() - 140, 20))
    minus_b = screen.blit(minus_button, (screen.get_width() - 140, 40))
    

    for b in birds:
        b.show()
    for p in pipes:
        p.show()
    pygame.display.update()

    

    clock.tick(60)

    