import random as r



def player_motion(obj, speed, s_width):
    obj.x += speed


    if obj.left <= 0:
        obj.left = 0.1
    elif obj.right >= s_width:
        obj.right = s_width + 0.1


def opponent_motion(obj, sp, s_width, s_height, pl,):
    obj.y += sp
    if obj.bottom > s_height:
        obj.x = r.randint(40, s_width - 40)
        obj.y = -50
        return 'miss'
    elif obj.colliderect(pl):
        obj.x = r.randint(40, s_width - 40)
        obj.y = -50
        return 'catch'











