import pygame

import display
import events
from background import background
from camere import Camera
from settings import Settings
from test_character import Test


def run_game():
    pygame.init()

    # создаем объект настроек.
    setting = Settings()

    # ооздаем фон
    background(setting)

    # параметры экрана
    screen = pygame.display.set_mode((setting.screen_width, setting.screen_height))  # экран , pygame.FULLSCREEN
    pygame.display.set_caption('game')

    # параметры экрана для создания фона окружения

    # создаем время для раскадровки
    dt = 0
    clock = pygame.time.Clock()

    # создаем объект, тестовый персонаж
    test = Test(setting, screen)
    # создаем список для класса
    characters = []
    # character = Character (setting,screen)

    # создаем камеру
    camera = Camera(setting)

    # основной цикл
    while True:
        # события
        events.check_events(test, setting, screen, characters, camera)

        # столкновения
        # test.collide_test(test,characters)
        test.collide_test(characters)

        # отображение
        display.update_screen(setting, screen, test, characters)

        test.update_test(dt)
        camera.move(characters, test)

        # счетчик времени для отображения
        dt = clock.tick(setting.fps)

        # print(test.direction)


run_game()
