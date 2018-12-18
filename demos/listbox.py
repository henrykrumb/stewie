from stewie.application import Application
from stewie.widgettree import build_widget_tree


def make_list_item(parent, i):
    item = {
        'type': 'VBox',
        'children': [
            {
                'type': 'Label',
                'text': 'LBL' + str(i)
            },
            {
                'type': 'OptionBox',
                'options': ['first option', 'second option', 'third option']
            }
        ]
    }
    return build_widget_tree(parent, item)

def demo_listbox():
    widgettree = {
        'type': 'ListBox',
        'address': 'lbox',
        'visible_entries': 4
    }
    
    app = Application(widgettree)
    for i in range(10):
        make_list_item(app.frame.get_child('lbox'), i)
    app.frame.pack()
    app.run()
