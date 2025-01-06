from runge_kutta_solver import RungeKuttaSolver

class Trajectory:
    def __init__(self, velocity_field, t_start, t_end, h):
        """
        Инициализация расчетчика траекторий.
        :param velocity_field: Поле скоростей (объект класса VelocityField)
        :param t_start: Начальное время
        :param t_end: Конечное время
        :param h: Шаг интегрирования
        """
        self.velocity_field = velocity_field
        self.t_start = t_start
        self.t_end = t_end
        self.h = h

    def calculate(self, point):
        """
        Расчет траектории для заданной точки.
        :param point: Объект MaterialPoint
        :return: Траектория движения (список координат)
        """
        def system(t, coords):
            return self.velocity_field.velocity(t, coords)

        solver = RungeKuttaSolver(system, self.t_start, self.t_end, [point.x, point.y], self.h)
        return solver.solve()
