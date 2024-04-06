def player_motion(obj,speed, s_width):
    obj.x += speed


    if obj.left <= 0:
        obj.left = 0.1
    elif obj.right >= s_width:
        obj.right = s_width + 0.1















