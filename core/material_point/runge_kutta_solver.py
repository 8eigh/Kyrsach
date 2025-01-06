import numpy as np

class RungeKuttaSolver:
    def __init__(self, f, t_start, t_end, y0, h):
        self.f = f  # Система ОДУ
        self.t_start = t_start
        self.t_end = t_end
        self.y0 = y0
        self.h = h

    def solve(self):
        t = self.t_start
        y = np.array(self.y0)
        trajectory = [(t, *y)]

        while t < self.t_end:
            k1 = self.h * np.array(self.f(t, y))
            k2 = self.h * np.array(self.f(t + self.h / 2, y + k1 / 2))
            y += k2
            t += self.h
            trajectory.append((t, *y))

        return trajectory