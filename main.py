import pygame as pg
import pygame.draw

width = 500
heigh = 500

pg.init()
win = pg.display.set_mode((width, heigh))

centr_x = width // 2
centr_y = heigh // 2
x = centr_x
y = centr_y
color = 'yellow'
delay = 1
while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x -= delay
    elif keys[pygame.K_RIGHT]:
        x += delay
    elif keys[pygame.K_UP]:
        y -= delay
    elif keys[pygame.K_DOWN]:
        y += delay
    else:
        x = centr_x
        y = centr_y

    win.fill((255, 255, 255))
    if x >= centr_x + 150 or y >= centr_y + 150 or x <= centr_x - 150 or y <= centr_y - 150:
        color = 'red'
        delay = 0.5
    else:
        color = 'yellow'
        delay = 1

    pygame.draw.circle(win, color, (x, y), 50)

    pygame.display.update()
    pygame.time.delay(10)