import os

import pygame

from map_lvl import lvl
from background_tiles_beck import Terra_Tiles


def background(setting):
    # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    # временно!!!!
    level = lvl()

    screen_save = pygame.display.set_mode((3264, 4512))
    x1 = y1 = 0
    x = y = 0
    tiles = []
    for row in level:  # строка
        for col in row:  # часть строки
            if col == '-':
                tile = Terra_Tiles(setting, screen_save, x=x, y=y, view='grass')
                tiles.append(tile)
            x += 32
        y += 32
        x = 0

    for tile in tiles:
        tile.blit()

    pygame.image.save(screen_save, os.path.join('save', 'save.png'))
