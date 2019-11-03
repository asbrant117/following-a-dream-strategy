import pygame
from pygame import *
from collide import collide_test

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
        self.direction = 'no'
        self.direction_stay = 'down'
        self.collision = 'No'
        self.action = 'no'

    # Функция помогающая отслеживать перемещение
    def update_test(self, dt):

        if self.direction == 'right' and self.collision != 'right':
            self.rect.x += self.setting.value[1][3]

        if self.direction == 'left' and self.collision != 'left':
            self.rect.x -= self.setting.value[1][3]

        if self.direction == 'up' and self.collision != 'top':
            self.rect.y -= self.setting.value[1][3]

        if self.direction == 'down' and self.collision != 'bottom':
            self.rect.y += self.setting.value[1][3]

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

    def collide(self, chatacters, tiles):
        collide_test(self, chatacters)
        collide_test(self, tiles)

    # оторажение
    def blit_test(self):
        # анимация передвижения
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

        # анимация стоя
        if self.direction == 'no' and self.action == 'no':
            if self.direction_stay == 'right':
                self.image = self.animation.anim_test_3S
            if self.direction_stay == 'left':
                self.image = self.animation.anim_test_7S
            if self.direction_stay == 'up':
                self.image = self.animation.anim_test_1S
            if self.direction_stay == 'down':
                self.image = self.animation.anim_test_5S
            if self.direction_stay == 'left_down':
                self.image = self.animation.anim_test_6S
            if self.direction_stay == 'left_up':
                self.image = self.animation.anim_test_8S
            if self.direction_stay == 'right_down':
                self.image = self.animation.anim_test_4S
            if self.direction_stay == 'right_up':
                self.image = self.animation.anim_test_2S

        if self.action == 'yes':
            self.image = self.animation.anim_test_5A

        pygame.draw.rect(self.screen, (0, 0, 255), self.rect)
        self.screen.blit(self.image[int(self.animation.frame)], self.rect)

        if self.health < 70 and self.health >= 30:
            self.health_colour = self.setting.health_colour_medium
        if self.health < 30:
            self.health_colour = self.setting.health_colour_low

        # отображение жизни юнита
        pygame.draw.rect(self.screen, self.health_colour,
                         (self.rect.x - abs((self.setting.value[1][1] - self.setting.value[1][6])) / 2,
                          (self.rect.y + self.setting.value[1][2] + 10), 100, 8))
        # pygame.draw.rect(self.screen, (0, 0, 0),
        #                  ((self.rect.x - 11), (self.rect.y + self.setting.value[1][2] + 10), 102, 10), 1)
