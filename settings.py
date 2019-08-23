class Settings():
    # класс для хранения всех настроик игры
    def __init__(self):
        # параметры экрана
        self.screen_width = 800  # 1600
        self.screen_height = 600  # 900
        self.screen_color = (230, 230, 230)

        # параметры времени
        self.dt = 0
        # колличество циклов while = кадрам игры в секунду
        self.fps = 60
        # время жизни отдельного карда
        self.time = 180

        # параметры тестового персонажа
        self.test_speed = 4
        self.test_speed_2 = 2
        self.test_x = 0
        self.test_y = 0
        self.test_health = 100

        # цвет жизни персожажа
        self.health_colour_full = (0, 255, 0)
        self.health_colour_medium = (255, 255, 0)
        self.health_colour_low = (255, 0, 0)

        # параметры character
        self.test_speed = 4
        self.test_speed_2 = 2
        self.test_x = 0
        self.test_y = 0
        self.test_health = 100

        # параметры камеры
        self.camera_speed = 10

        # параметры поля травы
        self.tile_width = 32
        self.tile_length = 32
