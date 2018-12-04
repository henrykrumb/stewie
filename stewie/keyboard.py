import curses


def curses_keycode(s):
    if s.isalnum():
        return ord(s)
    keys = {
        'up': curses.KEY_UP,
        'down': curses.KEY_DOWN,
        'left': curses.KEY_LEFT,
        'right': curses.KEY_RIGHT,
        'space': ord(' ')
    }
    return keys.get(s, None)