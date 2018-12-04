class SizeAttribute:
    def __init__(self, min_size=1, max_size=-1, prefered_size=-1):
        self._min_size = min_size
        self._max_size = max_size
        self._prefered_size = prefered_size
        if self._prefered_size == -1:
            self._prefered_size = max_size
