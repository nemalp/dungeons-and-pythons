def check_position(hero, direction, map_):

    if direction == 'up':
        if hero.location[0] - 1 != -1:
            return True
        else:
            return False
    elif direction == 'down':
        if hero.location[0] + 1 > len(map_):
            return False
        else:
            return True
    elif direction == 'left':
        if hero.location[1] - 1 != -1:
            return True
        else:
            return False
    elif direction == 'right':
        if hero.location[1] > len(map_[0]):
            return False
        else:
            return True
