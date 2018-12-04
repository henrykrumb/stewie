class ColorAttribute:
    def __init__(self):
        self._foreground = 1
        self._background = 0
        self._pattern = '#'

    @property
    def foreground(self):
        return self._foreground

    @foreground.setter
    def foreground(self, f):
        self._foreground = f

    @property
    def background(self):
        return self._background

    @background.setter
    def background(self, b):
        self._background = b

    @property
    def pattern(self):
        return self._pattern

    @pattern.setter
    def pattern(self, p):
        self._pattern = p
