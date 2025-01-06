class MaterialPoint:
    def __init__(self, x, y):
        """
        Инициализация материальной точки.
        :param x: Начальная координата x
        :param y: Начальная координата y
        """
        self.x = x
        self.y = y

    def position(self):
        """
        Возвращает текущее положение точки.
        """
        return self.x, self.y
