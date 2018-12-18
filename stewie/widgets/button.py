from .widget import Widget
from ..utils import strsize


class Button(Widget):
    def __init__(self, text: str, parent=None, address=''):
        super().__init__(parent, address)
        self._text = text
        self._focusable = True

    def _show(self, canvas):
        x, y, w, h = self._box
        if self._focused:
            canvas.draw_frame(self._box, thick=True)
        else:
            canvas.draw_frame(self._box, thick=False, dashed=True)
        if self._text:
            textw, texth = strsize(self._text)
            textx = int((w - textw) / 2)
            texty = int((h - texth) / 2)
            canvas.draw_text(self._text, (x + textx, y + texty))

    def _handle_key(self, key):
        if key == ord(' '):
            self.send_event('activate', data=self)
            return
        return key
