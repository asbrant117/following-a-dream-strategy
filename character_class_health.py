import pygame
from pygame import *
import character_class


class Health(character_class.Character):
    def __init__(self, setting, screen, animation, view, command, x, y, camera_x, camera_y):
        character_class.Character.__init__(self, setting, screen, animation, view, command, x, y, camera_x, camera_y)
        # инициализируем настройки и поверхность


        self.rect_health = pygame.Rect((self.rect.x - abs(
            (self.setting.value[self.view][1] - self.setting.value[self.view][6])) / 2,
                                 (self.rect.y + self.setting.value[self.view][2] + 10), 100, 8))

    def blit_health(self):
        if self.health < 70 and self.health >= 30:
            self.health_colour = self.setting.health_colour_medium
        if self.health < 30:
            self.health_colour = self.setting.health_colour_low

            # отображение жизни юнита
        pygame.draw.rect(self.screen, self.health_colour, self.rect_health )
