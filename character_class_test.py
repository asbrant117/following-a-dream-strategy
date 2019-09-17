import pygame
from pygame import *

import character_animation


class Test(pygame.sprite.Sprite, character_animation.Animation):
    def __init__(self, setting, screen, animation):
        pygame.sprite.Sprite.__init__(self)
        # инициализируем настройки и поверхность
        self.screen = screen
        self.setting = setting
        self.animation = animation

        # данные времени для анимации
        # self.time = setting.time
        # self.work_time = 0
        # self.skip_frame = 0
        # self.frame = 0

        # изображение героя и выделенный прямоугольник
        # self.image = self.anim_test_down
        self.rect = pygame.Rect(self.setting.test_x, self.setting.test_y, self.setting.value[1][1],
                                self.setting.value[1][2])

        # координаты расположения
        self.rect.x = self.setting.test_x
        self.rect.y = self.setting.test_y

        # жизнь персонажа
        self.health = self.setting.value[1][5]
        self.health_colour = self.setting.health_colour_full

        # флажки перемещения
        # флажок направления
        self.direction = 'down'
        self.collision = 'No'

    # Функция помогающая отслеживать перемещение
    def update_test(self, dt):

        if self.direction == 'right' and self.collision != 'right':
            self.rect.x += self.setting.value[1][4]

        if self.direction == 'left' and self.collision != 'left':
            self.rect.x -= self.setting.value[1][4]

        if self.direction == 'up' and self.collision != 'top':
            self.rect.y -= self.setting.value[1][4]

        if self.direction == 'down' and self.collision != 'bottom':
            self.rect.y += self.setting.value[1][4]

        if self.direction == 'right_up' and self.collision != 'right' and self.collision != 'top':
            self.rect.x += self.setting.value[1][4]
            self.rect.y -= self.setting.value[1][4]

        if self.direction == 'left_up' and self.collision != 'left' and self.collision != 'top':
            self.rect.x -= self.setting.value[1][4]
            self.rect.y -= self.setting.value[1][4]

        if self.direction == 'right_down' and self.collision != 'right' and self.collision != 'bottom':
            self.rect.y += self.setting.value[1][4]
            self.rect.x += self.setting.value[1][4]

        if self.direction == 'left_down' and self.collision != 'left' and self.collision != 'bottom':
            self.rect.y += self.setting.value[1][4]
            self.rect.x -= self.setting.value[1][4]

        # время жизни кадра
        self.animation.work_time += dt
        self.animation.skip_frame = self.animation.work_time / self.animation.time
        if self.animation.skip_frame > 0:
            self.animation.work_time = self.animation.work_time % self.animation.work_time
            self.animation.frame += self.animation.skip_frame
            if self.animation.frame >= len(self.image):
                self.animation.frame = 0

    def collide_test(self, chatacters, tiles):
        for chatacter in chatacters:
            if sprite.collide_rect(self, chatacter):
                print(1)
                if self.rect.right >= chatacter.rect.left - self.setting.value[1][
                    3] and self.rect.right <= chatacter.rect.left + self.setting.value[1][
                    3] and self.rect.bottom >= chatacter.rect.top:
                    self.rect.right = chatacter.rect.left
                    # self.collision = 'right'

                if self.rect.left >= chatacter.rect.right - self.setting.value[1][
                    3] and self.rect.left <= chatacter.rect.right + self.setting.value[1][3]:
                    self.rect.left = chatacter.rect.right
                    # self.collision = 'left'

                if self.rect.bottom >= chatacter.rect.top - self.setting.value[1][
                    3] and self.rect.bottom <= chatacter.rect.top + self.setting.value[1][3]:
                    self.rect.bottom = chatacter.rect.top
                # self.collision = 'bottom'

                if self.rect.top >= chatacter.rect.bottom - self.setting.value[1][
                    3] and self.rect.top <= chatacter.rect.bottom + 4:
                    self.rect.top = chatacter.rect.bottom
                    # self.collision = 'bottom'
            else:
                self.collision = 'no'

        for tile in tiles:
            if sprite.collide_rect(self, tile):
                print(1)
                if self.rect.right >= tile.rect.left - self.setting.value[1][
                    3] and self.rect.right <= tile.rect.left + self.setting.value[1][
                    3] and self.rect.bottom >= tile.rect.top:
                    self.rect.right = tile.rect.left
                    # self.collision = 'right'

                if self.rect.left >= tile.rect.right - self.setting.value[1][
                    3] and self.rect.left <= tile.rect.right + self.setting.value[1][3]:
                    self.rect.left = tile.rect.right
                    # self.collision = 'left'

                if self.rect.bottom >= tile.rect.top - self.setting.value[1][
                    3] and self.rect.bottom <= tile.rect.top + self.setting.value[1][3]:
                    self.rect.bottom = tile.rect.top
                # self.collision = 'bottom'

                if self.rect.top >= tile.rect.bottom - self.setting.value[1][
                    3] and self.rect.top <= tile.rect.bottom + 4:
                    self.rect.top = tile.rect.bottom
                    # self.collision = 'bottom'
            else:
                self.collision = 'no'
            #     self.rect.right = chatacter.rect.left
            #     self.collision = 'left'
            #     print('!!!!!!!!!!1')

            # for chatacter in chatacters:
            #     if sprite.collide_rect(self, chatacter):
            #         if self.rect.x + 40 < chatacter.rect.x:
            #             self.collision = 'right'
            #         if self.rect.x > chatacter.rect.x + 40:
            #             self.collision = 'left'
            #         if self.rect.y + 50 < chatacter.rect.y:
            #             self.collision = 'bottom'
            #         if self.rect.y > chatacter.rect.y + 50:  # if self.rect.top < chatacter.rect.bottom
            #             self.collision = 'top'
            #         break
            #     # print(self.collision)

        #     if self.rect.x > chatacter.rect.x:
        #         self.direction = 'stay_down'
        #     if self.rect.y > chatacter.rect.y:
        #         self.direction = 'stay_down'
        #     if self.rect.y < chatacter.rect.y:
        #         self.direction = 'stay_down'

    # оторажение
    def blit_test(self):
        if self.direction == 'right':
            self.image = self.animation.anim_test_3G
        if self.direction == 'left':
            self.image = self.animation.anim_test_7G
        if self.direction == 'up':
            self.image = self.animation.anim_test_1G
        if self.direction == 'down':
            self.image = self.animation.anim_test_5G
        if self.direction == 'left_down':
            self.image = self.animation.anim_test_6G
        if self.direction == 'left_up':
            self.image = self.animation.anim_test_8G
        if self.direction == 'right_down':
            self.image = self.animation.anim_test_4G
        if self.direction == 'right_up':
            self.image = self.animation.anim_test_2G
        if self.direction == 'stay_down':
            self.image = self.animation.anim_footmen_stay_down

        # self.screen.blit(self.image[int(self.animation.frame)], self.rect)
        pygame.draw.rect(self.screen, (0, 0, 255), self.rect)

        #  if self.direction == 'stay_down':
        #      self.image = self.animation_test_stay_down
        #  if self.direction == 'stay_left':
        #      self.image = self.animation_test_stay_left
        #  if self.direction == 'stay_right':
        #      self.image = self.animation_test_stay_right
        # N_colour = self.setting.health_colour_full
        if self.health < 70 and self.health >= 30:
            self.health_colour = self.setting.health_colour_medium
        if self.health < 30:
            self.health_colour = self.setting.health_colour_low

        # отображение жизни юнита
        pygame.draw.rect(self.screen, self.health_colour,
                         (self.rect.x - abs((self.setting.value[1][1] - self.setting.value[1][6])) / 2,
                          (self.rect.y + self.setting.value[1][2] + 10), 100, 8))
        pygame.draw.rect(self.screen, (0, 0, 0),
                         ((self.rect.x - 11), (self.rect.y + self.setting.value[1][2] + 10), 102, 10), 1)
