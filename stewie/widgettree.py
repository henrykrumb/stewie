from .containers import *
from .widgets import *


# TODO automatically associate widget classes with their names
name2widget = {
    'CheckBox': CheckBox,
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
    :param parent: parent Container to which the widgets are added as children
    :param widgets: dictionary representing the widget tree
    """
    root = widgets
    try:
        roottype = root['type']
    except Exception:
        raise RuntimeError('root widget type has to be defined')
    options = {
        k: root[k] for k in root if k not in ('children', 'type')
    }
    rootwidget = name2widget.get(roottype)(**options)
    _walk_children(root, rootwidget)
    parent.add_child(rootwidget)
