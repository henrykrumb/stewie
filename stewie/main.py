import argparse
import json
import logging

from .__version__ import __version__
from .application import Application


def main():
    logger = logging.getLogger('stewie')
    handler = logging.FileHandler('stewie.log')
    logger.addHandler(handler)
    formatter = logging.Formatter('%(asctime)s %(name)s [%(levelname)s] %(message)s')
    handler.setFormatter(formatter)

    config = {}
    with open('config.json', 'r') as f:
        config = json.load(f)

    version = 'stewie (version {})'.format(__version__)

    parser = argparse.ArgumentParser()
    parser.add_argument('--version',
                        action='version',
                        version=version)
    args = parser.parse_args()

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
                'type': 'Button',
                'text': 'Bar'
            },
            {
                'type': 'Button',
                'text': 'Baz'
            }
        ]
    }
    Application(widgettree).run()
