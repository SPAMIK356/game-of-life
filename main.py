import numpy as np
import pygame
from pygame import Rect

def draw_grid(grid: np.ndarray, cell_size: float, colors: np.ndarray, surface: pygame.surface) -> None:
    x_max = grid.shape[0]
    y_max = grid.shape[1]

    for x in range(x_max):
        for y in range(y_max):
            pygame.draw.rect(surface,colors[x,y], Rect(x*cell_size,y*cell_size, cell_size,cell_size)) 


def get_neighbours(grid: np.array) -> np.array:
    neigbours = np.zeros(shape=grid.shape)
    transformations = np.array([-1,0,1])
    for x in transformations:
        for y in transformations:
            if x == 0 and y == 0:
                continue
            neigbours += np.roll(grid, (x,y),(0,1))
    return neigbours
            

FPS = 60
WIDTH = 1280
HEIGHT = 720
CELL_SIZE = 5.0
cell_colors = np.array([(200,200,200),(0,0,0)])

#Pygame setup
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
running = True


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill('white')

    a = np.random.randint(0,2, (100,100))
    colors = cell_colors[a]
    draw_grid(a,CELL_SIZE,colors,screen)

    pygame.display.flip()
    clock.tick(FPS)