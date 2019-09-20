import pygame


class Health(pygame.sprite.Sprite):
    def __init__(self, setting, screen, character):
        pygame.sprite.Sprite.__init__(self)

        self.screen = screen
        self.setting = setting
        self.character = character

        self.rect = pygame.Rect((self.character.rect.x - abs((self.setting.value[2][1] - self.setting.value[2][6])) / 2,
                                 (self.character.rect.y + self.setting.value[2][2] + 10), 100, 8))

        self.rect_edging = (self.rect.x - 1, self.rect.y - 1, 100 + 2, 8 + 2)
        self.health = self.character.health

        # if self.health >= 70:
        #     self.health_colour = self.setting.health_colour_full
        # if self.health < 70 and self.health >= 30:
        #     self.health_colour = self.setting.health_colour_medium
        # if self.health < 30:
        #     self.health_colour = self.setting.health_colour_low

    def blit_Health(self):
        pygame.draw.rect(self.screen, self.setting.health_colour_full, self.rect)
        pygame.draw.rect(self.screen, (0, 0, 0), self.rect_edging, 1)
