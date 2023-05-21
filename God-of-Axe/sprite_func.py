import config as cfg


def updateMonsters_x(monster_list, shift, flag_direction):
    if flag_direction:
        for elem in monster_list:
            elem.rect.x += shift
    else:
        for elem in monster_list:
            elem.rect.x -= shift


def updateMonsters_y(monster_list, shift, flag_direction):
    if flag_direction:
        for elem in monster_list:
            elem.rect.y += shift
    else:
        for elem in monster_list:
            elem.rect.y -= shift
