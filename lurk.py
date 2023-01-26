# для отладки
import shelve

from consts import path_db

with shelve.open(path_db) as content:
    q = dict(content)
print(q.keys())
print(q['backend'])
print(len(q['db']))
print(q['db'][999])
try:
    print(q['db'][1000])
except KeyError:
    print('default base?')