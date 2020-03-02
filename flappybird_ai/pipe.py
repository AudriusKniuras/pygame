import random
import pygame

class Pipe():
    def __init__(self, screen):
        self.screen = screen
        self.width = screen.get_width()
        self.height = screen.get_height()
        self.top = int(random.random() * self.height / 2)
        self.bottom = int(random.random() * self.height / 2)
        if (self.bottom + self.top) > (self.height - 100):
            self.bottom -= 50
            self.top -= 50

        self.pipe_width = 15
        self.speed = 3
        # starts at the edge of the screen
        self.x = self.width

        self.color = (0,255,0)
    
    def show(self):
        rect1 = (self.x, 0, self.pipe_width, self.top)
        pygame.draw.rect(self.screen, self.color, rect1)
        rect2 = (self.x, self.height-self.bottom, self.pipe_width, self.bottom)
        pygame.draw.rect(self.screen, self.color, rect2)

    def update(self):
        self.x -= self.speed

    def offscreen(self):
        if self.x <= -self.pipe_width:
            return True
        else:
            return False
    
    def hit(self, bird):
        if (bird.y < self.top) or (bird.y > self.height - self.bottom):
            if (bird.x > self.x) and (bird.x < self.x + self.pipe_width):
                self.color = (255,0,0)
                return True
        return False
