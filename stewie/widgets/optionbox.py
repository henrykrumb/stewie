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

    def get_option(self):
        return self._options[self._ptr]

    def _show(self, canvas):
        x, y, w, h = self._box
        thick = self._focused
        canvas.draw_frame(self._box, thick=thick)
        if self._options:
            option = self._options[self._ptr]
            textw, texth = strsize(option)
            textx = int((w - textw) / 2)
            texty = int((h - texth) / 2)
            canvas.draw_text(option, (x + textx, y + texty))
            if self._ptr > 0:
                canvas.draw_frame((x, y, 5, h), thick=thick)
                canvas.draw_text('-', (x + 2, y + texty))
            if self._ptr < len(self._options) - 1:
                canvas.draw_frame((x + w - 5, y, 5, h), thick=thick)
                canvas.draw_text('+', (x + w - 3, y + texty))

    def _handle_key(self, key):
        if key == self._keys.get('previous', ord('-')):
            if self._ptr - 1 >= 0:
                self._ptr -= 1
                self.send_event('change', data=self._options[self._ptr])
            return
        elif key == self._keys.get('next', ord('+')):
            if self._ptr + 1 < len(self._options):
                self._ptr += 1
                self.send_event('change', data=self._options[self._ptr])
            return
        elif key == self._keys.get('activate', ord(' ')):
            self.send_event('activate')
            return
        return key
