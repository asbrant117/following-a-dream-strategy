import pygame


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

    for health in healths:
        health.blit_health()

    # отображение последнего прорисованного экрана
    pygame.display.flip()
