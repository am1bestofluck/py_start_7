"""
Работает из консоли.

ask - запускает запрос из базы.
add - добавляет пользователя.
"""

import sys

from pb_import import import_
from pb_export import update_base


def main():
    if len(sys.argv) != 2:
        print(__doc__)
        return
    keywords=('ask','add')
    if sys.argv not in keywords:
        if sys.argv[1] == keywords[0]:
            import_(input('What do We seek?'))
        if sys.argv[1] == keywords[1]:
            update_base()

main()