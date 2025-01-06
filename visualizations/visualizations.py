import matplotlib.pyplot as plt
import numpy as np

class Visualization:
    @staticmethod
    def plot_trajectories(trajectories, ax=None):
        if ax is None:
            fig, ax = plt.subplots()
        for trajectory in trajectories:
            points = np.array(trajectory)
            ax.plot(points[:, 1], points[:, 2], label=f"Start: {points[0, 1:3]}")
        ax.legend()
        ax.set_title('Траектории движения')
        plt.show()

    @staticmethod
    def plot_velocity_field(velocity_field, t, x_range, y_range):
        x = np.linspace(*x_range, 20)
        y = np.linspace(*y_range, 20)
        X, Y = np.meshgrid(x, y)
        U, V = velocity_field.field(X, Y, t)

        plt.figure(figsize=(10, 6))
        plt.quiver(X, Y, U, V, color='blue')
        plt.title(f'Поле скоростей (время {t})')
        plt.xlabel('x1')
        plt.ylabel('x2')
        plt.grid()
        plt.show()