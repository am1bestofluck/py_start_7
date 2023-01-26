from pb_import import import_
from pb_export import update_base

import sys

if sys.argv[1] == "ask":
    import_(input('What do We seek?'))
if sys.argv[1] == 'add':
    update_base()