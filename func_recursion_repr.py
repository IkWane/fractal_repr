import pygame as pg
import sys
from math import sqrt

def func(z, c) :
    return z**2 + c

size = 500
win_size = (size, size)
pg.init()
screen = pg.display.set_mode(win_size)
center = size/2
fractal_scale = size/4
iterations = 10
clock = pg.time.Clock()
square_check = False
check_distance = 5

while 1 :
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

    screen.fill((0, 0, 0))
    pg.display.set_caption(f"fps: {clock.get_fps():.2f} {iterations}") 
    for y in range(size) :
        for x in range(size) :
            pos = complex((x - center)/fractal_scale, (y - center)/fractal_scale)
            current = complex(0, 0)

            for i in range(iterations) :
                try :
                    current = func(current, pos)
                except OverflowError :
                    break
                if square_check :
                    if current.real > check_distance or current.imag > check_distance :
                        break
                else :
                    if sqrt(current.real**2 + current.imag**2) > check_distance :
                        break
            c = (1 - i / iterations) * 255
            screen.set_at((x, y), (c, c, c))
    pg.display.update()
    
