from .boxattribute import BoxAttribute
from .sizeattribute import SizeAttribute


class WidgetStyle:
    def __init__(self):
        self._padding = BoxAttribute(0, 0, 0, 0)
        self._margin = BoxAttribute(0, 0, 0, 0)
        self._width = SizeAttribute()
        self._height = SizeAttribute()

    @property
    def padding(self):
        return self._padding

    @padding.setter
    def padding(self, p):
        if type(p) == BoxAttribute:
            self._padding = p
        else:
            raise RuntimeError('wrong type passed for padding ' + str(type(p)))

    @property
    def margin(self):
        return self._margin

    @margin.setter
    def marging(self, m):
        if type(m) == BoxAttribute:
            self._margin = m
        else:
            raise RuntimeError('wrong type passed for margin ' + str(type(m)))


class ContainerStyle(WidgetStyle):
    def __init__(self):
        super(WidgetStyle).__init__()
