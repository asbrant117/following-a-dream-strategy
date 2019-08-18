import pygame

# from auxiliary_function import animation

# анимация для тестового героя
# передвижение
ANIMATION_DOWN = [(33, 19, 64, 92), (38, 250, 64, 92), (41, 140, 64, 92), (38, 250, 64, 92), (33, 19, 64, 92),
                  (32, 445, 64, 92), (32, 349, 66, 92), (32, 445, 64, 92)]
ANIMATION_LEFT_DOWN = [(159, 20, 84, 92), (159, 250, 89, 92), (159, 140, 89, 92), (159, 250, 89, 92), (159, 20, 84, 92),
                       (159, 442, 89, 96), (162, 344, 89, 92), (159, 442, 89, 96)]
ANIMATION_LEFT = [(310, 17, 70, 92), (306, 250, 105, 92), (300, 140, 105, 92), (306, 250, 105, 92), (310, 17, 70, 92),
                  (306, 445, 105, 92), (306, 350, 105, 92), (306, 445, 105, 92)]  #
ANIMATION_LEFT_UP = [(456, 14, 84, 92), (456, 246, 89, 92), (456, 136, 89, 92), (456, 246, 89, 92), (456, 14, 84, 92),
                     (456, 443, 89, 96), (456, 345, 89, 92), (456, 443, 89, 96)]  #
ANIMATION_UP = [(620, 14, 84, 92), (622, 244, 89, 92), (622, 130, 89, 92), (622, 244, 89, 92), (620, 14, 84, 92),
                (622, 444, 89, 92), (622, 346, 89, 92), (622, 444, 89, 92)]  #
ANIMATION_RIGHT_UP = [(940, 14, 84, 92), (940, 246, 89, 92), (940, 136, 89, 92), (940, 246, 89, 92), (940, 14, 84, 92),
                      (940, 443, 89, 96), (940, 345, 89, 92), (940, 443, 89, 96)]  #
ANIMATION_RIGHT = [(1088, 17, 70, 92), (1088, 250, 105, 92), (1088, 140, 105, 92), (1088, 250, 105, 92),
                   (1088, 17, 70, 92), (1088, 445, 105, 92), (1088, 350, 105, 92), (1088, 445, 105, 92)]
ANIMATION_RIGHT_DOWN = [(1232, 19, 84, 92), (1232, 252, 89, 92), (1232, 140, 89, 92), (1232, 252, 89, 92),
                        (1232, 19, 84, 92), (1232, 444, 89, 96), (1232, 344, 89, 92), (1232, 444, 89, 96)]
# стоит

ANIMATION_Stay_DOWN = [(33, 19, 64, 92), (33, 19, 64, 92), (33, 19, 64, 92), (33, 19, 64, 92), (33, 19, 64, 92),
                       (33, 19, 64, 92), (33, 19, 64, 92), (33, 19, 64, 92)]
ANIMATION_Stay_LEFT_DOWN = [(159, 20, 84, 92), (159, 20, 84, 92), (159, 20, 84, 92), (159, 20, 84, 92),
                            (159, 20, 84, 92), (159, 20, 84, 92), (159, 20, 84, 92), (159, 20, 84, 92)]
ANIMATION_Stay_LEFT = [(310, 17, 70, 92), (310, 17, 70, 92), (310, 17, 70, 92), (310, 17, 70, 92), (310, 17, 70, 92),
                       (310, 17, 70, 92), (310, 17, 70, 92), (310, 17, 70, 92)]
ANIMATION_Stay_LEFT_UP = [(456, 14, 84, 92), (456, 14, 84, 92), (456, 14, 84, 92), (456, 14, 84, 92), (456, 14, 84, 92),
                          (456, 14, 84, 92), (456, 14, 84, 92), (456, 14, 84, 92)]
ANIMATION_Stay_UP = [(620, 14, 84, 92), (620, 14, 84, 92), (620, 14, 84, 92), (620, 14, 84, 92), (620, 14, 84, 92),
                     (620, 14, 84, 92), (620, 14, 84, 92), (620, 14, 84, 92)]
