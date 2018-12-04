from .widget import Widget


class ProgressBar(Widget):
    _progress = 0

    def __init__(self, progress=0, parent=None, address=''):
        super().__init__(parent, address)
        self.progress = progress

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
        w_fill = int(w * self.progress)
        canvas.draw_box((x, y, w_fill, h))
        p = '{}%'.format(int(self.progress * 100))
        canvas.draw_text(p, (x + int(w / 2), y + int(h / 2)))
