import math



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

    def draw_frame(self, frame: tuple, style=None, thick=False, dashed=False):
        """
        Draw a rectangular frame.

        :param frame: tuple of (x, y, width, height)
        """
        # TODO move definitions to separate module
        # TODO make unicode configurable or better: dependent on unicode
        # support in terminal
        UNICODE = True
        if UNICODE:
            if thick:
                VLINE = '\u2588'
                UHLINE = '\u2580'
                LHLINE = '\u2584'
                ULCORNER = '\u2588'
                URCORNER = '\u2588'
                LLCORNER = '\u2588'
                LRCORNER = '\u2588'
            else:
                VLINE = '\u2502'
                UHLINE = '\u2500'
                LHLINE = '\u2500'
                ULCORNER = '\u250C'
                URCORNER = '\u2510'
                LLCORNER = '\u2514'
                LRCORNER = '\u2518'
        else:
            if thick:
                VLINE = '#'
                UHLINE = '#'
                LHLINE = '#'
                ULCORNER = '#'
                URCORNER = '#'
                LLCORNER = '#'
                LRCORNER = '#'
            else:
                VLINE = '|'
                UHLINE = '-'
                LHLINE = '_'
                ULCORNER = '.'
                URCORNER = '.'
                LLCORNER = '|'
                LRCORNER = '|'
        x, y, w, h = frame
        for by in range(1, h - 1):
            if dashed and by % 2 == 1:
                continue
            self.draw_char(VLINE, (x, y + by))
            self.draw_char(VLINE, (x + w - 1, y + by))
        for bx in range(1, w - 1):
            if dashed and bx % 2 == 1:
                continue
            self.draw_char(UHLINE, (x + bx, y))
            self.draw_char(LHLINE, (x + bx, y + h - 1))
        self.draw_char(ULCORNER, (x, y))
        self.draw_char(URCORNER, (x + w - 1, y))
        self.draw_char(LLCORNER, (x, y + h - 1))
        self.draw_char(LRCORNER, (x + w - 1, y + h - 1))

    def draw_box(self, box: tuple, character='\u2588', style=None):
        """
        Draw a rectangular box.

        :param box: tuple of (x, y, width, height)
        """
        x, y, w, h = box
        UNICODE = True
        BOX = character if UNICODE else '#'
        for by in range(h):
            for bx in range(w):
                self.draw_char(BOX, (x + bx, y + by))

    def draw_scrollbar(self, box: tuple, page: int, pages: int):
        x, y, w, h = box
        UNICODE = True
        if UNICODE:
            ARROW_UP = '\u25B2'
            ARROW_DOWN = '\u25BC'
            HANDLE = '\u2591'
        else:
            ARROW_UP = '^'
            ARROW_DOWN = 'v'
            HANDLE = '#'
        handle_h = math.ceil((h - 3) / pages)
        handle_y = y + 1 + int(page * handle_h)
        self.draw_box((x, handle_y, w, handle_h), HANDLE)
        self.draw_char(ARROW_UP, (x, y))
        self.draw_char(ARROW_DOWN, (x, y + h - 1))
