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
    def button_activate(event):
        label = app.frame.get_child('label')
        label.set_text(event.source)
    app.register_callback('activate', button_activate)
    app.run()
