#!/usr/bin/env python3
import logging

from demos import demo_vbox


if __name__ == '__main__':
    logger = logging.getLogger('stewie')
    handler = logging.FileHandler('stewie.log')
    logger.addHandler(handler)
    logfmt = '%(asctime)s %(name)s [%(levelname)s] %(message)s'
    formatter = logging.Formatter(logfmt)
    handler.setFormatter(formatter)

    demo_vbox()
