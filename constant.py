# кол-во обновлений в секунду
FPS = 10

# пресет рабочего окна
WIN_WIDTH = 601
WIN_HEIGHT = 601

# блок цветов
WHITE = (255, 255, 255)
ORANGE = (255, 150, 100)
BLACK = (0, 0, 0)

acceleration = 1  # ускорение при нажатие
delta = 30  # изменение угла поворота
width = 600  # ширина рабочего пространства
height = 600  # высота рабочего пространствац
zoom = 5  # коэффицент приближения

# начальное положение сетки в глобальных координатах
x_global_coord_grid = 0
y_global_coord_grid = 0

# стартовая позиция
x_start_local = 75
y_start_local = 75

# количество строк и столбцов сетки
numbers_height_grid = 150
numbers_width_grid = 150

# радиус тестовой точки
test_radius_object = 5

# размеры танка
tank_width = 10  # 38 пикселей
tank_height = 12  # 43 пикселей

# это от сетки, которая скрыта (дичь какая-то, а мы это по серьезке писали)
x0 = 0
x = 0
y = 0
y0 = 0
h = 200
hl = 3  # numbers_height_grid // 3
wl = 3  # numbers_width_grid // 3

# коорды position_local
x1 = x0 - tank_width // 2
y1 = y0 - tank_height // 2

x2 = x0 + tank_width // 2
y2 = y0 - tank_height // 2

x3 = x0 - tank_width // 2
y3 = y0 + tank_height // 2

x4 = x0 + tank_width // 2
y4 = y0 + tank_height // 2
