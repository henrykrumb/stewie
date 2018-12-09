from stewie.application import Application


def demo_listbox():
    buttons = []
    for i in range(7):
        button = {
            'type': 'Button',
            'text': 'BTN ' + str(i),
            'address': 'BTN_' + str(i)
        }
        buttons.append(button)
    widgettree = {
        'type': 'ListBox',
        'visible_entries': 5,
        'children': buttons
    }
    Application(widgettree).run()
