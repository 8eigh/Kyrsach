import numpy as np

class VelocityField:
    def __init__(self, a_func, b_func):
        self.a_func = a_func
        self.b_func = b_func

    def velocity(self, t, x):
        return np.array([-self.a_func(t) * x[0], self.b_func(t) * x[1]])

    def field(self, grid_x, grid_y, t):
        u = np.zeros_like(grid_x)
        v = np.zeros_like(grid_y)
        for i in range(grid_x.shape[0]):
            for j in range(grid_x.shape[1]):
                velocity = self.velocity(t, [grid_x[i, j], grid_y[i, j]])
                u[i, j], v[i, j] = velocity
        return u, v
