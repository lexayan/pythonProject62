import sys
import pygame as pg
import random as r
import game_logic as gl
pg.init()

#Config Variables
W = 1280
H = 720
FPS = 60
clock = pg.time.Clock()
speed = 10
object_speed = speed
player_speed = 0



#COLORS
GRAY = (79, 74, 71)
RED = (219, 20, 20)
BROWN = (150, 86, 41)


#GAME OBJECTS
player = pg.Rect(0, H-30, 100, 20)
player.centerx = W//2
apple = pg.Rect(r.randint(40, W - 40), -50, 40, 40)




screen = pg.display.set_mode((W, H))
pg.display.set_caption('Catch an apple')




game_over = False

while not game_over:
    clock.tick(FPS)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
    screen.fill(GRAY)
    pg.draw.rect(screen, BROWN, player)
    pg.draw.ellipse(screen, RED, apple)


    pg.display.update()

    apple.y += 5
    if apple.bottom > H:
        apple.x = r.randint(40, W-40)
        apple.y = -50

    keys = pg.key.get_pressed()
    if keys[pg.K_LEFT]:
        player_speed = -speed
    elif keys[pg.K_RIGHT]:
        player_speed = speed
    else:
        player_speed = 0
    gl.player_motion(player, player_speed, W)

