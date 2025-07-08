import numpy as np
import pygame
from pygame.font import Font

def draw_grid(grid: np.ndarray, sim_surface: pygame.surface, width, height) -> pygame.Surface:
    pygame.surfarray.blit_array(sim_surface,np.transpose(grid))
    scaled_surface = pygame.transform.scale(sim_surface, (width, height))
    return scaled_surface

def render_fps_counter(screen: pygame.surface, color: tuple, font:Font, fps:float) -> None:

    counter = font.render(str(int(fps)),False, color)
    screen.blit(counter,(0,0))
    

def get_neighbours(grid: np.array) -> np.array:
    neigbours = np.zeros(shape=grid.shape)
    
    for x in range(-1,2):
        for y in range(-1,2):
            if x == 0 and y == 0:
                continue
            neigbours += np.roll(grid, (x,y),(0,1))
    return neigbours

def calculate_next_state(grid: np.array):
    ...

FPS = 60
WIDTH = 800
HEIGHT = 800
CELL_SIZE = 100.0
cell_colors = np.array([(0,0,0),(255,255,255)])

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
running = True

fps_counter_font = pygame.font.SysFont("Arial",32)
fps_counter_color = (255,0,0)

grid = np.random.randint(0,2, (100,100))
sim_surface = pygame.Surface(grid.shape)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill('white')

    colors = cell_colors[grid]

    pygame.Surface.blit(screen,draw_grid(np.transpose(colors),sim_surface,WIDTH,HEIGHT), (0,0))
    render_fps_counter(screen,fps_counter_color,fps_counter_font,clock.get_fps())
    pygame.display.flip()

    neigbours = get_neighbours(grid)

    empty = grid == 0
    taken = grid == 1
    
    buffer = grid.copy()

    buffer[(neigbours<2) & taken] = 0
    buffer[(neigbours > 3) & taken] = 0
    buffer[np.logical_or(neigbours == 2, neigbours == 3) &  taken] = 1
    buffer[(neigbours == 3) & empty] = 1

    grid = buffer

    

    clock.tick(FPS)