import curses

import traceback
import sys

from .canvas import Canvas
from .containers import Frame
from .events import dispatch_events
from .keyboard import curses_keycode
from .widgettree import build_widget_tree


class Application:
    def __init__(self, widgets: dict):
        self._screen = curses.initscr()
        try:
            self._canvas = Canvas(self._screen)
            self._frame = Frame((0, 0, curses.COLS, curses.LINES), self)
            build_widget_tree(self._frame, widgets)
        except Exception:
            self.exit()
            exc_info = sys.exc_info()
            traceback.print_exception(*exc_info)
            exit()

    def run(self):
        try:
            self._frame.pack()
            curses.noecho()
            curses.cbreak()
            curses.curs_set(False)
            self._screen.keypad(True)
            height, width = self._screen.getmaxyx()
            quit = False
            while not quit:
                lines, cols = self._screen.getmaxyx()
                if width != cols or height != lines:
                    width = cols
                    height = lines
                    self._frame._box = (0, 0, cols, lines)
                    self._frame.pack()
                self._screen.clear()
                self._frame.show(self._canvas)
                c = self._screen.getch()
                if c == curses_keycode('q'):
                    quit = True
                self._frame.handle_key(c)
                dispatch_events()
            self.exit()
        except Exception:
            self.exit()
            exc_info = sys.exc_info()
            traceback.print_exception(*exc_info)

    def exit(self):
        curses.curs_set(True)
        curses.nocbreak()
        curses.echo()
        self._screen.keypad(False)
        curses.endwin()
