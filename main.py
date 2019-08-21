import pygame

import display
import events
from settings import Settings
from test_character import Test
from camere import Camera
from terra_tiles import Terra_Tiles


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

    #создаем камеру
    camera = Camera(setting)



    #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    # временно!!!!
    level = [
        "----------------------------------",
        "----------------------------------",
        "----------------------------------",
        "----------------------------------",
        "----------------------------------",
        "----------------------------------",
        "----------------------------------",
        "----------------------------------",
        "----------------------------------",
        "----------------------------------",
        "----------------------------------",
        "----------------------------------",
        "----------------------------------",
        "----------------------------------",
        "----------------------------------",
        "----------------------------------",
        "----------------------------------",
        "----------------------------------",
        "----------------------------------"]
    x = y = 0
    tiles = []
    for row in level:  # строка
        for col in row:  # часть строки
            if col == '-':
                tile = Terra_Tiles(setting,screen,x=x,y=y,view='grass')
                tiles.append(tile)
            x += 32
        y+=32
        x=0




    # основной цикл
    while True:
        # события
        events.check_events(test, setting, screen, characters,camera)

        # столкновения
        # test.collide_test(test,characters)
        test.collide_test(characters)

        # отображение
        display.update_screen(setting, screen, test, characters,tiles)

        test.update_test(dt)
        camera.move(characters,test)

        # счетчик времени для отображения
        dt = clock.tick(setting.fps)

        # print(test.direction)


run_game()
