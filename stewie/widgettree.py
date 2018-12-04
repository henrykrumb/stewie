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


def walk_children(node, nodewidget):
    children = node.get('children', [])
    for child in children:
        options = {k: child[k] for k in child if k not in ('children', 'type')}
        childwidget = name2widget.get(child['type'])(**options)
        walk_children(child, childwidget)
        nodewidget.add_child(childwidget)


def build_widget_tree(parent: Container, widgets: dict):
    root = widgets
    rootwidget = name2widget.get(root['type'])()
    walk_children(root, rootwidget)
    parent.add_child(rootwidget)
