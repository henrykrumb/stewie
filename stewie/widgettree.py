from .containers import *
from .widgets import *


name2widget = {
    'Frame': Frame,
    'HBox': HBox,
    'ListBox': ListBox,
    'VBox': VBox,
    'Button': Button,
    'Label': Label,
    'OptionBox': OptionBox,
    'ProgressBar': ProgressBar
}


def _walk_children(node, nodewidget):
    children = node.get('children', [])
    for child in children:
        options = {
            k: child[k] for k in child if k not in ('children', 'type')
        }
        try:
            childtype = child['type']
        except Exception:
            raise RuntimeError('child widget type has to be defined')
        childwidget = name2widget.get(childtype)(**options)
        _walk_children(child, childwidget)
        nodewidget.add_child(childwidget)


def build_widget_tree(parent: Container, widgets: dict):
    """
    :param parent: the tree is added to the parent Container
    :param widgets: dictionary representing the widget tree
    """
    root = widgets
    try:
        roottype = root['type']
    except:
        raise RuntimeError('root widget type has to be defined')
    rootwidget = name2widget.get(root['type'])()
    _walk_children(root, rootwidget)
    parent.add_child(rootwidget)
