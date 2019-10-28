import pygame

import display
import events
from main_challenging_objects import challenging_objects


def run_game():
    pygame.init()
    # создание всех объектов
    (dt, clock, setting, animation, background_animation, screen, tiles, test, characters, healths, background_full,
     camera,idd) = challenging_objects()
    # основной цикл
    while True:
        # события
        events.check_events(test, setting, screen, characters, camera, animation, healths,idd)

        # столкновения
        # test.collide_test(test,characters)
        test.collide_test(characters, tiles)

        # отображение
        display.update_screen(setting, screen, test, characters, background_full, healths)

        test.update_test(dt)
        camera.move(characters, test)

        # счетчик времени для отображения
        dt = clock.tick(setting.fps)


run_game()
