import pygame

class Bird():
    def __init__(self, screen):
        self.screen = screen
        self.height = screen.get_height()
        self.width = screen.get_width()

        self.y = int(self.height/2)
        self.x = 25

        self.gravity = 0.2
        self.velocity = 0
        self.lift = -5
    
    def show(self):
        pygame.draw.circle(self.screen, (255,255,255), (int(self.x), int(self.y)), 16)

    def update(self):
        self.velocity += self.gravity
        self.y += self.velocity
        # add some air resistance
        self.velocity *+ 0.9


        if self.y > self.height:
            self.y = self.height
            self.velocity = 0
        if self.y < 0:
            self.y = 0
            self.velocity = 0

    def up(self):
        if self.velocity > 0:
            self.velocity = 0
        self.velocity += self.lift