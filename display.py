import pygame


def update_screen(setting, screen, test, characters):
    # перерисовка
    # экран
    screen.fill(setting.screen_color)

    # тестовый героий
    test.blit_test()
    # персонажи
    for character in characters:
        character.blit_character()

    # отображение последнего прорисованного экрана
    pygame.display.flip()
