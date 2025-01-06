from core.material_point.velocity_field import VelocityField
from core.material_point.body import Body
from core.material_point.trajectory import Trajectory
from visualizations.visualizations import Visualization
import numpy as np

def main():
    # Заданные функции A(t) и B(t)
    A = lambda t: t
    B = lambda t: np.log(t)

    # Создаем поле скоростей
    velocity_field = VelocityField(A, B)

    # Создаем тело (окружность радиуса 4, центр в (0, 0))
    body = Body(4, 0, 0)
    points = body.points()

    # Расчет траекторий точек тела
    t_start, t_end, h = 0.1, 2, 0.01  # Временной интервал и шаг
    trajectory_calculator = Trajectory(velocity_field, t_start, t_end, h)
    trajectories = [trajectory_calculator.calculate(point) for point in points]

    # Построение графиков
    Visualization.plot_trajectories(trajectories)
    Visualization.plot_velocity_field(velocity_field, t=1, x_range=(-5, 5), y_range=(-5, 5))

if __name__ == "__main__":
    main()
