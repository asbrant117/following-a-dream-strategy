from pygame import *
import os


ICON_DIR = os.path.dirname(__file__)  # Полный путь к каталогу с файлами


frame_Grass = [(0, 495, 32, 32)]
feame_Tree = [(0, 231, 32, 32)]

class Background_Animation(object):
    def __init__(self):
        self.time = 180
        self.work_time = 0
        self.skip_frame = 0
        self.frame = 0

        self.sprite_tile = image.load('%s/picter/TerraTiles.png' % ICON_DIR)

        self.anim_gras =  self.sprite_tile.subsurface(frame_Grass)
        self.anim_tree = self.sprite_tile.subsurface(feame_Tree)