import os

import pygame

from background_map_lvl import lvl
from background_class import Terra_Tiles


def background_physical(setting, background_animation, screen):
    level = lvl()
    x = y = 0
    tiles = []
    for row in level:  # строка
        for col in row:  # часть строки
            if col == '1':
                view = 'tree'
                tile = Terra_Tiles(setting, screen, background_animation, x=x, y=y, view=view)
                tiles.append(tile)
            x += 32
        y += 32
        x = 0

    return tiles
