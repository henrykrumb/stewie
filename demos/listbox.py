from stewie.application import Application


def demo_listbox():
    widgettree = {
        'type': 'ListBox',
        'visible_entries': 5,
        'children': [
            {
                'type': 'Button',
                'text': 'BTN 1'
            },
            {
                'type': 'Button',
                'text': 'BTN 2'
            },
            {
                'type': 'Button',
                'text': 'BTN 3'
            },
            {
                'type': 'Button',
                'text': 'BTN 4'
            },
            {
                'type': 'Button',
                'text': 'BTN 5'
            },
            {
                'type': 'Button',
                'text': 'BTN 6'
            },
            {
                'type': 'Button',
                'text': 'BTN 7'
            },
            {
                'type': 'Button',
                'text': 'BTN 8'
            },
            {
                'type': 'Button',
                'text': 'BTN 9'
            }
        ]
    }
    Application(widgettree).run()
