import pygame


class Health(pygame.sprite.Sprite):
    def __init__(self, setting, screen, character):
        pygame.sprite.Sprite.__init__(self)

        self.screen = screen
        self.setting = setting
        self.character = character

        self.rect = pygame.Rect((self.character.rect.x - abs((self.setting.value[2][1] - self.setting.value[2][6]))/ 2,
                                      (self.character.rect.y + self.setting.value[2][2] + 10), 100, 8))

    def blit_Health(self):
        pygame.draw.rect(self.screen,self.setting.health_colour_full,self.rect)