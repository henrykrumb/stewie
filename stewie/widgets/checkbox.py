from .widget import Widget
from ..utils import strsize


class CheckBox(Widget):
    def __init__(self, text: str, state=False, parent=None, address=''):
        super().__init__(parent, address)
        self._text = text
        self._state = state
        self._focusable = True

    def _show(self, canvas):
        x, y, w, h = self._box
        if self._focused:
            canvas.draw_frame(self._box)
        if self._text:
            text = '['
            text += 'x' if self._state else ' '
            text += '] ' + self._text
            textw, texth = strsize(text)
            textx = int((w - textw) / 2)
            texty = int((h - texth) / 2)
            canvas.draw_text(text, (x + textx, y + texty))

    def _handle_key(self, key):
        if key == ord(' '):
            self._state = not self._state
            self.send_event('activate', data=self._state)
            return
        return key
