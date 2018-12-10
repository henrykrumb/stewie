import curses

from .container import Container


class VBox(Container):
    def __init__(self, parent=None, address=''):
        super().__init__(parent, address)
        self._keys = {
            'up': curses.KEY_UP,
            'down': curses.KEY_DOWN
        }

    def _pack(self):
        x, y, w, h = self._box
        if not self._children:
            return
        childheight = int(h / len(self._children))
        for c in range(len(self._children)):
            cx = x
            cy = int(c * childheight)
            cw = w
            ch = int(childheight)
            self._children[c]._box = (cx, cy, cw, ch)
        indices = self._get_focusable_child_indices()
        if self._focused_child in indices:
            index = indices.index(self._focused_child)
        else:
            index = 0
        if len(indices) > 0:
            self._focused_child = indices[index]

    def _show(self, canvas):
        return

    def _handle_key(self, key):
        if self._focused_child < 0:
            return key
        indices = self._get_focusable_child_indices()
        index = indices.index(self._focused_child)
        if key == self._keys.get('down', curses.KEY_DOWN):
            index += 1
            if index >= len(indices):
                index = 0
            self._focused_child = indices[index]
            return
        if key == self._keys.get('up', curses.KEY_UP):
            index -= 1
            if index < 0:
                index = len(indices) - 1
            self._focused_child = indices[index]
            return
        return key
