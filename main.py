import numpy as np
import pygame
from pygame import Rect

def draw_grid(grid: np.ndarray, cell_size: float, colors: np.ndarray, surface: pygame.surface) -> None:
    x_max = grid.shape[0]
    y_max = grid.shape[1]

    for y in range(y_max):
        for x in range(x_max):
            pygame.draw.rect(surface,colors[x,y], Rect(x*cell_size,y*cell_size, cell_size,cell_size)) 


def get_neighbours(grid: np.array) -> np.array:
    neigbours = np.zeros(shape=grid.shape)
    
    for x in range(-1,2):
        for y in range(-1,2):
            if x == 0 and y == 0:
                continue
            neigbours += np.roll(grid, (x,y),(0,1))
    return neigbours
            

FPS = 1
WIDTH = 1280
HEIGHT = 720
CELL_SIZE = 50.0
cell_colors = np.array([(250,0,0),(0,250,0)])

#Pygame setup
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
running = True

grid = np.random.randint(0,2, (3,3))

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill('white')

    colors = cell_colors[grid]

    draw_grid(grid,CELL_SIZE,colors,screen)

    pygame.display.flip()

    neigbours = get_neighbours(grid)

    empty = grid == 0
    taken = grid == 1
    
    grid[(neigbours<2) & taken] = 0
    grid[(neigbours > 3) & taken] = 0
    grid[np.logical_or(neigbours == 2, neigbours == 3) &  taken] = 1
    grid[(neigbours == 3) & empty] = 1

    clock.tick(FPS)