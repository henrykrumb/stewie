from .widget import Widget
from ..utils import strsize


class OptionBox(Widget):
    def __init__(self, options: list, parent=None, address=''):
        super().__init__(parent, address)
        self._options = options
        self._ptr = 0
        self._focusable = True
        self._keys = {
            'activate': ord(' '),
            'previous': ord('-'),
            'next': ord('+')
        }

    def _show(self, canvas):
        x, y, w, h = self._box
        if self._focused:
            canvas.draw_frame(self._box)
        if self._options:
            option = self._options[self._ptr]
            textw, texth = strsize(option)
            textx = int((w - textw) / 2)
            texty = int((h - texth) / 2)
            canvas.draw_text(option, (x + textx, y + texty))

    def _handle_key(self, key):
        if key == self._keys.get('previous', ord('-')):
            if self._ptr - 1 >= 0:
                self._ptr -= 1
            return
        elif key == self._keys.get('next', ord('+')):
            if self._ptr + 1 < len(self._options):
                self._ptr += 1
            return
        elif key == self._keys.get('activate', ord(' ')):
            self.send_event('optionbox_activate')
            return
        return key
