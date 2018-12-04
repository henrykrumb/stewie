def ellipsis(string, length):
    if not string:
        return ''
    if not isinstance(string, str):
        string = str(string)
    if len(string) <= length:
        return string
    if length <= 3:
        return string[:length-1] + '…'
    return string[:length-3] + '...'


def padstr(string, length, center=False):
    delta = length - len(string)
    if delta > 0:
        if center:
            prefix = delta // 2
            suffix = delta - prefix
            string = ' ' * prefix + string + ' ' * suffix
        else:
            string = string + ' ' * delta
    return string


def strsize(string):
    height = string.count('\n') + 1
    width = 0
    for line in string.splitlines():
        if len(line) > width:
            width = len(line)
    return width, height

