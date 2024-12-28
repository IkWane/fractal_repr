import pygame as pg
import sys
from math import sqrt

def func(z, c) :
    return z**2 + c

size = 800
win_size = (size, size)
pg.init()
screen = pg.display.set_mode(win_size)
center = size/2
iterations = 10

while 1 :
    for event in pg.event.get() :
        if (
            event.type == pg.QUIT or 
            (event.type == pg.KEYDOWN and 
             event.key == pg.K_ESCAPE)
             ) :
            pg.quit()
            sys.exit()
        if event.type == pg.MOUSEWHEEL :
            if iterations + event.y > 1 :
                iterations += event.y
    
    points = []
    mp = pg.mouse.get_pos()
    pos = complex(mp[0]/center - 1, mp[1]/center -1)
    current = complex(0, 0)

    for i in range(iterations) :
        points.append(((current.real + 1) * center, (current.imag + 1) * center))
        try :
            current = func(current, pos)
        except OverflowError :
            break
        if sqrt(current.real**2 + current.imag**2) > 10 :
            break

    screen.fill((0, 0, 0))
    c = i / iterations * 255
    pg.draw.lines(screen, (c, c, c), False, points)

    pg.display.update()
    
