import pygame
import time

class Block:
    def __init__(self,x_pos,y_pos,width, screen, speed, mass):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.width = width
        self.screen = screen
        self.speed = speed
        self.mass = mass
        self.rect = pygame.rect.Rect((self.x_pos,self.y_pos,self.width,self.width))
    
    def draw(self):
        pygame.draw.rect(self.screen, (255,255,255), self.rect)
    
    def move(self):
        # print(self.x_pos)
        self.x_pos = self.x_pos - self.speed
        # self.rect.move_ip(-1, 0)
        self.rect = pygame.rect.Rect((self.x_pos,self.y_pos,self.width,self.width))
        
    def collide(self, other):
        return not ( (self.x_pos + self.width < other.x_pos) 
                or self.x_pos > other.x_pos + other.width)

        # if (self.x_pos + self.width == other.x_pos):
        #     print('collide')

    def bounce(self, other):
        sum_mass = self.mass + other.mass
        new_speed = ((self.mass-other.mass)/sum_mass) * self.speed
        new_speed += ((2 * other.mass)/sum_mass) * other.speed

        return new_speed


screen = pygame.display.set_mode((800, 400))

block_big = Block(400,300,100, screen, 10, 200)
block_small = Block(200,360,40,screen, 0, 100)

screen.fill((0,0,0))
block_small.draw()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0,0,0))

    block_big.move()
    block_big.draw()
    block_small.move()
    block_small.draw()
    
    pygame.display.update()

    if (block_small.collide(block_big)):
        v1 = block_big.bounce(block_small)
        v2 = block_small.bounce(block_big)
        print(v1)
        print(v2)
        block_small.speed = int(v2)
        block_big.speed = int(v1)
        print('Collide')

    print(f'v1: {block_small.speed}, v2: {block_big.speed}')

    time.sleep(0.01)

