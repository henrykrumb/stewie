import argparse

from .listbox import demo_listbox
from .vbox import demo_vbox


demos = {
    'listbox': demo_listbox,
    'vbox': demo_vbox
}


def main():
    parser = argparse.ArgumentParser()
    choices = list(demos.keys())
    parser.add_argument('DEMO',
                        choices=choices)
    args = parser.parse_args()
    demo = args.DEMO
    demos.get(demo)()
