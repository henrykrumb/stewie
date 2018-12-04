from .widget import Widget
from ..utils import strsize


class Label(Widget):
    def __init__(self, text: str, parent=None, address=''):
        super().__init__(parent, address)
        self._text = text

    def _show(self, canvas):
        x, y, w, h = self._box
        if self._text:
            textw, texth = strsize(self._text)
            textx = round((w - textw) / 2)
            texty = round((h - texth) / 2)
            canvas.draw_text(self._text, (x + textx, y + texty))
