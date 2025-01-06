import numpy as np
from core.material_point import MaterialPoint

class Body:
    def __init__(self, radius, center_x, center_y):
        """
        Создание тела (окружности).
        :param radius: Радиус круга
        :param center_x: Центр окружности (x)
        :param center_y: Центр окружности (y)
        """
        self.radius = radius
        self.center_x = center_x
        self.center_y = center_y

    def points(self, num_points=50):
        """
        Генерация точки на окружности.
        :param num_points: Количество точек для разбиения
        :return: Список объектов MaterialPoint
        """
        angles = np.linspace(0, np.pi / 2, num_points)  # Первая четверть
        return [MaterialPoint(self.center_x + self.radius * np.cos(angle),
                              self.center_y + self.radius * np.sin(angle)) for angle in angles]