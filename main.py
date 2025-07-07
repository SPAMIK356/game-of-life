import numpy as np
import pygame


def draw_grid(grid: np.ndarray, cell_size: float) -> None:
    ...


FPS = 60
WIDTH = 1280
HEIGHT = 720
CELL_SIZE = 5.0
C_EMPTY = (100,100,100)
C_TAKEN = (0,0,0)

#Pygame setup
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
running = True

a = np.random.randint(0,2, (100,100))

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill('white')

    pygame.display.flip()
    clock.tick(FPS)