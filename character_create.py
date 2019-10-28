import random

from character_class import Character
from character_class_health import Health


# создаем по определенным критериям персонажий и добавляем в группу
def create_characters(setting, screen, characters, camera, animation, healths, idd,test):
    # создание персонажа в определенных координатах
    while True:
        # рандомная выборка
        x = random.randint(540, 540)
        y = random.randint(540,540)

        # проверка на пересечение с героем
        # if (x < (hero.rect.x - 150) or x > (hero.rect.x + 150)) or \
        #        (y < (hero.rect.y - 150) or y > (hero.rect.y + 150)):
        # создание персонажа
        character = Character(setting, screen, animation, x=x, y=y, view='footmen', command=1, camera_x=camera.x,
                              camera_y=camera.y, idd=idd,test = test)

        characters.append(character)

        health = Health(setting, screen, character)

        healths.append(health)

        idd = idd + 1
        return characters, healths, idd

        # проверка на пересечение с другими персонажами
        # if not pygame.sprite.spritecollideany(character, characters):
        #    # при отуствии пересечений с чем либо, мы добавляем в группу и выходим из цикла
        #    characters.add(character)
        #    break

#
