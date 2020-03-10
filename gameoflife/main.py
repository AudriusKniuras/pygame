import pygame
import random



def count_neighbors(grid, x, y):
    count = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            try:
                if grid[x+i][y+j] == 1:
                    count += 1
            # if cell is at the grid range, pick a random value for it's neighbors
            # with 20% chance that it's a live neighbor
            except IndexError:
                if random.random() >= 0.8:
                    count += 1
    count -= grid[x][y]
    return count

screen = pygame.display.set_mode((800, 800))
resolution = 8
rows = screen.get_height() // resolution
cols = screen.get_width() // resolution

grid = []

for i in range(cols):
    grid.append([])
    for j in range(rows):
        if random.random() < 0.95:
            grid[i].append(0)
        else:
            grid[i].append(1)

grid_copy = grid.copy()
        
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    

    for i in range(cols):
        for j in range(rows):
            neighbor_count = count_neighbors(grid_copy, i, j)
            if grid[i][j] == 1:
                if neighbor_count > 3 or neighbor_count < 2:
                    grid[i][j] = 0
            elif grid[i][j] == 0:
                if neighbor_count == 3:
                    grid[i][j] = 1

    grid_copy = grid.copy()

    for i in range(cols):
        for j in range(rows):
            if grid[i][j] == 0:
                pygame.draw.rect(screen, (255,255,255), (j*resolution, i*resolution, resolution-1, resolution-1))
            else:
                pygame.draw.rect(screen, (0,0,0), (j*resolution, i*resolution, resolution-1, resolution-1))

    # for i in range(cols):
    #     for j inrange(rows):

    clock.tick(10)
    pygame.display.update()