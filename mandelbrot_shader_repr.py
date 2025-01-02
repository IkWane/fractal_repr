import pygame as pg
import pygame_shaders as pgs
import sys
from math import sqrt, exp

def func(z, c) :
    return z**2 + c

size = 800
win_size = (size, size)
pg.init()
screen = pg.display.set_mode(win_size, pg.OPENGL | pg.DOUBLEBUF | pg.HWSURFACE)
display = pg.Surface(win_size)
display.set_colorkey((0, 0, 0))
center = size/2
fractal_scale = 4
iterations = 10
clock = pg.time.Clock()
square_check = False
check_distance = 5
inputs = [0, 0, 0]
constant = (0,0)
offset = (0, 0)
prev_mp = (0, 0)

zoom = 0

shader = pgs.Shader(
    win_size, win_size, 
    (0, 0), 
    "shaders/vertex.glsl", 
    "shaders/fragment.glsl",
    display
    )

while 1 :
    clock.tick()
    mp = pg.mouse.get_pos()
    for event in pg.event.get() :
        if (
            event.type == pg.QUIT or 
            (event.type == pg.KEYDOWN and 
             event.key == pg.K_ESCAPE)
             ) :
            pg.quit()
            sys.exit()
        elif event.type == pg.KEYDOWN :
            if event.key == pg.K_k :
                square_check = False if square_check else True
            elif event.key == pg.K_LCTRL :
                inputs[0] = True
            elif event.key == pg.K_LSHIFT :
                inputs[2] = True
        elif event.type == pg.KEYUP :
            if event.key == pg.K_LCTRL :
                inputs[0] = False
            elif event.key == pg.K_LSHIFT :
                inputs[2] = False
        elif event.type == pg.MOUSEBUTTONDOWN :
            if event.button == 1 :
                inputs[1] = True
        elif event.type == pg.MOUSEBUTTONUP :
            if event.button == 1 :
                inputs[1] = False
        elif event.type == pg.MOUSEWHEEL :
            if inputs[2] :
                if iterations + event.y > 1 :
                    iterations += event.y
            else :
                zoom += event.y
                zoom = max(0, zoom)
                fractal_scale = 4 * exp(-0.5 * zoom)
    
    pgs.clear((0, 0, 0))
    delta = (mp[0] - prev_mp[0], mp[1] - prev_mp[1])
    if inputs[1] :
        offset = ((offset[0] - delta[0] / size * fractal_scale), (offset[1] + delta[1] / size * fractal_scale))
    shader.send("iterations", [iterations])
    shader.send("checkDistance", [check_distance])
    shader.send("constant", [(constant[0] / size - 0.5) * 4, (constant[1] / size - 0.5) * 4])
    shader.send("offset", [offset[0], offset[1]])
    shader.send("fractalScale", [fractal_scale])
    display.fill((0, 0, 0))
    pg.display.set_caption(f"fps: {clock.get_fps():.2f} {iterations} {fractal_scale}") 
    shader.render(display)
    if inputs[0] :
        constant = mp
        pg.draw.line(screen, (1.0, 1.0, 1.0, 1.0), (size/2,size/2), mp)
    prev_mp = mp
    pg.display.flip()