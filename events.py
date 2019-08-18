import sys

import pygame

import create_character
import camere


def check_events(test, setting, screen, characters,camera):
    # обработка действий
    for event in pygame.event.get():
        # выход
        if event.type == pygame.QUIT:
            sys.exit()

        # регистрация нажатия
        keys = pygame.key.get_pressed()
        # if event.type == pygame.KEYDOWN:

        if keys[pygame.K_s] and not (keys[pygame.K_a] or keys[pygame.K_d]):
            test.direction = 'down'
        if keys[pygame.K_w] and not (keys[pygame.K_a] or keys[pygame.K_d]):
            test.direction = 'up'
        if keys[pygame.K_a] and not (keys[pygame.K_w] or keys[pygame.K_s]):
            test.direction = 'left'
        if keys[pygame.K_d] and not (keys[pygame.K_w] or keys[pygame.K_s]):
            test.direction = 'right'

        if keys[pygame.K_s] and keys[pygame.K_a]:
            test.direction = 'left_down'
        if keys[pygame.K_s] and keys[pygame.K_d]:
            test.direction = 'right_down'
        if keys[pygame.K_w] and keys[pygame.K_a]:
            test.direction = 'left_up'
        if keys[pygame.K_w] and keys[pygame.K_d]:
            test.direction = 'right_up'

        #передвижение камеры
        if keys[pygame.K_RIGHT]:
            camera.direction = 'right'
        if keys[pygame.K_LEFT]:
            camera.direction = 'left'



        # создание персонажей
        if keys[pygame.K_BACKSPACE]:
            create_character.create_characters(setting, screen, characters)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                camera.direction = 'No'
            if event.key == pygame.K_LEFT:
                camera.direction = 'No'
