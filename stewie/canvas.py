class Canvas:
    def __init__(self, screen):
        self._screen = screen

    def draw_text(self, text: str, position: tuple):
        """
        """
        x, y = position
        try:
            self._screen.addstr(y, x, text)
        except Exception:
            pass

    def draw_char(self, char: str, position: tuple):
        """
        """
        x, y = position
        try:
            self._screen.addnstr(y, x, char, 1)
        except Exception:
            pass

    def draw_frame(self, frame: tuple, style=None):
        """
        Draw a rectangular frame.

        :param frame: tuple of (x, y, width, height)
        """
        # TODO move definitions to separate module
        UNICODE = True
        if UNICODE:
            HLINE = '\u2500'
            VLINE = '\u2502'
            ULCORNER = '\u250C'
            URCORNER = '\u2510'
            LLCORNER = '\u2514'
            LRCORNER = '\u2518'
        else:
            HLINE = '#'
            VLINE = '#'
            ULCORNER = '#'
            URCORNER = '#'
            LLCORNER = '#'
            LRCORNER = '#'
        x, y, w, h = frame
        for by in range(1, h - 1):
            self.draw_char(VLINE, (x, y + by))
            self.draw_char(VLINE, (x + w - 1, y + by))
        for bx in range(1, w - 1):
            self.draw_char(HLINE, (x + bx, y))
            self.draw_char(HLINE, (x + bx, y + h - 1))
        self.draw_char(ULCORNER, (x, y))
        self.draw_char(URCORNER, (x + w - 1, y))
        self.draw_char(LLCORNER, (x, y + h - 1))
        self.draw_char(LRCORNER, (x + w - 1, y + h - 1))

    def draw_box(self, box: tuple, style=None):
        """
        Draw a rectangular box.

        :param box: tuple of (x, y, width, height)
        """
        x, y, w, h = box
        for by in range(h):
            for bx in range(w):
                self.draw_char('#', (x + bx, y + by))
