import pygame
import os
import animation

ANIMATION_Grass = [(0, 429, 32, 32)]
ICON_DIR = os.path.dirname(__file__)  # Полный путь к каталогу с файлами
pichter = pygame.image.load('%s/picter/TerraTiles.png' % ICON_DIR)


class Terra_Tiles(pygame.sprite.Sprite):
    def __init__(self, setting, screen_save, x, y, view):
        pygame.sprite.Sprite.__init__(self)
        self.screen_save = screen_save
        self.setting = setting

        # данные времени для анимации
        self.time = setting.time
        self.work_time = 0
        self.skip_frame = 0
        self.frame = 0

        self.image = pichter.subsurface((0, 429, 32, 32))


        self.view = view
        if view == 'grass':
            self.width = self.setting.tile_width
            self.length = self.setting.tile_length

        # параметры прямоугольника персонажа
        self.rect = pygame.Rect(x, y, self.width, self.length)

        self.rect.x = x
        self.rect.y = y



    # def update(self, dt):
    #     # время жизни кадра
    #     self.work_time += dt
    #     self.skip_frame = self.work_time / self.time
    #     if self.skip_frame > 0:
    #         self.work_time = self.work_time % self.work_time
    #         self.frame += self.skip_frame
    #         if self.frame >= len(self.image):
    #             self.frame = 0

    def blit(self):



        self.screen_save.blit(self.image, self.rect)
