import os

import pygame

from background_map_lvl import lvl
from background_class import Terra_Tiles


def background(setting):
    # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    # временно!!!!
    level = lvl()

    screen_save = pygame.display.set_mode((3264, 4512))
    x1 = y1 = 0
    x = y = 0
    tiles = []
    tiles_tree = []
    for row in level:  # строка
        for col in row:  # часть строки
            if col == '-':
                view = 'grass'
                tile = Terra_Tiles(setting, screen_save, x=x, y=y, view=view)
                tiles.append(tile)
            if col == '1':
                view = 'tree'
                tile = Terra_Tiles(setting, screen_save, x=x, y=y, view=view)
                tiles_tree.append(tile)
            x += 32
        y += 32
        x = 0

    for tile in tiles:
        tile.blit()

    for tile in tiles_tree:
        tile.blit()

    pygame.image.save(screen_save, os.path.join('save', 'save.png'))
    return tiles_tree
