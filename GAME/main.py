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

score, miss = 0, 0
pg.font.init()
score_font = pg.font.SysFont('Arial', 32)

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
    if miss >= 3:
        game_over = True


    clock.tick(FPS)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
    screen.fill(GRAY)
    pg.draw.rect(screen, BROWN, player)
    pg.draw.ellipse(screen, RED, apple)

    score_text = score_font.render(f'Score: {score}', True, (107, 237, 185))
    miss_text = score_font.render(f'Miss: {miss}', True, (107, 237, 185))
    pg.display.update()


    apple_catch = gl.opponent_motion(apple, object_speed, W, H, player)

    keys = pg.key.get_pressed()
    if keys[pg.K_LEFT]:
        player_speed = -speed
    elif keys[pg.K_RIGHT]:
        player_speed = speed
    else:
        player_speed = 0
    gl.player_motion(player, player_speed, W)