ANIMATION_Stay_RIGHT_UP = [(940, 14, 84, 92), (940, 14, 84, 92), (940, 14, 84, 92), (940, 14, 84, 92),
                           (940, 14, 84, 92), (940, 14, 84, 92), (940, 14, 84, 92), (940, 14, 84, 92)]
ANIMATION_Stay_RIGHT = [(1088, 17, 70, 92), (1088, 17, 70, 92), (1088, 17, 70, 92), (1088, 17, 70, 92),
                        (1088, 17, 70, 92), (1088, 17, 70, 92), (1088, 17, 70, 92), (1088, 17, 70, 92)]
ANIMATION_Stay_RIGHT_DOWN = [(1232, 19, 84, 92), (1232, 19, 84, 92), (1232, 19, 84, 92), (1232, 19, 84, 92),
                             (1232, 19, 84, 92), (1232, 19, 84, 92), (1232, 19, 84, 92), (1232, 19, 84, 92)]

# анимация бугая
# передвижение
ANIMATION_Grunt_DOWN = [(32, 12, 80, 94), (32, 118, 86, 94), (32, 228, 86, 94), (32, 118, 86, 94), (32, 12, 80, 94),
                        (32, 342, 86, 94), (32, 442, 86, 94), (32, 342, 86, 94)]
ANIMATION_Grunt_LEFT_DOWN = [(184, 12, 80, 94), (184, 118, 86, 94), (184, 228, 86, 94), (184, 118, 86, 94),
                             (184, 342, 86, 94), (184, 442, 88, 94), (184, 342, 86, 94)]
ANIMATION_Grunt_LEFT = [(318, 12, 80, 94), (318, 118, 86, 94), (318, 228, 86, 94), (318, 118, 86, 94),
                        (318, 12, 80, 94), (318, 342, 86, 94), (318, 442, 88, 94), (318, 342, 86, 94)]
ANIMATION_Grunt_LEFT_UP = [(470, 12, 80, 94), (470, 118, 86, 94), (470, 228, 86, 94), (470, 118, 86, 94),
                           (470, 12, 80, 94), (470, 342, 86, 94), (470, 442, 88, 94), (470, 342, 86, 94)]
ANIMATION_Grunt_UP = [(628, 12, 80, 94), (628, 118, 86, 94), (628, 228, 86, 94), (628, 118, 86, 94), (628, 12, 80, 94),
                      (628, 342, 86, 94), (628, 442, 88, 94), (628, 342, 86, 94)]
ANIMATION_Grunt_RIGHT_UP = [(914, 12, 80, 94), (914, 118, 86, 94), (914, 228, 86, 94), (914, 118, 86, 94),
                            (914, 12, 80, 94), (914, 342, 86, 94), (914, 442, 88, 94), (914, 342, 86, 94)]
ANIMATION_Grunt_RIGHT = [(1066, 12, 88, 94), (1066, 118, 88, 94), (1066, 228, 88, 94), (1066, 118, 88, 94),
                         (1066, 12, 88, 94), (1066, 342, 88, 94), (1066, 442, 88, 94), (1066, 342, 88, 94)]
ANIMATION_Grunt_RIGHT_DOWN = [(1214, 12, 80, 94), (1214, 118, 86, 94), (1214, 228, 86, 94), (1214, 118, 86, 94),
                              (1214, 12, 80, 94), (1214, 342, 86, 94), (1214, 442, 88, 94), (1214, 342, 86, 94)]
# стоит
ANIMATION_Grunt_Stay_DOWN = [(32, 12, 80, 94), (32, 12, 80, 94), (32, 12, 80, 94), (32, 12, 80, 94), (32, 12, 80, 94),
                             (32, 12, 80, 94), (32, 12, 80, 94), (32, 12, 80, 94)]
ANIMATION_Grunt_Stay_LEFT_DOWN = [(184, 12, 80, 94), (184, 12, 80, 94), (184, 12, 80, 94), (184, 12, 80, 94),
                                  (184, 12, 80, 94), (184, 12, 80, 94), (184, 12, 80, 94), (184, 12, 80, 94)]
