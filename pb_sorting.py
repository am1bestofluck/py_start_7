import shelve
import pprint
from consts import path_db

def sort_by_name() -> None: # пузырёк, работает настолько медленно что можно
    # сказать что не работает
    with shelve.open(path_db,writeback=True) as content:
        unit = 0
        while unit < len(content['db'])-1:
            if content['db'][unit+1]['name'] > content['db'][unit]['name']:
                content['db'][unit+1]['name'],content['db'][unit]['name'] =\
                    content['db'][unit]['name'], content['db'][unit+1]['name']
                unit = 0
                # print(f'#{unit}')
            unit +=1
            # print(f'!!{unit}')
            
    # return

def sort_by_index() -> None:
    with shelve.open(path_db,writeback=True) as content:
        unit = 0
        while unit < len(content['db'])-1:
            if content['db'][unit+1]['name'] > content['db'][unit]['name']:
                content['db'][unit+1]['name'],content['db'][unit]['name'] =\
                    content['db'][unit]['name'], content['db'][unit+1]['name']
                unit = 0
                # print(f'#{unit}')
            unit +=1
            # print(f'!!{unit}')
def extract_key(itm):
    print(itm)
    return itm['name']


def sort_main():
    with shelve.open(path_db,writeback=True) as content:
        q = content['db'].values()
        sorted(q,key=extract_key)
        pprint.pp(q)


sort_main()