from pygame import *
import os
import frame
from auxiliary_function import list_frame

# подсказка # S - стоит, G - идти
#       1
#   8       2
# 7           3
#   6       4
#       5

# тестовый персонаж
# кадры тестового персонажа (передвижение)

frame_test_1G = frame.frame_test_1G()
frame_test_2G = frame.frame_test_2G()
frame_test_3G = frame.frame_test_3G()
frame_test_4G = frame.frame_test_4G()
frame_test_5G = frame.frame_test_5G()
frame_test_6G = frame.frame_test_6G()
frame_test_7G = frame.frame_test_7G()
frame_test_8G = frame.frame_test_8G()

# кадры тестового персонажа (стоять)
frame_test_1S = frame.frame_test_1S()
frame_test_2S = frame.frame_test_2S()
frame_test_3S = frame.frame_test_3S()
frame_test_4S = frame.frame_test_4S()
frame_test_5S = frame.frame_test_5S()
frame_test_6S = frame.frame_test_6S()
frame_test_7S = frame.frame_test_7S()
frame_test_8S = frame.frame_test_8S()

frame_test_5A = frame.frame_test_5A()


# пехотинцы
# кадры пехотинца (передвижение)
frame_footmen_1G = frame.frame_footmen_1G()
frame_footmen_2G = frame.frame_footmen_2G()
frame_footmen_3G = frame.frame_footmen_3G()
frame_footmen_4G = frame.frame_footmen_4G()
frame_footmen_5G = frame.frame_footmen_5G()
frame_footmen_6G = frame.frame_footmen_6G()
frame_footmen_7G = frame.frame_footmen_7G()
frame_footmen_8G = frame.frame_footmen_8G()

# кадры пехотинца (стоять)
frame_footmen_1S = frame.frame_footmen_1S()
frame_footmen_2S = frame.frame_footmen_2S()
frame_footmen_3S = frame.frame_footmen_3S()
frame_footmen_4S = frame.frame_footmen_4S()
frame_footmen_5S = frame.frame_footmen_5S()
frame_footmen_6S = frame.frame_footmen_6S()
frame_footmen_7S = frame.frame_footmen_7S()
frame_footmen_8S = frame.frame_footmen_8S()

# Бугай
# пехотинцы
# кадры пехотинца (передвижение)
frame_grunt_1G = frame.frame_grunt_1G()
frame_grunt_2G = frame.frame_grunt_2G()
frame_grunt_3G = frame.frame_grunt_3G()
frame_grunt_4G = frame.frame_grunt_4G()
frame_grunt_5G = frame.frame_grunt_5G()
frame_grunt_6G = frame.frame_grunt_6G()
frame_grunt_7G = frame.frame_grunt_7G()
frame_grunt_8G = frame.frame_grunt_8G()

# кадры пехотинца (стоять)
frame_grunt_1S = frame.frame_grunt_1S()
frame_grunt_2S = frame.frame_grunt_2S()
frame_grunt_3S = frame.frame_grunt_3S()
frame_grunt_4S = frame.frame_grunt_4S()
frame_grunt_5S = frame.frame_grunt_5S()
frame_grunt_6S = frame.frame_grunt_6S()
frame_grunt_7S = frame.frame_grunt_7S()
frame_grunt_8S = frame.frame_grunt_8S()

# травушка - муравушка
frame_grass = frame.frame_grass()

ICON_DIR = os.path.dirname(__file__)  # Полный путь к каталогу с файлами


