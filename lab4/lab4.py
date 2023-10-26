# Построение хэш-таблицы
ht = {}


def genKey ( s, modKey):
    sord = ""
    for c in s :
        k = ord( c)
        sord = sord + str( k)
    num = int( sord)
    key = num % modKey
    skey = str( key)
    return skey


def add ( skey, s):
    global ht
    if ( skey in ht):
        ht[ skey].append( s)
    else:
        t = []
        t.append( s)
        ht[ skey] = t


def printHt( h):
    for key in h :
        print( "Ключ ", key, " соответствует строкам:")
        for j in h[ key]:
            print( j) 
        print()
    if (len(ht) == 0):
        print('Таблица пуста.')


def find(st, modle_key):
    global ht
    key = genKey(st, modle_key)
    if (key in ht.keys()):
        mas = ht[key]
        if (st in mas):
            return key
        else:
            return ""
    else:
        return ""


def delete( st, modle_key):
    global ht
    key = find(st, modle_key)
    if (key != ""):
        mas = ht[key]
        cm = mas.count(st)
        for i in range(cm):
            mas.remove(st)
        print('Элемент(ы) удалён.')
    else:
        print("Элемент не найден")


# главная программа.
mk = int( input( "Введите коэффициент для построения ключа: "))


while(True):
    dataRaw = input("Введите команду.")


    if(dataRaw == "add"):
        sf = input("Введите значение, которое Вы хотите добавить в таблицу.")
        keyf = genKey(sf, mk)
        add(keyf, sf)


    elif(dataRaw == "delete"):
        sf = input("Введите значение, подлежащее удалению из таблицы.")
        delete(sf, mk)


    elif(dataRaw == "find"):
        sf = input("Укажите значение для поиска в таблицы.")
        if (find(sf, mk) != ''):
            print('Элемент найден.')
        else:
            print('Жлемент не найден.')


    elif(dataRaw == "print"):
        printHt(ht)
        print()


    elif(dataRaw == "exit"):
        break


    else:
        print("Ошибка ввода команды!")


print( "Конец программы.")