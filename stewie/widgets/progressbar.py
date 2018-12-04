from .widget import Widget


class ProgressBar(Widget):
    def __init__(self, parent=None, address=''):
        super().__init__(parent, address)
        self._progress = 0

    @property
    def progress(self):
        return self._progress

    @progress.setter
    def progress(self, progress: float):
        if 0 <= progress <= 1:
            self._progress = progress
        else:
            raise RuntimeError('progress value not in interval [0, 1]')

    def show(self, canvas):
        x, y, w, h = self._box
        # TODO vertical/horizontal option
        # TODO reverse option
        canvas.draw_box((x, y, w, h))
