# для отладки
import shelve

with shelve.open('dtb') as content:
    q = dict(content)
print(q.keys())
print(q['backend'])
print(len(q['db']))