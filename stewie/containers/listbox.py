import curses

from .container import Container


class ListBox(Container):
    def __init__(self, visible_entries: int, parent=None, address=''):
        super().__init__(parent, address)
        self._visible_entries = visible_entries
        self._scroll = 0
        self._keys = {
            'up': curses.KEY_UP,
            'down': curses.KEY_DOWN
        }

    def _add_child(self, child):
        if not child._focusable:
            raise RuntimeError('ListBox children must be focusable')
        return True

    def _remove_child(self, child):
        return True

    def _pack(self):
        x, y, w, h = self._box
        if not self._children:
            return
        childheight = h / len(self._children)
        for c in range(len(self._children)):
            cx = x
            cy = round(c * childheight)
            cw = w
            ch = round(childheight)
            self._children[c]._box = (cx, cy, cw, ch)

    def _show(self, canvas):
        return

    def show(self, canvas):
        """
        Override Container's show method so that only a portion of the
        children is displayed.
        """
        self._show(canvas)
        start = self._scroll
        end = start + self._visible_entries
        if end > len(self._children):
            end = len(self._children)
        for c in range(start, end):
            child = self._children[c]
            if child._visible:
                child.show(canvas)

    def _handle_key(self, key):
        if key == self._keys.get('down', curses.KEY_DOWN):
            self._focused_child += 1
            if self._focused_child > self._scroll + self._visible_entries:
                self._scroll += 1
            return
        if key == self._keys.get('up', curses.KEY_UP):
            self._focused_child -= 1
            if self._focused_child < self._scroll + self._visible_entries:
                self._scroll -= 1
            return
        return key
