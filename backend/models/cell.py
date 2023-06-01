class Cell:

    FULL  = '■'
    EMPTY = '✕'
    UNDEF = '.'

    def __init__(self, x, y, value=UNDEF):
        self._x = x
        self._y = y
        self._value = value

    def get_x(self):
        return self._x

    def get_y(self):
        return self._y

    def get_value(self):
        return self._value

    def set_value(self, value):
        self._value = value

    def change_value(self):
        value = self._value
        if value == self.UNDEF:
            value = self.EMPTY
        elif value == self.EMPTY:
            value = self.FULL
        else:
            value = self.UNDEF
        self._value = value

    def __str__(self):
        return self._value
