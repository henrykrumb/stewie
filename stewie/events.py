from queue import Queue


_callbacks = {}
_queue = Queue()


def send_event(event_type, data=None, source=None, sink=None):
    """
    Throws a new event onto the event bus. Events can be sent from any source,
    but they can only be received by EventNodes.

    :param event_type:
    :param data: event payload
    :param source: where the event comes from
    :param sink: event destination
    """
    event = None
    if isinstance(event_type, Event):
        event = event_type
    else:
        event = Event(event_type, data, source, sink)
    _queue.put(event)


def dispatch_events():
    """
    Distribute all events in the queue among the listening receivers.
    Called inside the mainloop.
    """
    while not _queue.empty():
        event = _queue.get()
        if event.type in _callbacks:
            # directed events
            if event.sink:
                if event.sink in _callbacks[event.type]:
                    for callback in _callbacks[event.type][event.sink]:
                        callback(event)
            # broadcast events
            else:
                for address in _callbacks[event.type]:
                    for callback in _callbacks[event.type][address]:
                        callback(event)


class Event:
    """
    Events can be imagined as packages which contain data in any form.

    :param event_type: identification string
    :param data: any kind of payload data
    :param source: event origin
    :param sink: event destination
    """
    def __init__(self, event_type, data=None, source=None, sink=None):
        self.type = event_type
        self.data = data
        self.source = source
        self.sink = sink

    def __str__(self):
        s = '<Event type=' + self.type
        if self.source:
            s += ' src=' + self.source
        if self.data:
            s += ' data=' + self.data
        if self.sink:
            s += ' sink=' + self.sink
        s += '>'
        return s


class EventNode:
    """
    EventNode objects process events sent from arbitrary sources.

    :param address: address string
    """
    def __init__(self, parent=None, address=''):
        self.parent = parent
        self.address = address
        if not address:
            self.address = ''
            if parent:
                self.address = parent.address + '.'
            self.address += self.__class__.__name__ + ':' + str(id(self))
        # register all '@on'-decorated methods
        for member in dir(self):
            if callable(getattr(self, member)):
                func = getattr(self, member)
                if hasattr(func, 'register'):
                    _register_callback(self, func.event_type, func)

    def send_event(self, event_type, data=None, sink=None):
        """
        Wrapper method for send_event in event module.
        Reduces number of parameters needed by inserting source address.

        :param event_type:
        :param data: event payload
        :param sink: event destination
        """
        send_event(event_type, data, self.address, sink)

    def __str__(self):
        return '<EventNode address={}>'.format(self.address)


def _register_callback(node: EventNode, event_type, func):
    """
    :param node: EventNode object
    :param event_type:
    :param func: callback method of node
    """
    if event_type not in _callbacks:
        _callbacks[event_type] = {}
    if node.address not in _callbacks[event_type]:
        _callbacks[event_type][node.address] = []
    _callbacks[event_type][node.address].append(func)


def on(event_type):
    """
    Decorator for EventNodes.
    Subscribes a method to an event type.

    Example::

        class Listener(EventNode):
            ...
            @on('listener.hello')
            def hello(self, event):
                self.do_something(event.data)
            ...

    :param event_type:
    """
    def decorator(func):
        from functools import wraps

        @wraps(func)
        def decorate(*args, **kwargs):
            return func(*args, **kwargs)

        decorate.register = True
        decorate.event_type = event_type
        return decorate
    return decorator
