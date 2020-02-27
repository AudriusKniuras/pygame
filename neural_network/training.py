import random

class Point:
    def __init__(self):
        x = random.randint(width)
        y = random.randint(height)

        if x > y:
            label = 1
        else:
            label = -1