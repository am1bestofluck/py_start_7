import shelve
from consts import path_db

def sort_by_name() -> None: # пузырёк, работает но крайне медленно
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

sort_by_name()
