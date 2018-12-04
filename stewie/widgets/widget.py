from ..events import EventNode
from ..styles import WidgetStyle


class Widget(EventNode):
    def __init__(self, parent=None, address=''):
        super().__init__(parent, address)
        self._style = WidgetStyle()
        self._box = (0, 0, -1, -1)
        self._focusable = False
        self._focused = False
        self._visible = True

    def _handle_key(self, key):
        return key

    def handle_key(self, key):
        return self._handle_key(key)

    def pack(self):
        return

    def _show(self, canvas):
        return

    def show(self, canvas):
        self._show(canvas)
