from .container import Container


class Frame(Container):
    def __init__(self, box, parent, address='frame'):
        super().__init__(parent, address)
        self._box = box

    def add_child(self, widget):
        if len(self._children) > 0:
            raise RuntimeError('Frames can only have one child')
        super().add_child(widget)

    def _pack(self):
        if self._children:
            self._children[0]._box = self._box