ANIMATION_Grunt_Stay_LEFT = [(318, 12, 80, 94), (318, 12, 80, 94), (318, 12, 80, 94), (318, 12, 80, 94),
                             (318, 12, 80, 94), (318, 12, 80, 94), (318, 12, 80, 94), (318, 12, 80, 94)]
ANIMATION_Grunt_Stay_LEFT_UP = [(470, 12, 80, 94), (470, 12, 80, 94), (470, 12, 80, 94), (470, 12, 80, 94),
                                (470, 12, 80, 94), (470, 12, 80, 94), (470, 12, 80, 94), (470, 12, 80, 94)]
ANIMATION_Grunt_Stay_UP = [(628, 12, 80, 94), (628, 12, 80, 94), (628, 12, 80, 94), (628, 12, 80, 94),
                           (628, 12, 80, 94), (628, 12, 80, 94), (628, 12, 80, 94), (628, 12, 80, 94)]
ANIMATION_Grunt_Stay_RIGHT_UP = [(914, 12, 80, 94), (914, 12, 80, 94), (914, 12, 80, 94), (914, 12, 80, 94),
                                 (914, 12, 80, 94), (914, 12, 80, 94), (914, 12, 80, 94), (914, 12, 80, 94)]
ANIMATION_Grunt_Stay_RIGHT = [(1066, 12, 88, 94), (1066, 12, 88, 94), (1066, 12, 88, 94), (1066, 12, 88, 94),
                              (1066, 12, 88, 94), (1066, 12, 88, 94), (1066, 12, 88, 94), (1066, 12, 88, 94)]
ANIMATION_Grunt_Stay_RIGHT_DOWN = [(1214, 12, 80, 94), (1214, 12, 80, 94), (1214, 12, 80, 94), (1214, 12, 80, 94),
                                   (1214, 12, 80, 94), (1214, 12, 80, 94), (1214, 12, 80, 94), (1214, 12, 80, 94)]

# анимация для тестового героя
# передвижение
ANIMATION_Footmen_DOWN = [(33, 19, 64, 92), (38, 250, 64, 92), (41, 140, 64, 92), (38, 250, 64, 92), (33, 19, 64, 92),
                          (32, 445, 64, 92), (32, 349, 66, 92), (32, 445, 64,
                                                                 92)]
ANIMATION_Footmen_LEFT_DOWN = [(159, 20, 84, 92), (159, 250, 89, 92), (159, 140, 89, 92), (159, 250, 89, 92),
                               (159, 20, 84, 92), (159, 442, 89, 96), (162, 344, 89, 92), (159, 442, 89,
                                                                                           96)]
ANIMATION_Footmen_LEFT = [(310, 17, 70, 92), (306, 250, 105, 92), (300, 140, 105, 92), (306, 250, 105, 92),
                          (310, 17, 70, 92), (306, 445, 105, 92), (306, 350, 105, 92), (306, 445, 105, 92)]  #
ANIMATION_Footmen_LEFT_UP = [(456, 14, 84, 92), (456, 246, 89, 92), (456, 136, 89, 92), (456, 246, 89, 92),
                             (456, 14, 84, 92), (456, 443, 89, 96), (456, 345, 89, 92), (456, 443, 89, 96)]  #
ANIMATION_Footmen_UP = [(620, 14, 84, 92), (622, 244, 89, 92), (622, 130, 89, 92), (622, 244, 89, 92),
                        (620, 14, 84, 92), (622, 444, 89, 92), (622, 346, 89, 92), (622, 444, 89, 92)]  #
ANIMATION_Footmen_RIGHT_UP = [(940, 14, 84, 92), (940, 246, 89, 92), (940, 136, 89, 92), (940, 246, 89, 92),
                              (940, 14, 84, 92), (940, 443, 89, 96), (940, 345, 89, 92), (940, 443, 89, 96)]  #
ANIMATION_Footmen_RIGHT = [(1088, 17, 70, 92), (1088, 250, 105, 92), (1088, 140, 105, 92), (1088, 250, 105, 92),
                           (1088, 17, 70, 92), (1088, 445, 105, 92), (1088, 350, 105, 92), (1088, 445, 105, 92)]
