class Camera():
    def __init__(self, setting):
        # инициализируем настройки
        self.setting = setting

        self.x = 0
        self.y = 0

        self.direction = 'no'

    def move(self, characrets, test):

        if self.direction == 'right':
            self.x -= self.setting.camera_speed
            test.rect.x -= self.setting.camera_speed
            for characret in characrets:
                characret.rect.x -= self.setting.camera_speed
        if self.direction == 'left':
            self.x += self.setting.camera_speed
            test.rect.x += self.setting.camera_speed
            for characret in characrets:
                characret.rect.x += self.setting.camera_speed
        if self.direction == 'up':
            self.y += self.setting.camera_speed
            test.rect.y += self.setting.camera_speed
            for characret in characrets:
                characret.rect.y += self.setting.camera_speed
        if self.direction == 'down':
            self.y -= self.setting.camera_speed
            test.rect.y -= self.setting.camera_speed
            for characret in characrets:
                characret.rect.y -= self.setting.camera_speed

# def camera(characters):
#     for i in characters:

# WIN_WIDTH = 800 #Ширина создаваемого окна
# WIN_HEIGHT = 640 # Высота
#
# class Camera(objtec):
#    def __init__(self, camera_func, width, height):
#        self.camera_func = camera_func
#        self.state = Rect(0, 0, width, height)
#
#    def apply(self, target):
#        return target.rect.move(self.state.topleft)
#
#    def update(self, target):
#        self.state = self.camera_func(self.state, target.rect)
#
#
# def camera_configure(camera, target_rect):
#    l, t, _, _ = target_rect
#    _, _, w, h = camera
#    l, t = -l + WIN_WIDTH / 2, -t + WIN_HEIGHT / 2
#
#    l = min(0, l)  # Не движемся дальше левой границы
#    l = max(-(camera.width - WIN_WIDTH), l)  # Не движемся дальше правой границы
#    t = max(-(camera.height - WIN_HEIGHT), t)  # Не движемся дальше нижней границы
#    t = min(0, t)  # Не движемся дальше верхней границы
#
#    return Rect(l, t, w, h)
