from .boxattribute import BoxAttribute
from .sizeattribute import SizeAttribute


class BoxStyle:
    def __init__(self):
        self._width = SizeAttribute()
        self._height = SizeAttribute()
        self._border = BoxAttribute()
