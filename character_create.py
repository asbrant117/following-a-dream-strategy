import random

from character_class import Character
from character_class_health import Health


# создаем по определенным критериям персонажий и добавляем в группу
def create_characters(setting, screen, characters, camera, animation, healths):
    # создание персонажа в определенных координатах
    while True:
        # рандомная выборка
        x = random.randint(510, 800)
        y = random.randint(300, 600)

        # проверка на пересечение с героем
        # if (x < (hero.rect.x - 150) or x > (hero.rect.x + 150)) or \
        #        (y < (hero.rect.y - 150) or y > (hero.rect.y + 150)):
        # создание персонажа
        # test - 1
        # footmen - 2
        # grunt - 3
        character = Character(setting, screen, animation, x=x, y=y, view=1, command=1, camera_x=camera.x,
                              camera_y=camera.y)

        characters.append(character)

        health = Health(setting, screen, animation, x=x, y=y, view=1, command=1, camera_x=camera.x,
                              camera_y=camera.y)
        #
        healths.append(health)
        return (characters, healths)

        # проверка на пересечение с другими персонажами
        # if not pygame.sprite.spritecollideany(character, characters):
        #    # при отуствии пересечений с чем либо, мы добавляем в группу и выходим из цикла
        #    characters.add(character)
        #    break

#
