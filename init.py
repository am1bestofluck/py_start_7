# к заданию не относится, создаёт дефолтную базу
import random,shelve
from consts import path_db, random_names
counter = 0
with open(random_names) as lst:
    all_names = list(lst.read().split('\n'))
with shelve.open(path_db,'n',writeback=True) as core:
    core['backend']=dict()
    core['backend']['indx'] = 1000
    core ['db'] = dict()
    for name in all_names:
        randnum = f"022{random.choice(range(1000)):03}"+\
            f"{random.choice(range(1000)):03}"
        comment = random.choice(["work","home","obsolete"])
        core['db'][counter] = {"id": counter, "name": name.upper(),\
             "phone": randnum, 'comment':comment}
        counter += 1