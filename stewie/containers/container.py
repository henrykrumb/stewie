from ..styles import ContainerStyle
from ..widgets import Widget


class Container(Widget):
    def __init__(self, parent=None, address=''):
        super().__init__(parent, address)
        self._focused_child = 0
        self._focusable = True
        self._children = []
        self._style = ContainerStyle()

    def get_child(self, address, recursive=True):
        for child in self._children:
            if child.address == address:
                return child
            if recursive:
                if hasattr(child, 'get_child'):
                    c = child.get_child(address, recursive)
                    if c is not None:
                        return c
        return None

    def _add_child(self, widget):
        return True

    def add_child(self, widget):
        if self._add_child(widget):
            widget._parent = self
            self._children.append(widget)
            self.pack()
            return True
        return False

    def _remove_child(self, widget):
        return True

    def remove_child(self, widget):
        status = False
        for child in self._children:
            if child.address == widget.address:
                if self._remove_child(child):
                    self._children.remove(child)
                    status = True
                    break
        if status:
            self.pack()
        return status

    def _get_focusable_child_indices(self):
        indices = []
        for c in range(len(self._children)):
            child = self._children[c]
            if child._focusable:
                indices.append(c)
        return indices

    def _pack(self):
        return

    def pack(self):
        if self._focused_child >= len(self._children):
            self._focused_child = len(self._children) - 1
        self._pack()
        for c in range(len(self._children)):
            child = self._children[c]
            child._focused = (c == self._focused_child)
            child.pack()

    def _show(self, canvas):
        return

    def show(self, canvas):
        self._show(canvas)
        for child in self._children:
            if child._visible:
                child.show(canvas)

    def _handle_key(self, key):
        return key

    def handle_key(self, key):
        k = self._handle_key(key)
        for c in range(len(self._children)):
            child = self._children[c]
            child._focused = (c == self._focused_child)
        if k is None:
            return
        if 0 <= self._focused_child < len(self._children):
            child = self._children[self._focused_child]
            if child.handle_key(key) is None:
                return
        return key

    def __iter__(self):
        return self._children.__iter__()

    def __len__(self):
        return len(self._children)
