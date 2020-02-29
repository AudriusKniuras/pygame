import random
import pygame
import pygame.gfxdraw

import other_stuff

class Point:
    def __init__(self, screen, x=None, y=None):
        self.screen = screen
        self.bias = 1

        # self.x = random.randint(0, screen.get_width())
        # self.y = random.randint(0, screen.get_height())
        if x is None and y is None:
            self.x = round(random.uniform(-1, 1), 3)
            self.y = round(random.uniform(-1, 1), 3)
        else:
            self.x = x
            self.y = y

        
        lineY = other_stuff.line_function(self.x)

        if self.y > lineY:
            self.label = 1
        else:
            self.label = -1
    
    def pixelX(self):
        transformed_x = other_stuff.affine_transformation(self.x, -1, 1, 0, self.screen.get_width())
        return transformed_x

    def pixelY(self):
        transformed_y = other_stuff.affine_transformation(self.y, -1, 1, self.screen.get_height(), 0)
        return transformed_y

    def show(self, color = (0,0,0)):
        if self.label == 1:
            # pygame.gfxdraw.aacircle(self.screen, self.x, self.y, 4, (0,0,0))
            pygame.gfxdraw.aacircle(self.screen, self.pixelX(), self.pixelY(), 4, color)
            # pygame.draw.circle(self.screen, color, (self.pixelX(), self.pixelY()), 5, 1)

        elif self.label == -1:
            # pygame.gfxdraw.aacircle(self.screen, self.x, self.y, 4, (0,0,0))
            # pygame.gfxdraw.filled_circle(self.screen, self.x, self.y, 4, (0,0,0))
            pygame.gfxdraw.aacircle(self.screen, self.pixelX(), self.pixelY(), 4, (0,0,0))
            pygame.gfxdraw.filled_circle(self.screen, self.pixelX(), self.pixelY(), 4, color)

