import curses

from .container import Container


class HBox(Container):
    def __init__(self, parent=None, address=''):
        super().__init__(parent, address)
        self._keys = {
            'left': curses.KEY_LEFT,
            'right': curses.KEY_RIGHT
        }

    def _pack(self):
        x, y, w, h = self._box
        if not self._children:
            return
        childwidth = w / len(self._children)
        for c in range(len(self._children)):
            cx = int(c * childwidth)
            cy = y
            cw = int(childwidth)
            ch = h
            self._children[c]._box = (cx, cy, cw, ch)

    def _handle_key(self, key):
        indices = self._get_focusable_child_indices()
        index = indices.index(self._focused_child)
        if key == self._keys.get('right', curses.KEY_RIGHT):
            index += 1
            if index >= len(indices):
                index = 0
            self._focused_child = indices[index]
            return
        if key == self._keys.get('left', curses.KEY_LEFT):
            index -= 1
            if index < 0:
                index = len(indices) - 1
            self._focused_child = indices[index]
            return
        return key
