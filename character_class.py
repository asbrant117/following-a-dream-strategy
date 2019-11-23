import pygame
from collide import collide_test
import character_animation


class Character(pygame.sprite.Sprite):
    def __init__(self, setting, screen, animation, view, command, x, y, camera_x, camera_y, idd, test):
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



        self.x1 = self.x2 = x + camera_x
        self.y1 = self.y2 = y + camera_y

        # self.x = x
        # self.y = y

        # флажок направления
        self.direction = 'down'
        self.collision = 'No'

        # информация о юните
        # вид юнита
        self.view = view
        # команда
        self.command = command
        # жизнь персонажа
        self.health = self.setting.value[2][5]
        self.health_colour = self.setting.health_colour_full

        self.idd = idd

        self.target = test
        self.time = 0
        self.collision = 'no'
        self.purpose = 'target'


    # Функция помогающая отслеживать перемещение
    def update_character(self, test):


        if self.purpose == 'target':
            if self.time == 0:
                distance0 = int(((test.rect.x - self.rect.x) ** 2 + (test.rect.y - self.rect.y) ** 2) ** 0.5)

                distance1 = int(
                    ((test.rect.x - self.rect.x + self.setting.value[2][3]) ** 2 + (
                                test.rect.y - self.rect.y) ** 2) ** 0.5)

                distance2 = int(
                    ((test.rect.x - self.rect.x - self.setting.value[2][3]) ** 2 + (
                                test.rect.y - self.rect.y) ** 2) ** 0.5)

                distance3 = int(
                    ((test.rect.x - self.rect.x) ** 2 + (
                                test.rect.y - self.rect.y + self.setting.value[2][3]) ** 2) ** 0.5)

                distance4 = int(
                    ((test.rect.x - self.rect.x) ** 2 + (
                                test.rect.y - self.rect.y - self.setting.value[2][3]) ** 2) ** 0.5)

                distance = min(distance1, distance2, distance3, distance4)

                if distance == distance1:
                    self.direction = 'left'
                if distance == distance2:
                    self.direction = 'right'
                if distance == distance3:
                    self.direction = 'up'
                if distance == distance4:
                    self.direction = 'down'


        # else:
        # время действия команды на новый поиск
        self.time += 1
        if self.time == 30:
            self.time = 0
        if abs(self.rect.x - test.rect.x) > 0 and abs(self.rect.x - test.rect.x) < 10:
            self.time = 0
        if abs(self.rect.y - test.rect.y) > 0 and abs(self.rect.y - test.rect.y) < 10:
            self.time = 0

        if self.direction == 'right' and self.collision != 'right':
            self.rect.x += self.setting.value[2][3]

        if self.direction == 'left' and self.collision != 'left':
            self.rect.x -= self.setting.value[2][3]

        if self.direction == 'up' and self.collision != 'top':
            self.rect.y -= self.setting.value[2][3]

        if self.direction == 'down' and self.collision != 'bottom':
            self.rect.y += self.setting.value[2][3]
        # # время жизни кадра
        # self.animation.work_time += dt
        # self.animation.skip_frame = self.animation.work_time / self.animation.time
        # if self.animation.skip_frame > 0:
        #     self.animation.work_time = self.animation.work_time % self.animation.work_time
        #     self.animation.frame += self.animation.skip_frame
        #     if self.animation.frame >= len(self.image):
        #         self.animation.frame = 0

    def collide(self, tiles):
        collide_test(self, tiles)

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

            pygame.draw.rect(self.screen, (255, 255, 0), self.rect)
            # self.screen.blit(self.image[int(self.animation.frame)], self.rect)
