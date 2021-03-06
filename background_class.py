import os

import pygame

import background_animation_statically



class Terra_Tiles(pygame.sprite.Sprite):
    def __init__(self, setting, screen_save, background_animation, x, y, view):
        pygame.sprite.Sprite.__init__(self)
        self.screen_save = screen_save
        self.setting = setting
        self.background_animation = background_animation

        self.view = view
        if view == 'grass':
            self.width = self.setting.tile_width
            self.length = self.setting.tile_length
            self.image = background_animation.anim_grass

        if view == 'tree':
            self.width = self.setting.tile_width
            self.length = self.setting.tile_length
            self.image = background_animation.anim_tree

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
        self.screen_save.blit(self.image[int(0)], self.rect)
