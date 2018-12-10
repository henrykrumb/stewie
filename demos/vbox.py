from stewie.application import Application


def demo_vbox():
    widgettree = {
        'type': 'VBox',
        'children': [
            {
                'type': 'Label',
                'text': '',
                'address': 'label'
            },
            {
                'type': 'Button',
                'text': 'button',
                'address': 'button'
            },
            {
                'type': 'OptionBox',
                'options': ['foo', 'bar', 'baz']
            },
            {
                'type': 'CheckBox',
                'text': 'boolean'
            },
            {
                'type': 'ProgressBar',
                'progress': 0.15
            }
        ]
    }
    app = Application(widgettree)
    
    app.run()
