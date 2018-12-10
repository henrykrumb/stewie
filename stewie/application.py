import curses

import traceback
import signal
import sys

from .canvas import Canvas
from .containers import Frame
from .events import dispatch_events, EventNode
from .keyboard import curses_keycode
from .widgettree import build_widget_tree


class Application(EventNode):
    def __init__(self, widgets: dict):
        super().__init__(None, 'application')
        signal.signal(signal.SIGINT, self._exit_signal_handler)
        signal.signal(signal.SIGTERM, self._exit_signal_handler)

        self._screen = curses.initscr()
        try:
            self._canvas = Canvas(self._screen)
            self.frame = Frame((0, 0, curses.COLS, curses.LINES), self)
            build_widget_tree(self.frame, widgets)
        except Exception:
            self.exit()
            exc_info = sys.exc_info()
            traceback.print_exception(*exc_info)
            exit()

    def _exit_signal_handler(self, signum, frame):
        self.exit()
        exit()

    def run(self, thread=None):
        try:
            self.frame.pack()
            curses.noecho()
            curses.cbreak()
            curses.curs_set(False)
            self._screen.keypad(True)
            height, width = self._screen.getmaxyx()
            quit = False
            while not quit:
                if thread and thread.is_stop_requested():
                    quit = True
                lines, cols = self._screen.getmaxyx()
                if width != cols or height != lines:
                    width = cols
                    height = lines
                    self.frame._box = (0, 0, cols, lines)
                    self.frame.pack()
                self._screen.erase()
                self.frame.show(self._canvas)
                c = self._screen.getch()
                if c == curses_keycode('q'):
                    quit = True
                self.frame.handle_key(c)
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
