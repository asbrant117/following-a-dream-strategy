import pygame
from pygame import *
import os

import character_animation

ICON_DIR = os.path.dirname(__file__)  # Полный путь к каталогу с файлами




class Beckground_full(pygame.sprite.Sprite):
    def __init__(self, setting, screen):
        picture = pygame.image.load('%s/save/save.png' % ICON_DIR)
        pygame.sprite.Sprite.__init__(self)
        # инициализируем настройки и поверхность
        self.screen = screen
        self.setting = setting

        self.rect = pygame.Rect(0, 0, 3500, 3500)
        self.image = picture

        self.rect.x = 0
        self.rect.y = 0

    def blit_background_full(self):
        self.screen.blit(self.image, self.rect)
