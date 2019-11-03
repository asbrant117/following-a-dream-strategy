from pygame import *
def collide_test(test, chatacters):
    for chatacter in chatacters:
        if sprite.collide_rect(test, chatacter):
            if test.rect.right >= chatacter.rect.left - test.setting.value[1][
                3] and test.rect.right <= chatacter.rect.left + test.setting.value[1][
                3] and test.rect.bottom >= chatacter.rect.top:
                test.rect.right = chatacter.rect.left
                test.collision = 'right'

            if test.rect.left >= chatacter.rect.right - test.setting.value[1][
                3] and test.rect.left <= chatacter.rect.right + test.setting.value[1][3]:
                test.rect.left = chatacter.rect.right
                test.collision = 'left'

            if test.rect.bottom >= chatacter.rect.top - test.setting.value[1][
                3] and test.rect.bottom <= chatacter.rect.top + test.setting.value[1][3]:
                test.rect.bottom = chatacter.rect.top
                test.collision = 'bottom'

            if test.rect.top >= chatacter.rect.bottom - test.setting.value[1][
                3] and test.rect.top <= chatacter.rect.bottom + 4:
                test.rect.top = chatacter.rect.bottom
                test.collision = 'top'
        else:
            test.collision = 'no'

