import shelve
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

def qs_main():
    with shelve.open(path_db,writeback=True) as content:
        qs_name(content,0,len(content['db']))
def qs_name(base:dict = None, i_index_left:int= 0 ,i_index_right:int = 0) -> None:
        if base is None:
            with shelve.open(path_db,writeback=True) as content:
                content = content
        m_index_left,m_index_right = i_index_left, i_index_right
        test_case = content['db'][m_index_left]
        while m_index_left <= m_index_right:
            while test_case > content['db'][m_index_right]:
                m_index_right -=1
            while test_case < content['db'][m_index_left]:
                m_index_left +=1
            if content['db'][m_index_left] <= content['db'][m_index_right]:
                temp = content['db'][m_index_left]
                content['db'][m_index_left] = content['db'][m_index_right]
                content['db'][m_index_right] = temp
                m_index_right -= 1
                m_index_left += 1
            if (m_index_left < i_index_right):
                qs_name(content['db'],)
            if (m_index_right >m_index_left):
                qs_name(content['db'])


