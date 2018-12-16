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
        if not self._children:
            return
        x, y, w, h = self._box
        childheight = int(h / self._visible_entries)
        for child in self._children:
            child._visible = False
        start = self._scroll
        end = start + self._visible_entries
        if end > len(self._children):
            end = len(self._children)
        for c in range(start, end):
            cx = x
            cy = int((c - start) * childheight)
            cw = w
            ch = int(childheight)
            self._children[c]._visible = True
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
            if self._focused_child >= len(self._children):
                self._focused_child = len(self._children) - 1
            key = None
        elif key == self._keys.get('up', curses.KEY_UP):
            self._focused_child -= 1
            if self._focused_child < 0:
                self._focused_child = 0
            key = None
        if self._focused_child - self._scroll >= self._visible_entries:
            self._scroll += self._visible_entries
        elif self._focused_child - self._scroll < 0:
            self._scroll -= self._visible_entries
        if key is None:
            self.pack()
        return key