ANIMATION_Footmen_RIGHT_DOWN = [(1232, 19, 84, 92), (1232, 252, 89, 92), (1232, 140, 89, 92), (1232, 252, 89, 92),
                                (1232, 19, 84, 92), (1232, 444, 89, 96), (1232, 344, 89, 92), (1232, 444, 89, 96)]
# стоит _Footmen

ANIMATION_Footmen_Stay_DOWN = [(33, 19, 64, 92), (33, 19, 64, 92), (33, 19, 64, 92), (33, 19, 64, 92), (33, 19, 64, 92),
                               (33, 19, 64, 92), (33, 19, 64, 92), (33, 19, 64, 92)]
ANIMATION_Footmen_Stay_LEFT_DOWN = [(159, 20, 84, 92), (159, 20, 84, 92), (159, 20, 84, 92), (159, 20, 84, 92),
                                    (159, 20, 84, 92), (159, 20, 84, 92), (159, 20, 84, 92), (159, 20, 84, 92)]
ANIMATION_Footmen_Stay_LEFT = [(310, 17, 70, 92), (310, 17, 70, 92), (310, 17, 70, 92), (310, 17, 70, 92),
                               (310, 17, 70, 92), (310, 17, 70, 92), (310, 17, 70, 92), (310, 17, 70, 92)]
ANIMATION_Footmen_Stay_LEFT_UP = [(456, 14, 84, 92), (456, 14, 84, 92), (456, 14, 84, 92), (456, 14, 84, 92),
                                  (456, 14, 84, 92), (456, 14, 84, 92), (456, 14, 84, 92), (456, 14, 84, 92)]
ANIMATION_Footmen_Stay_UP = [(620, 14, 84, 92), (620, 14, 84, 92), (620, 14, 84, 92), (620, 14, 84, 92),
                             (620, 14, 84, 92), (620, 14, 84, 92), (620, 14, 84, 92), (620, 14, 84, 92)]
ANIMATION_Footmen_Stay_RIGHT_UP = [(940, 14, 84, 92), (940, 14, 84, 92), (940, 14, 84, 92), (940, 14, 84, 92),
                                   (940, 14, 84, 92), (940, 14, 84, 92), (940, 14, 84, 92), (940, 14, 84, 92)]
ANIMATION_Footmen_Stay_RIGHT = [(1088, 17, 70, 92), (1088, 17, 70, 92), (1088, 17, 70, 92), (1088, 17, 70, 92),
                                (1088, 17, 70, 92), (1088, 17, 70, 92), (1088, 17, 70, 92), (1088, 17, 70, 92)]
ANIMATION_Footmen_Stay_RIGHT_DOWN = [(1232, 19, 84, 92), (1232, 19, 84, 92), (1232, 19, 84, 92), (1232, 19, 84, 92),
                                     (1232, 19, 84, 92), (1232, 19, 84, 92), (1232, 19, 84, 92), (1232, 19, 84, 92)]


