import pygame
import random

# Constants
WIDTH, HEIGHT = 600, 400
GRID_SIZE = 20
BLACK, WHITE, GREEN, RED = (0, 0, 0), (255, 255, 255), (0, 255, 0), (255, 0, 0)

class Snake:
    def __init__(self):
        self.body = [(WIDTH // 2, HEIGHT // 2)]
        self.direction = (GRID_SIZE, 0)
        self.grow = False
    
    def move(self):
        head_x, head_y = self.body[0]
        new_head = (head_x + self.direction[0], head_y + self.direction[1])
        
        if not self.grow:
            self.body.pop()
        self.grow = False
        
        self.body.insert(0, new_head)
    
    def chance_direction():
    
    def snake_grow():
    
    def check_collsion(self):


class food(self):


def main():


if __name__ == "__main__":
    main()
