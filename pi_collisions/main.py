import pygame
import time

class Block:
    def __init__(self,x_pos,y_pos,width, screen, speed):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.width = width
        self.screen = screen
        self.speed = speed
        self.mass = 1
        self.rect = pygame.rect.Rect((self.x_pos,self.y_pos,self.width,self.width))
    
    def draw(self):
        pygame.draw.rect(self.screen, (255,255,255), self.rect)
    
    def move(self):
        print(self.x_pos)
        self.x_pos = self.x_pos - self.speed
        self.rect.move_ip(-1, 0)
        
    def collide(self, other):
        return not ( (self.x_pos + self.width < other.x_pos) 
                or self.x_pos > other.x_pos + other.width)

        # if (self.x_pos + self.width == other.x_pos):
        #     print('collide')

    def bounce(self, other):
        sum_mass = this.mass + other.mass
        new_speed = ((this.mass-other.mass)/sum_mass) * this.speed
        new_speed += ((2 * other.mass)/sum_mass) * other.speed
        
        return new_speed


screen = pygame.display.set_mode((800, 400))

block_big = Block(400,300,100, screen, 1)
block_small = Block(200,360,40,screen,0)

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
    block_small.draw()
    pygame.display.update()

    if block_small.collide(block_big):
        print("Collide")

    time.sleep(0.05)

