import sys
import pygame as pg

pg.init()

#Config Variables
W = 1280
H = 720
FPS = 60
clock = pg.time.Clock()


screen = pg.display.set_mode((W, H))
pg.display.set_caption('Catch an apple')

game_over = False

while not game_over:
    clock.tick(FPS)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()



