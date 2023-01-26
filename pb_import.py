import datetime,time
import shelve
from pathlib import Path

def import_(name_to_import: str =  None) -> None:
    """лезем в шкаф, ищем то что в name_to_import; если name_to_import - пустое:
    выгребаем всю базу
    """
    # определяемся с именем файла 
    who = "full" if name_to_import is None or set(name_to_import)== set()\
         else name_to_import
    report_name = f"{who}_{datetime.datetime.today():%m%d%Y_%H%M%S__%f}.txt"
    # идём по базе
    find_ = "" if name_to_import is None else name_to_import.upper()
    extracted = ""
    with shelve.open('dtb','r') as read_it:
        for id in read_it['db']:
            if find_ in read_it['db'][id]['name']:
                extracted += f"{str(read_it['db'][id])}\n"
    # выгружаем
    if not extracted:
        print("no matches")
        return None
    while Path(report_name).exists():
        time.sleep(0.000001)
        report_name = f"{who}_{datetime.datetime.today():%m%d%Y_%H%M%S__%f}.txt"
    with open(report_name,'w') as write_here:
        write_here.write(extracted)
    # закругляемся
    print(f"Выгружено в {report_name}")
    return None