class Animation(object):
    def __init__(self):
        #параметры для передачи кадров
        self.time = 180
        self.work_time = 0
        self.skip_frame = 0
        self.frame = 0

        self.sprite_test = image.load('%s/picter/Footmen.png' % ICON_DIR)
        self.sprite_footmen = image.load('%s/picter/Footmen.png' % ICON_DIR)
        self.sprite_grunt = image.load('%s/picter/Grunt.png' % ICON_DIR)
        self.sprite_grass = image.load('%s/picter/TerraTiles.png' % ICON_DIR)

        self.amim_grass = list_frame(frame_grass, self.sprite_grass.subsurface)

        # тестовый
        # анимация тестового героя (передвижение)
        self.anim_test_1G = list_frame(frame_test_1G, self.sprite_test.subsurface)
        self.anim_test_2G = list_frame(frame_test_2G, self.sprite_test.subsurface)
        self.anim_test_3G = list_frame(frame_test_3G, self.sprite_test.subsurface)
        self.anim_test_4G = list_frame(frame_test_4G, self.sprite_test.subsurface)
        self.anim_test_5G = list_frame(frame_test_5G, self.sprite_test.subsurface)
        self.anim_test_6G = list_frame(frame_test_6G, self.sprite_test.subsurface)
        self.anim_test_7G = list_frame(frame_test_7G, self.sprite_test.subsurface)
        self.anim_test_8G = list_frame(frame_test_8G, self.sprite_test.subsurface)
        # анимация тестового героя (стоять)
        self.anim_test_1S = list_frame(frame_test_1S, self.sprite_test.subsurface)
        self.anim_test_2S = list_frame(frame_test_2S, self.sprite_test.subsurface)
        self.anim_test_3S = list_frame(frame_test_3S, self.sprite_test.subsurface)
        self.anim_test_4S = list_frame(frame_test_4S, self.sprite_test.subsurface)
        self.anim_test_5S = list_frame(frame_test_5S, self.sprite_test.subsurface)
        self.anim_test_6S = list_frame(frame_test_6S, self.sprite_test.subsurface)
        self.anim_test_7S = list_frame(frame_test_7S, self.sprite_test.subsurface)
        self.anim_test_8S = list_frame(frame_test_8S, self.sprite_test.subsurface)
        # анимация тестового героя (атака)
        self.anim_test_5A = list_frame(frame_test_5A, self.sprite_test.subsurface)


        # Пехотинец
        # анимация пехотинцы (передвижение)
        self.anim_footmen_1G = list_frame(frame_footmen_1G, self.sprite_footmen.subsurface)
        self.anim_footmen_2G = list_frame(frame_footmen_2G, self.sprite_footmen.subsurface)
        self.anim_footmen_3G = list_frame(frame_footmen_3G, self.sprite_footmen.subsurface)
        self.anim_footmen_4G = list_frame(frame_footmen_4G, self.sprite_footmen.subsurface)
        self.anim_footmen_5G = list_frame(frame_footmen_5G, self.sprite_footmen.subsurface)
        self.anim_footmen_6G = list_frame(frame_footmen_6G, self.sprite_footmen.subsurface)
        self.anim_footmen_7G = list_frame(frame_footmen_7G, self.sprite_footmen.subsurface)
        self.anim_footmen_8G = list_frame(frame_footmen_8G, self.sprite_footmen.subsurface)
        # анимация пехотинца (стоять)
        self.anim_footmen_1S = list_frame(frame_footmen_1S, self.sprite_footmen.subsurface)
        self.anim_footmen_2S = list_frame(frame_footmen_2S, self.sprite_footmen.subsurface)
        self.anim_footmen_3S = list_frame(frame_footmen_3S, self.sprite_footmen.subsurface)
        self.anim_footmen_4S = list_frame(frame_footmen_4S, self.sprite_footmen.subsurface)
        self.anim_footmen_5S = list_frame(frame_footmen_5S, self.sprite_footmen.subsurface)
        self.anim_footmen_6S = list_frame(frame_footmen_6S, self.sprite_footmen.subsurface)
        self.anim_footmen_7S = list_frame(frame_footmen_7S, self.sprite_footmen.subsurface)
        self.anim_footmen_8S = list_frame(frame_footmen_8S, self.sprite_footmen.subsurface)





        #Бугай
        # анимация тестового героя (передвижение)
        self.anim_grunt_1G = list_frame(frame_grunt_1G, self.sprite_grunt.subsurface)
        self.anim_grunt_2G = list_frame(frame_grunt_2G, self.sprite_grunt.subsurface)
        self.anim_grunt_3G = list_frame(frame_grunt_3G, self.sprite_grunt.subsurface)
        self.anim_grunt_4G = list_frame(frame_grunt_4G, self.sprite_grunt.subsurface)
        self.anim_grunt_5G = list_frame(frame_grunt_5G, self.sprite_grunt.subsurface)
        self.anim_grunt_6G = list_frame(frame_grunt_6G, self.sprite_grunt.subsurface)
        self.anim_grunt_7G = list_frame(frame_grunt_7G, self.sprite_grunt.subsurface)
        self.anim_grunt_8G = list_frame(frame_grunt_8G, self.sprite_grunt.subsurface)
        # анимация тестового героя (стоять)
        self.anim_grunt_1S = list_frame(frame_grunt_1S, self.sprite_grunt.subsurface)
        self.anim_grunt_2S = list_frame(frame_grunt_2S, self.sprite_grunt.subsurface)
        self.anim_grunt_3S = list_frame(frame_grunt_3S, self.sprite_grunt.subsurface)
        self.anim_grunt_4S = list_frame(frame_grunt_4S, self.sprite_grunt.subsurface)
        self.anim_grunt_5S = list_frame(frame_grunt_5S, self.sprite_grunt.subsurface)
        self.anim_grunt_6S = list_frame(frame_grunt_6S, self.sprite_grunt.subsurface)
        self.anim_grunt_7S = list_frame(frame_grunt_7S, self.sprite_grunt.subsurface)
        self.anim_grunt_8S = list_frame(frame_grunt_8S, self.sprite_grunt.subsurface)

