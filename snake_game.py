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
    
    def change_direction(self, new_direction):
        opposite = (-self.direction[0], -self.direction[1])
        if new_direction != opposite:
            self.direction = new_direction

    
    def grow_snake(self):
        self.grow = True
    
    def check_collision(self):
        head_x, head_y = self.body[0]
        if head_x < 0 or head_x >= WIDTH or head_y < 0 or head_y >= HEIGHT:
            return True
        if len(self.body) > 1 and (head_x, head_y) in self.body[1:]:
            return True
        return False


class Food:
    def __init__(self):
        self.position = self.random_position()

    def random_position(self):
         return (random.randint(0, (WIDTH - GRID_SIZE) // GRID_SIZE) * GRID_SIZE,random.randint(0, (HEIGHT - GRID_SIZE) // GRID_SIZE) * GRID_SIZE)

    def spawn_new(self):
        self.position = self.random_position()

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    snake = Snake()
    food = Food()
    running = True
    
    while running:
        screen.fill(BLACK)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    snake.change_direction((0, -GRID_SIZE))
                elif event.key == pygame.K_DOWN:
                    snake.change_direction((0, GRID_SIZE))
                elif event.key == pygame.K_LEFT:
                    snake.change_direction((-GRID_SIZE, 0))
                elif event.key == pygame.K_RIGHT:
                    snake.change_direction((GRID_SIZE, 0))
        
        snake.move()
        
        if snake.body[0] == food.position:
            snake.grow_snake()
            food.spawn_new()
        
        if snake.check_collision():
            running = False
        
        pygame.draw.rect(screen, RED, (*food.position, GRID_SIZE, GRID_SIZE))
        for segment in snake.body:
            pygame.draw.rect(screen, GREEN, (*segment, GRID_SIZE, GRID_SIZE))
        
        pygame.display.flip()
        clock.tick(10)
    
    pygame.quit()

if __name__ == "__main__":
    main()
