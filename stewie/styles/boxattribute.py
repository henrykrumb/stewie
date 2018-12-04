class BoxAttribute:
    def __init__(self, top=None, bottom=None, left=None, right=None):
        self._top = top
        self._bottom = bottom
        self._left = left
        self._right = right

    @property
    def top(self):
        return self._top

    @top.setter
    def top(self, t):
        self._top = t

    @property
    def bottom(self):
        return self._bottom

    @bottom.setter
    def bottom(self, b):
        self._bottom = b

    @property
    def left(self):
        return self._left

    @left.setter
    def left(self, l):
        self._left = l

    @property
    def right(self):
        return self._right

    @right.setter
    def right(self, r):
        self._right = r
