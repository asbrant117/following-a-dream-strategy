import pygame

import display
import events
from settings import Settings
from test_character import Test


def run_game():
    pygame.init()

    # создаем объект настроек.
    setting = Settings()

    # параметры экрана
    screen = pygame.display.set_mode((setting.screen_width, setting.screen_height))  # экран , pygame.FULLSCREEN
    pygame.display.set_caption('game')

    # создаем время для раскадровки
    dt = 0
    clock = pygame.time.Clock()

    # создаем объект, тестовый персонаж
    test = Test(setting, screen)
    # создаем список для класса
    characters = []
    # character = Character (setting,screen)

    # основной цикл
    while True:
        # события
        events.check_events(test, setting, screen, characters)

        # столкновения
        # test.collide_test(test,characters)
        test.collide_test(characters)

        # отображение
        display.update_screen(setting, screen, test, characters)

        test.update_test(dt)

        # счетчик времени для отображения кадра
        dt = clock.tick(setting.fps)

        # print(test.direction)


run_game()
