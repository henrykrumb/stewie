from stewie.application import Application


def demo_vbox():
    widgettree = {
        'type': 'VBox',
        'children': [
            {
                'type': 'Button',
                'text': 'Hello'
            },
            {
                'type': 'Button',
                'text': 'World'
            },
            {
                'type': 'Button',
                'text': 'Foo'
            },
            {
                'type': 'OptionBox',
                'options': ['foo', 'bar', 'baz']
            },
            {
                'type': 'ProgressBar',
                'progress': 0.15
            }
        ]
    }
    Application(widgettree).run()
