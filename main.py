import numpy as np
import pygame
from pygame.font import Font
from numpy.typing import NDArray

def draw_grid(grid: NDArray, sim_surface: pygame.surface, width, height) -> pygame.Surface:
    '''Generate a surface with grid and scales it to width and height'''
    pygame.surfarray.blit_array(sim_surface,grid)
    scaled_surface = pygame.transform.scale(sim_surface, (width, height))
    return scaled_surface

def render_fps_counter(screen: pygame.surface, color: tuple, font:Font, fps:float) -> None:
    '''Function for rendering fps counter in the top left corner of screen'''
    counter = font.render(str(int(fps)),False, color)
    screen.blit(counter,(0,0))
    

def get_neighbours(grid: NDArray) -> NDArray:
    '''Returns a numpy 2D array of neighbours amount for each cell'''
    neigbours = np.zeros(shape=grid.shape)
    
    for x in range(-1,2):
        for y in range(-1,2):
            if x == 0 and y == 0:
                continue
            neigbours += np.roll(grid, (x,y),(0,1))
    return neigbours

def calculate_next_state(grid: NDArray) -> NDArray:
    '''Calculates the next state of cellular automata. Returns a 2D numpy array with the state'''
    neigbours = get_neighbours(grid)

    empty = grid == 0
    taken = grid == 1
    
    buffer = grid.copy()

    buffer[(neigbours<2) & taken] = 0
    buffer[(neigbours > 3) & taken] = 0
    buffer[(neigbours == 3) & empty] = 1
    return(buffer)

#Parametrs of window
FPS = 60
WIDTH = 800
HEIGHT = 800
TITLE = 'Game of life'

#Grid parametrs
GRID_WIDTH = 1000
GRID_HEIGHT = 1000
EMPTY_CELL_COLOR = (0,0,0)
OCCUPIED_CELL_COLOR = (255,255,255)

#Pygame initialization
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(TITLE)
clock = pygame.time.Clock()
running = True

#FPS counter parametrs
fps_counter_font = pygame.font.SysFont("Arial",32)
fps_counter_color = (255,0,0)

#Initialization of grid, simulation surface and colors array
cell_colors = np.array([EMPTY_CELL_COLOR,OCCUPIED_CELL_COLOR])
grid = np.random.randint(0,2, (GRID_WIDTH,GRID_HEIGHT))
sim_surface = pygame.Surface(grid.shape)

#Main loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #Creates a 2D array which contains colors of each cell
    colors = cell_colors[grid]

    #Renders grid on screen
    screen.blit(draw_grid(colors,sim_surface,WIDTH,HEIGHT), (0,0))

    #Renders FPS counter
    render_fps_counter(screen,fps_counter_color,fps_counter_font,clock.get_fps())

    pygame.display.flip()

    #Applying new state for grid
    grid = calculate_next_state(grid)

    clock.tick(FPS)