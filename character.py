import pygame

import animation


class Character(pygame.sprite.Sprite, animation.Animation):
    def __init__(self, setting, screen, view, comand, health, x, y, camera_x,camera_y):
        pygame.sprite.Sprite.__init__(self)
        animation.Animation.__init__(self)
        # инициализирует героя и поверхность
        self.screen = screen
        self.setting = setting

        # данные времени для анимации
        self.time = setting.time
        self.work_time = 0
        self.skip_frame = 0
        self.frame = 0

        # изображение героя и выделенный прямоугольник
        self.image = self.anim_test_down  #
        self.rect = pygame.Rect(x, y, 54, 64)

        # координаты расположения
        self.rect.x = x + camera_x
        self.rect.y = y + camera_y
        # self.x = x
        # self.y = y

        # флажок направления
        self.direction = 'down'

        # информация о юните
        # вид юнита
        self.view = view
        # команда
        self.comand = comand
        # жизнь персонажа
        self.health = health
        self.health_colour = self.setting.health_colour_full

    # Функция помогающая отслеживать перемещение
    def update_character(self, dt):
        # if self.direction == 'right':
        #     self.rect.x += self.setting.test_speed

        # время жизни кадра
        self.work_time += dt
        self.skip_frame = self.work_time / self.time
        if self.skip_frame > 0:
            self.work_time = self.work_time % self.work_time
            self.frame += self.skip_frame
            if self.frame >= len(self.image):
                self.frame = 0

    # оторажение
    def blit_character(self):
        if self.view == 'footmen':
            if self.direction == 'right':
                self.image = self.anim_footmen_right
            if self.direction == 'left':
                self.image = self.anim_footmen_left
            if self.direction == 'up':
                self.image = self.anim_footmen_up
            if self.direction == 'down':
                self.image = self.anim_footmen_down
            if self.direction == 'left_down':
                self.image = self.anim_footmen_left_down
            if self.direction == 'left_up':
                self.image = self.anim_footmen_left_up
            if self.direction == 'right_down':
                self.image = self.anim_footmen_right_down
            if self.direction == 'right_up':
                self.image = self.anim_footmen_right_up

            #  if self.direction == 'stay_down':
            #      self.image = self.animation_test_stay_down
            #  if self.direction == 'stay_left':
            #      self.image = self.animation_test_stay_left
            #  if self.direction == 'stay_right':
            #      self.image = self.animation_test_stay_right
            #  if self.direction == 'stay_up':
            #      self.image = self.animation_test_stay_up

            self.screen.blit(self.image[int(self.frame)], self.rect)

            if self.health >= 70:
                self.health_colour = self.setting.health_colour_full
            if self.health < 70 and self.health >= 30:
                self.health_colour = self.setting.health_colour_medium
            if self.health < 30:
                self.health_colour = self.setting.health_colour_low

            # отображение жизни юнита
            pygame.draw.rect(self.screen, self.health_colour, ((self.rect.x - 10), (self.rect.y + 100), 100, 8))
            pygame.draw.rect(self.screen, (0, 0, 0), ((self.rect.x - 11), (self.rect.y + 98), 102, 10), 1)
