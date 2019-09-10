import pygame

import character_animation


class Character(pygame.sprite.Sprite):
    def __init__(self, setting, screen, animation, view, command, x, y, camera_x, camera_y):
        pygame.sprite.Sprite.__init__(self)
        # инициализирует героя и поверхность
        self.screen = screen
        self.setting = setting
        self.animation = animation


        # изображение героя и выделенный прямоугольник
        self.rect = pygame.Rect(x, y, self.setting.value[2][1], self.setting.value[2][2])

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
        self.command = command
        # жизнь персонажа
        self.health = self.setting.value[2][5]
        self.health_colour = self.setting.health_colour_full

    # Функция помогающая отслеживать перемещение
    def update_character(self, dt):
        # if self.direction == 'right':
        #     self.rect.x += self.setting.test_speed

        # время жизни кадра
        self.animation.work_time += dt
        self.animation.skip_frame = self.animation.work_time / self.animation.time
        if self.animation.skip_frame > 0:
            self.animation.work_time = self.animation.work_time % self.animation.work_time
            self.animation.frame += self.animation.skip_frame
            if self.animation.frame >= len(self.image):
                self.animation.frame = 0

    # оторажение
    def blit_character(self):
        if self.view == 'footmen':
            if self.direction == 'right':
                self.image = self.animation.anim_footmen_2G
            if self.direction == 'left':
                self.image = self.animation.anim_footmen_7G
            if self.direction == 'up':
                self.image = self.animation.anim_footmen_1G
            if self.direction == 'down':
                self.image = self.animation.anim_footmen_5G
            if self.direction == 'left_down':
                self.image = self.animation.anim_footmen_6G
            if self.direction == 'left_up':
                self.image = self.animation.anim_footmen_8G
            if self.direction == 'right_down':
                self.image = self.animation.anim_footmen_4G
            if self.direction == 'right_up':
                self.image = self.animation.anim_footmen_2G

            #  if self.direction == 'stay_down':
            #      self.image = self.animation_test_stay_down
            #  if self.direction == 'stay_left':
            #      self.image = self.animation_test_stay_left
            #  if self.direction == 'stay_right':
            #      self.image = self.animation_test_stay_right
            #  if self.direction == 'stay_up':
            #      self.image = self.animation_test_stay_up

            pygame.draw.rect(self.screen,(255, 255, 0),self.rect)
            # self.screen.blit(self.image[int(self.animation.frame)], self.rect)


            if self.health >= 70:
                self.health_colour = self.setting.health_colour_full
            if self.health < 70 and self.health >= 30:
                self.health_colour = self.setting.health_colour_medium
            if self.health < 30:
                self.health_colour = self.setting.health_colour_low

            # отображение жизни юнита
            pygame.draw.rect(self.screen, self.health_colour,
                             (self.rect.x - abs((self.setting.value[2][1] - self.setting.value[2][6])) / 2,
                              (self.rect.y + self.setting.value[2][2] + 10), 100, 8))
            pygame.draw.rect(self.screen, (0, 0, 0), ((self.rect.x - 11), (self.rect.y + 98), 102, 10), 1)
