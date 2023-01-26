

import shelve
import string

def validate() -> tuple[str]:
    
    validSymbols = " -абвгдеёжзийклмнопрстуфчцчшщъыьэюя"
    validSymbols += validSymbols.upper()
    validSymbols = set(validSymbols)
    validSymbols.update(set(string.ascii_letters))
    while True:
        name = input("Name Surname")
        if set(name).issubset(' -'):
            print('blank is forbidden')
            continue
        if not set(name).issubset(validSymbols): # symbols
            print(f"Symbol(s)" + 
            f" {sorted(list(''.join(set(name).difference(validSymbols))))}"+\
             " are forbidden.")
            continue
        if len(name.strip().split())<2: #two words
            print(" at least two words separated by space")
            continue
        name = name.upper()
        break

    validSymbols = string.digits  + "+()- "
    validSymbols = set(validSymbols)
    while True:
        phone = input('phone')
        if set(phone).issubset(' -+()'):
            print('blank is forbidden')
            continue
        if not set(phone).issubset(validSymbols): # symbols
            print(f"Symbol(s)" + 
            f" {sorted(list(''.join(set(phone).difference(validSymbols))))}"+\
             " are forbidden.")
            continue
        break

    comment = input("Comment? 100 symbols cap.")[:100]
    return (name,phone,comment)

def update_base():
    data = validate()
    with shelve.open("dtb",writeback=True) as content:
        ind = content['backend']['indx']
        content['backend']['indx'] = ind+1
        content['db'][ind] = {"id":ind, "name": data[0], "phone": data[1],
            'comment':data[2]}
