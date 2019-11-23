import pygame
from background_create import background
from camere import Camera
from settings import Settings
from character_class_test import Test
from character_animation import Animation
from background_class_full import Beckground_full
from background_animation_statically import Background_Animation
from background_physical import background_physical


def challenging_objects():
    # создаем время для раскадровки
    dt = 0
    clock = pygame.time.Clock()

    # создаем объект настроек.
    setting = Settings()

    # объект анимации и загрузок
    animation = Animation()
    background_animation = Background_Animation()

    # #  ооздаем фон, создается картинка в отдельном окне
    # background(setting, background_animation)

    # параметры экрана
    screen = pygame.display.set_mode((setting.screen_width, setting.screen_height))  # экран , pygame.FULLSCREEN
    pygame.display.set_caption('game')

    # создание списка с объектами для соударений
    tiles = background_physical(setting, background_animation, screen)

    # создаем объект, тестовый персонаж
    test = Test(setting, screen, animation)

    # создаем список для классов персонажи, здоровья
    characters = []
    healths = []

    # создаем фон
    background_full = Beckground_full(setting, screen)

    # создаем камеру
    camera = Camera(setting)

    idd = 0

    return (
        dt, clock, setting, animation, background_animation, screen, tiles, test, characters, healths, background_full,
        camera, idd)
