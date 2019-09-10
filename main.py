import pygame

import display
import events
from background_create import background
from camere import Camera
from settings import Settings
from character_class_test import Test
from character_animation import Animation
from background_class_full import Beckground_full

def run_game():
    pygame.init()

    # создаем время для раскадровки
    dt = 0
    clock = pygame.time.Clock()

    # создаем объект настроек.
    setting = Settings()
    # объект анимации и загрузок
    animation = Animation()

    #  ооздаем фон,травы, объектов, всего статичного в игре
    tiles_tree = background(setting)

    # параметры экрана
    screen = pygame.display.set_mode((setting.screen_width, setting.screen_height))  # экран , pygame.FULLSCREEN
    pygame.display.set_caption('game')

    # параметры экрана для создания фона окружения



    # создаем объект, тестовый персонаж
    test = Test(setting, screen,animation)
    # создаем список для класса
    characters = []
    #создаем фон
    background_full = Beckground_full(setting, screen)


    # создаем камеру
    camera = Camera(setting)

    # основной цикл
    while True:
        # события
        events.check_events(test, setting, screen, characters, camera,animation)

        # столкновения
        # test.collide_test(test,characters)
        test.collide_test(characters,tiles_tree)

        # отображение
        display.update_screen(setting, screen, test, characters,background_full)

        test.update_test(dt)
        camera.move(characters, test)

        # счетчик времени для отображения
        dt = clock.tick(setting.fps)

        # print(test.direction)


run_game()

