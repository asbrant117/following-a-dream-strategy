import random

from character import Character


# создаем по определенным критериям персонажий и добавляем в группу
def create_characters(setting, screen, characters):
    # создание персонажа в определенных координатах
    while True:
        # рандомная выборка
        x = random.randint(510, 800)
        y = random.randint(300, 600)

        # проверка на пересечение с героем
        # if (x < (hero.rect.x - 150) or x > (hero.rect.x + 150)) or \
        #        (y < (hero.rect.y - 150) or y > (hero.rect.y + 150)):
        # создание персонажа
        character = Character(setting, screen, x=x, y=y, view='footmen', comand=1, health=100)

        characters.append(character)
        print(len(characters))
        return characters

        # проверка на пересечение с другими персонажами
        # if not pygame.sprite.spritecollideany(character, characters):
        #    # при отуствии пересечений с чем либо, мы добавляем в группу и выходим из цикла
        #    characters.add(character)
        #    break

#
