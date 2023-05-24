


def update_monsters_x(monster_list, shift, flag_direction):

    if flag_direction:
        for elem in monster_list:
            elem.rect.x += shift
    else:
        for elem in monster_list:
            elem.rect.x -= shift


def update_monsters_y(monster_list, shift, flag_direction):

    if flag_direction:
        for elem in monster_list:
            elem.rect.y += shift
    else:
        for elem in monster_list:
            elem.rect.y -= shift

