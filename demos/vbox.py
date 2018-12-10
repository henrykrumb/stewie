from stewie.application import Application


def demo_vbox():
    widgettree = {
        'type': 'VBox',
        'children': [
            {
                'type': 'Label',
                'text': ''
            },
            {
                'type': 'Button',
                'text': 'button'
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
    def activate(event):
        label = app.frame.get_child('Label:1')
        source = app.frame.get_child(event.source)
        label.set_text(event.source)
        if event.source == 'Button:1':
            label.set_text('button pressed')
        elif event.source == 'OptionBox:1':
            label.set_text('optionbox activated: ' + source.get_option())
        elif event.source == 'CheckBox:1':
            label.set_text('checkbox toggled: ' + str(source._state))
    app.register_callback('activate', activate)
    app.run()