# как организовать функцию для переложения анимации
class Animation():
    def __init__(self):

        self.sprite_test = pygame.image.load('picter/Footmen.png').convert_alpha()
        self.sprite_Footman = pygame.image.load('picter/Footmen.png').convert_alpha()
        self.sprite_Grunt = pygame.image.load('picter/Grunt.png').convert_alpha()

        # блок для анимации тестоого героя
        # передвижение
        anim = []
        for frame in ANIMATION_DOWN:
            anim.append(self.sprite_test.subsurface(frame))
        self.anim_test_down = anim

        anim = []
        for frame in ANIMATION_LEFT:
            anim.append(self.sprite_test.subsurface(frame))
        self.anim_test_left = anim

        anim = []
        for frame in ANIMATION_LEFT_DOWN:
            anim.append(self.sprite_test.subsurface(frame))
        self.anim_test_left_down = anim

        anim = []
        for frame in ANIMATION_LEFT_UP:
            anim.append(self.sprite_test.subsurface(frame))
        self.anim_test_left_up = anim

        anim = []
        for frame in ANIMATION_RIGHT:
            anim.append(self.sprite_test.subsurface(frame))
        self.anim_test_right = anim

        anim = []
        for frame in ANIMATION_RIGHT_DOWN:
            anim.append(self.sprite_test.subsurface(frame))
        self.anim_test_right_down = anim

        anim = []
        for frame in ANIMATION_RIGHT_UP:
            anim.append(self.sprite_test.subsurface(frame))
        self.anim_test_right_up = anim

        anim = []
        for frame in ANIMATION_UP:
            anim.append(self.sprite_test.subsurface(frame))
        self.anim_test_up = anim

        # стоять
        anim = []
        for frame in ANIMATION_Stay_DOWN:
            anim.append(self.sprite_test.subsurface(frame))
        self.anim_test_stay_down = anim

        anim = []
        for frame in ANIMATION_Stay_LEFT:
            anim.append(self.sprite_test.subsurface(frame))
        self.anim_test_stay_left = anim

        anim = []
        for frame in ANIMATION_Stay_LEFT_DOWN:
            anim.append(self.sprite_test.subsurface(frame))
        self.anim_test_stay_left_down = anim

        anim = []
        for frame in ANIMATION_Stay_LEFT_UP:
            anim.append(self.sprite_test.subsurface(frame))
        self.anim_test_stay_left_up = anim

        anim = []
        for frame in ANIMATION_Stay_RIGHT:
            anim.append(self.sprite_test.subsurface(frame))
        self.anim_test_stay_right = anim

        anim = []
        for frame in ANIMATION_Stay_RIGHT_DOWN:
            anim.append(self.sprite_test.subsurface(frame))
        self.anim_test_stay_right_down = anim

        anim = []
        for frame in ANIMATION_Stay_RIGHT_UP:
            anim.append(self.sprite_test.subsurface(frame))
        self.anim_test_stay_right_up = anim

        anim = []
        for frame in ANIMATION_Stay_UP:
            anim.append(self.sprite_test.subsurface(frame))
        self.anim_test_stay_up = anim

        # Анимация пехотинка
        # Передвжение
        anim = []
        for frame in ANIMATION_Footmen_DOWN:
            anim.append(self.sprite_Footman.subsurface(frame))
        self.anim_footmen_down = anim

        anim = []
        for frame in ANIMATION_Footmen_LEFT:
            anim.append(self.sprite_Footman.subsurface(frame))
        self.anim_footmen_left = anim

        anim = []
        for frame in ANIMATION_Footmen_LEFT_DOWN:
            anim.append(self.sprite_Footman.subsurface(frame))
        self.anim_test_left_down = anim

        anim = []
        for frame in ANIMATION_Footmen_LEFT_UP:
            anim.append(self.sprite_Footman.subsurface(frame))
        self.anim_footmen_left_up = anim

        anim = []
        for frame in ANIMATION_Footmen_RIGHT:
            anim.append(self.sprite_Footman.subsurface(frame))
        self.anim_footmen_right = anim

        anim = []
        for frame in ANIMATION_Footmen_RIGHT_DOWN:
            anim.append(self.sprite_Footman.subsurface(frame))
        self.anim_footmen_right_down = anim

        anim = []
        for frame in ANIMATION_Footmen_RIGHT_UP:
            anim.append(self.sprite_Footman.subsurface(frame))
        self.anim_footmen_right_up = anim

        anim = []
        for frame in ANIMATION_Footmen_UP:
            anim.append(self.sprite_Footman.subsurface(frame))
        self.anim_footmen_up = anim

        # стоять
        anim = []
        for frame in ANIMATION_Footmen_Stay_DOWN:
            anim.append(self.sprite_Footman.subsurface(frame))
        self.anim_footmen_stay_down = anim

        anim = []
        for frame in ANIMATION_Footmen_Stay_LEFT:
            anim.append(self.sprite_Footman.subsurface(frame))
        self.anim_footmen_stay_left = anim

        anim = []
        for frame in ANIMATION_Footmen_Stay_LEFT_DOWN:
            anim.append(self.sprite_Footman.subsurface(frame))
        self.anim_footmen_stay_left_down = anim

        anim = []
        for frame in ANIMATION_Footmen_Stay_LEFT_UP:
            anim.append(self.sprite_Footman.subsurface(frame))
        self.anim_footmen_stay_left_up = anim

        anim = []
        for frame in ANIMATION_Footmen_Stay_RIGHT:
            anim.append(self.sprite_Footman.subsurface(frame))
        self.anim_footmen_stay_right = anim

        anim = []
        for frame in ANIMATION_Footmen_Stay_RIGHT_DOWN:
            anim.append(self.sprite_Footman.subsurface(frame))
        self.anim_footmen_stay_right_down = anim

        anim = []
        for frame in ANIMATION_Footmen_Stay_RIGHT_UP:
            anim.append(self.sprite_Footman.subsurface(frame))
        self.anim_footmen_stay_right_up = anim

        anim = []
        for frame in ANIMATION_Footmen_Stay_UP:
            anim.append(self.sprite_Footman.subsurface(frame))
        self.anim_footmen_stay_up = anim

        # анимация бугая

        # передвижение
        anim = []
        for frame in ANIMATION_Grunt_DOWN:
            anim.append(self.sprite_Grunt.subsurface(frame))
        self.anim_grunt_down = anim

        anim = []
        for frame in ANIMATION_Grunt_LEFT:
            anim.append(self.sprite_Grunt.subsurface(frame))
        self.anim_grunt_left = anim

        anim = []
        for frame in ANIMATION_Grunt_LEFT_DOWN:
            anim.append(self.sprite_Grunt.subsurface(frame))
        self.anim_grunt_left_down = anim

        anim = []
        for frame in ANIMATION_Grunt_LEFT_UP:
            anim.append(self.sprite_Grunt.subsurface(frame))
        self.anim_grunt_left_up = anim

        anim = []
        for frame in ANIMATION_Grunt_RIGHT:
            anim.append(self.sprite_Grunt.subsurface(frame))
        self.anim_grunt_right = anim

        anim = []
        for frame in ANIMATION_Grunt_RIGHT_DOWN:
            anim.append(self.sprite_Grunt.subsurface(frame))
        self.anim_grunt_right_down = anim

        anim = []
        for frame in ANIMATION_Grunt_RIGHT_UP:
            anim.append(self.sprite_Grunt.subsurface(frame))
        self.anim_grunt_right_up = anim

        anim = []
        for frame in ANIMATION_Grunt_UP:
            anim.append(self.sprite_Grunt.subsurface(frame))
        self.anim_grunt_up = anim

        # стоять
        anim = []
        for frame in ANIMATION_Grunt_Stay_DOWN:
            anim.append(self.sprite_Grunt.subsurface(frame))
        self.anim_grunt_stay_down = anim

        anim = []
        for frame in ANIMATION_Grunt_Stay_LEFT:
            anim.append(self.sprite_Grunt.subsurface(frame))
        self.anim_grunt_stay_left = anim

        anim = []
        for frame in ANIMATION_Grunt_Stay_LEFT_DOWN:
            anim.append(self.sprite_Grunt.subsurface(frame))
        self.anim_grunt_stay_left_down = anim

        anim = []
        for frame in ANIMATION_Grunt_Stay_LEFT_UP:
            anim.append(self.sprite_Grunt.subsurface(frame))
        self.anim_grunt_stay_left_up = anim

        anim = []
        for frame in ANIMATION_Grunt_Stay_RIGHT:
            anim.append(self.sprite_Grunt.subsurface(frame))
        self.anim_grunt_stay_right = anim

        anim = []
        for frame in ANIMATION_Grunt_Stay_RIGHT_DOWN:
            anim.append(self.sprite_Grunt.subsurface(frame))
        self.anim_grunt_stay_right_down = anim

        anim = []
        for frame in ANIMATION_Grunt_Stay_RIGHT_UP:
            anim.append(self.sprite_Grunt.subsurface(frame))
        self.anim_grunt_stay_right_up = anim

        anim = []
        for frame in ANIMATION_Grunt_Stay_UP:
            anim.append(self.sprite_Grunt.subsurface(frame))
        self.anim_grunt_stay_up = anim
