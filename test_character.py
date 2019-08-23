import pygame
from pygame import *

import animation


class Test(pygame.sprite.Sprite, animation.Animation):
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
        self.rect = pygame.Rect(self.setting.test_x, self.setting.test_y, 54, 64)

        # координаты расположения
        self.rect.x = self.setting.test_x
        self.rect.y = self.setting.test_y

        # жизнь персонажа
        self.health = self.setting.test_health
        self.health_colour = self.setting.health_colour_full

        # флажки перемещения
        # флажок направления
        self.direction = 'down'
        self.collision = 'No'

    # Функция помогающая отслеживать перемещение
    def update_test(self, dt):

        if self.direction == 'right' and self.collision != 'right':
            self.rect.x += self.setting.test_speed

        if self.direction == 'left' and self.collision != 'left':
            self.rect.x -= self.setting.test_speed

        if self.direction == 'up' and self.collision != 'top':
            self.rect.y -= self.setting.test_speed

        if self.direction == 'down' and self.collision != 'bottom':
            self.rect.y += self.setting.test_speed

        if self.direction == 'right_up' and self.collision != 'right' and self.collision != 'top':
            self.rect.x += self.setting.test_speed_2
            self.rect.y -= self.setting.test_speed_2

        if self.direction == 'left_up' and self.collision != 'left' and self.collision != 'top':
            self.rect.x -= self.setting.test_speed_2
            self.rect.y -= self.setting.test_speed_2

        if self.direction == 'right_down' and self.collision != 'right' and self.collision != 'bottom':
            self.rect.y += self.setting.test_speed_2
            self.rect.x += self.setting.test_speed_2

        if self.direction == 'left_down' and self.collision != 'left' and self.collision != 'bottom':
            self.rect.y += self.setting.test_speed_2
            self.rect.x -= self.setting.test_speed_2

        # время жизни кадра
        self.animation.work_time += dt
        self.animation.skip_frame = self.animation.work_time / self.animation.time
        if self.animation.skip_frame > 0:
            self.animation.work_time = self.animation.work_time % self.animation.work_time
            self.animation.frame += self.animation.skip_frame
            if self.animation.frame >= len(self.image):
                self.animation.frame = 0


    def collide_test(self, chatacters):
        for chatacter in chatacters:
            if sprite.collide_rect(self, chatacter):
                if self.rect.x + 40 < chatacter.rect.x:
                    self.collision = 'right'
                if self.rect.x > chatacter.rect.x + 40:
                    self.collision = 'left'
                if self.rect.y + 50 < chatacter.rect.y:
                    self.collision = 'bottom'
                if self.rect.y > chatacter.rect.y + 50:  # if self.rect.top < chatacter.rect.bottom
                    self.collision = 'top'
                break
            # print(self.collision)
            else:
                self.collision = 'no'

        #     if self.rect.x > chatacter.rect.x:
        #         self.direction = 'stay_down'
        #     if self.rect.y > chatacter.rect.y:
        #         self.direction = 'stay_down'
        #     if self.rect.y < chatacter.rect.y:
        #         self.direction = 'stay_down'

    # оторажение
    def blit_test(self):
        if self.direction == 'right':
            self.image = self.animation.anim_test_right
        if self.direction == 'left':
            self.image = self.animation.anim_test_left
        if self.direction == 'up':
            self.image = self.animation.anim_test_up
        if self.direction == 'down':
            self.image = self.animation.anim_test_down
        if self.direction == 'left_down':
            self.image = self.animation.anim_test_left_down
        if self.direction == 'left_up':
            self.image = self.animation.anim_test_left_up
        if self.direction == 'right_down':
            self.image = self.animation.anim_test_right_down
        if self.direction == 'right_up':
            self.image = self.animation.anim_test_right_up
        if self.direction == 'stay_down':
            self.image = self.animation.anim_footmen_stay_down

        #  if self.direction == 'stay_down':
        #      self.image = self.animation_test_stay_down
        #  if self.direction == 'stay_left':
        #      self.image = self.animation_test_stay_left
        #  if self.direction == 'stay_right':
        #      self.image = self.animation_test_stay_right
        #  if self.direction == 'stay_up':
        #      self.image = self.animation_test_stay_up

        self.screen.blit(self.image[int(self.animation.frame)], self.rect)

        if self.health >= 70:
            self.health_colour = self.setting.health_colour_full
        if self.health < 70 and self.health >= 30:
            self.health_colour = self.setting.health_colour_medium
        if self.health < 30:
            self.health_colour = self.setting.health_colour_low

        # отображение жизни юнита
        pygame.draw.rect(self.screen, self.health_colour, ((self.rect.x - 10), (self.rect.y + 100), 100, 8))
        pygame.draw.rect(self.screen, (0, 0, 0), ((self.rect.x - 11), (self.rect.y + 98), 102, 10), 1)
