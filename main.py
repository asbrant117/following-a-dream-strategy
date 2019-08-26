import pygame

import display
import events
from background import background
from camere import Camera
from settings import Settings
from test_character import Test
from animation import Animation

def run_game():
    pygame.init()

    # создаем время для раскадровки
    dt = 0
    clock = pygame.time.Clock()

    # создаем объект настроек.
    setting = Settings()
    # объект анимации и загрузок
    animation = Animation()

    # ооздаем фон,травы, объектов, всего статичного в игре
    #background(setting)

    # параметры экрана
    screen = pygame.display.set_mode((setting.screen_width, setting.screen_height))  # экран , pygame.FULLSCREEN
    pygame.display.set_caption('game')

    # параметры экрана для создания фона окружения



    # создаем объект, тестовый персонаж
    test = Test(setting, screen,animation)
    # создаем список для класса
    characters = []
    # character = Character (setting,screen)

    # создаем камеру
    camera = Camera(setting)

    # основной цикл
    while True:
        # события
        events.check_events(test, setting, screen, characters, camera,animation)

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
