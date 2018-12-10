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
                'options': ['foo', 'bar', 'baz'],
                'address': 'optionbox'
            },
            {
                'type': 'CheckBox',
                'text': 'boolean',
                'address': 'checkbox'
            },
            {
                'type': 'ProgressBar',
                'progress': 0.15
            }
        ]
    }
    app = Application(widgettree)
    def activate(event):
        label = app.frame.get_child('label')
        source = app.frame.get_child(event.source)
        if event.source == 'button':
            label.set_text('button pressed')
        elif event.source == 'optionbox':
            label.set_text('optionbox activated: ' + source.get_option())
        elif event.source == 'checkbox':
            label.set_text('checkbox toggled: ' + str(source._state))
    app.register_callback('activate', activate)
    app.run()
