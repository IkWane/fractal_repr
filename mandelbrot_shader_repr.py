import pygame as pg
import pygame_shaders as pgs
import sys
from math import sqrt

def func(z, c) :
    return z**2 + c

size = 800
win_size = (size, size)
pg.init()
screen = pg.display.set_mode(win_size, pg.OPENGL | pg.DOUBLEBUF | pg.HWSURFACE)
display = pg.Surface(win_size)
display.set_colorkey((0, 0, 0))
center = size/2
fractal_scale = 2
iterations = 10
clock = pg.time.Clock()
square_check = False
check_distance = 5

shader = pgs.Shader(
    win_size, win_size, 
    (0, 0), 
    "shaders/vertex.glsl", 
    "shaders/fragment.glsl",
    display
    )

while 1 :
    clock.tick()
    for event in pg.event.get() :
        if (
            event.type == pg.QUIT or 
            (event.type == pg.KEYDOWN and 
             event.key == pg.K_ESCAPE)
             ) :
            pg.quit()
            sys.exit()
        elif event.type == pg.MOUSEWHEEL :
            if iterations + event.y > 1 :
                iterations += event.y
        elif event.type == pg.KEYDOWN :
            if event.key == pg.K_k :
                square_check = False if square_check else True
    
    mp = pg.mouse.get_pos()
    shader.send("iterations", [iterations])
    shader.send("checkDistance", [check_distance])
    pgs.clear((0, 0, 0))
    display.fill((0, 0, 0))
    pg.display.set_caption(f"fps: {clock.get_fps():.2f} {iterations}") 
    shader.render(display)
    pg.display.flip()