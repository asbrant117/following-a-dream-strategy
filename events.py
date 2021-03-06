import sys

import pygame

import character_create


def check_events(test, setting, screen, characters, camera, animation, healths, idd):
    # обработка действий
    for event in pygame.event.get():
        # выход
        if event.type == pygame.QUIT:
            sys.exit()

        # регистрация нажатия
        keys = pygame.key.get_pressed()
        # if event.type == pygame.KEYDOWN:

        if not (keys[pygame.K_s] and keys[pygame.K_w] and keys[pygame.K_a] and keys[pygame.K_d] and keys[
            pygame.K_SPACE]):
            test.direction = 'no'
            test.action = 'no'

        if keys[pygame.K_s] and not (keys[pygame.K_a] or keys[pygame.K_d]):
            test.direction = 'down'
            test.direction_stay = 'down'
        if keys[pygame.K_w] and not (keys[pygame.K_a] or keys[pygame.K_d]):
            test.direction = 'up'
            test.direction_stay = 'up'
        if keys[pygame.K_a] and not (keys[pygame.K_w] or keys[pygame.K_s]):
            test.direction = 'left'
            test.direction_stay = 'left'
        if keys[pygame.K_d] and not (keys[pygame.K_w] or keys[pygame.K_s]):
            test.direction = 'right'
            test.direction_stay = 'right'

        if keys[pygame.K_s] and keys[pygame.K_a]:
            test.direction = 'left_down'
            test.direction_stay = 'left_down'
        if keys[pygame.K_s] and keys[pygame.K_d]:
            test.direction = 'right_down'
            test.direction_stay = 'right_down'
        if keys[pygame.K_w] and keys[pygame.K_a]:
            test.direction = 'left_up'
            test.direction_stay = 'left_up'
        if keys[pygame.K_w] and keys[pygame.K_d]:
            test.direction = 'right_up'
            test.direction_stay = 'right_up'

        # передвижение камеры
        if keys[pygame.K_RIGHT]:
            camera.direction = 'right'
        if keys[pygame.K_LEFT]:
            camera.direction = 'left'
        if keys[pygame.K_DOWN]:
            camera.direction = 'down'
        if keys[pygame.K_UP]:
            camera.direction = 'up'

        # # атака героя
        if keys[pygame.K_SPACE]:
             test.action = 'yes'


        # создание персонажей
        if keys[pygame.K_BACKSPACE]:
            (characters, healths, idd) = character_create.create_characters(setting, screen, characters, camera,
                                                                            animation,
                                                                            healths, idd, test)

        # if event.type == pygame.KEYDOWN:
        #
        #     # атака героя
        #     if event.key == pygame.K_SPACE:
        #         test.action = 'yes'
        #         test.direction = 'no'
        #         test.direction_stay = 'no'

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                camera.direction = 'No'
            if event.key == pygame.K_LEFT:
                camera.direction = 'No'
            if event.key == pygame.K_UP:
                camera.direction = 'No'
            if event.key == pygame.K_DOWN:
                camera.direction = 'No'

