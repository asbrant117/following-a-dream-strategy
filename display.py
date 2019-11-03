import pygame
# заметка, отоброжения фона слишком тормозит процесс. данная опирация много жрет, почему? что делать?

def update_screen(setting, screen, test, characters, background_full,healths):
    # перерисовка
    # экран
    screen.fill(setting.screen_color)

    # фон
    background_full.blit_background_full()

    # тестовый героий
    test.blit_test()
    # персонажи
    for character in characters:
        character.blit_character()
        character.update_character(test)
    for health in healths:
        health.blit_Health()

    # отображение последнего прорисованного экрана
    pygame.display.flip()
