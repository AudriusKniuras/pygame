import pygame
import random



def count_neighbors(grid, x, y):
    count = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            if grid[i][j] == 1:
                count += 1
    count -= grid[x][y]
    return count

screen = pygame.display.set_mode((800, 800))
resolution = 10
rows = screen.get_height() // resolution
cols = screen.get_width() // resolution

grid = []

for i in range(cols):
    grid.append([])
    for j in range(rows):
        if random.random() < 0.9:
            grid[i].append(0)
        else:
            grid[i].append(1)

grid_copy = grid.copy()
        

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    for i in range(cols):
        for j in range(rows):
            if grid[i][j] == 0:
                pygame.draw.rect(screen, (255,255,255), (j*resolution, i*resolution, resolution-1, resolution-1))
            else:
                pygame.draw.rect(screen, (0,0,0), (j*resolution, i*resolution, resolution-1, resolution-1))

    # for i in range(cols):
    #     for j inrange(rows):


    pygame.display.update()