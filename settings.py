class Settings(object):
    # класс для хранения всех настроик игры
    def __init__(self):
        # параметры экрана
        self.screen_width = 1600  # 1600
        self.screen_height = 900  # 900
        self.screen_color = (230, 230, 230)

        # параметры времени
        self.dt = 0
        # колличество циклов while = кадрам игры в секунду
        self.fps = 60
        # время жизни отдельного карда
        self.time = 360

        # параметры тестового персонажа
        self.test_speed = 4
        self.test_speed_2 = 2
        self.test_x = 40
        self.test_y = 40
        self.test_health = 100

        # цвет жизни персожажа
        self.health_colour_full = (0, 255, 0)
        self.health_colour_medium = (255, 255, 0)
        self.health_colour_low = (255, 0, 0)

        # параметры character
        # параметры footmen
        self.footmen_speed = 4
        self.footmen_speed_2 = 2
        self.footmen_x = 0
        self.footmen_y = 0
        self.footmen_health = 100

        # параметры камеры
        self.camera_speed = 10

        # параметры поля травы
        self.tile_width = 32
        self.tile_length = 32

        self.value = [['name', 'ширина', 'высота', 'скорость', 'скоростьДИАГ', 'здоровье','ширинаЗДОР',''],
                      ['test       ', 55, 70, 6, 4, 30,100],
                      ['footmen    ', 55, 70, 4, 3, 100,100],
                      ['grunt      ', 1, 100, 100, 10, 100,100]]

        self.value_healf = [['']]
