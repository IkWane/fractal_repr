import pygame as pg
import sys

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
        if event.type == pg.QUIT :
            pg.quit()
            sys.exit()
        if event.type == pg.MOUSEWHEEL :
            if iterations + event.y > 1 :
                iterations += event.y
    
    points = []
    mp = pg.mouse.get_pos()
    pos = complex(mp[0]/center - 1, mp[1]/center -1)
    current = complex(0, 0)
    print(current)

    for i in range(iterations) :
        points.append(((current.real + 1) * center, (current.imag + 1) * center))
        try :
            current = func(current, pos)
        except OverflowError :
            break

    screen.fill((0, 0, 0))

    pg.draw.lines(screen, (255, 255, 255), False, points)

    pg.display.update()
    
