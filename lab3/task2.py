# Создаём бинарное дерево.
root = None


def createNode(inform, parentNode):
    temp = {"left": None, "right": None}
    temp["value"] = inform
    temp["parent"] = parentNode
    return temp


# Функция для добавления элемента.
def add (inform, tree, parentNode):
    temp = tree
    global root
    if (tree == None):


# Формирование нового узла дерева.
        temp = createNode(inform, parentNode)


# Добавление узла в пустое дерево (создание корня).
        if (root == None):


# "root" получает указатель на первый созданный узел.
            root = temp


# Если добавляемое значение inform меньше значения в узле дерева, то добавляем его в левое поддерево.
    elif (inform < tree["value"]):
        temp["left"] = add(inform, tree["left"], tree)
    elif (inform > tree["value"]):
        temp["right"] = add(inform, tree["right"], tree)
    else:
        print("Элемент с данным значением уже имеется в структуре дерева.")
    return temp # Ссылка либо на вновь созданный узел, либо на то поддерево, в котором выполнялось сравнение.


# Обход дерева и печать информационных полей его узлов.
def traversal(tree):
    if (tree != None):
        traversal(tree["left"])
        print(tree["value"], end = " ")
        p = tree["parent"]
        if (p != None):
            print('Родитель', p["value"])
        else:
            print("родитель пуст.")
        traversal(tree['right'])


def find(elem, tree): # возвращает ссылку на найденный узел.
    temp = tree
    while(temp != None):
        if (elem > temp["value"]):
            temp = temp["right"]
        elif (elem < temp["value"]):
            temp = temp["left"]
        else:
            return temp # Возвращает ссылку на найденый узел.
    return temp # После цикла возвращает пустую ссылку. Узел не найден.


def delNode(deleting):
    global root
    if (deleting == None):
        print("Попытка удалить несуществующий узел.")
        return False
    tempLeft = deleting["left"]
    tempRight = deleting["right"]
    tempParent = deleting["parent"]
    if (tempRight == None): # Если правое поддерево удаляемого узла пусто.
        if (tempParent != None): # Если удаляемый узел является промежуточным.
            if (deleting["value"] < tempParent ["value"]):
                tempParent["left"] = tempLeft
            else:
                tempParent["right"] = tempLeft
        else:
            root = tempLeft
        if (tempLeft != None):
            tempLeft["parent"] = tempParent
    else: # Правое поддерево не пустое.
        tempRight["parent"] = tempParent
        if (tempParent != None):
            if (deleting["value"] > tempParent["value"]):
                tempParent["right"] = tempRight
            else:
                tempParent["left"] = tempRight
        else:
            root = tempRight
# Правое поддерево прикреплено к родителю удаляемого элемента.


# Левое поддерево удаляемого элемента надо прикрепить к самому левому элементу правого поддерева.
        if (tempLeft != None):
            temp = tempRight
            while(temp["left"] != None):
                temp = temp["left"]
            temp["left"] = tempLeft
            tempLeft["parent"] = temp
    temp = deleting
    temp.clear()
    return True


# Удаление элемента.
def delete(elem, tree):
    global root
    temp = find(elem, root)
    if (temp != None):
        if delNode(temp):
            print("Элемент удалён.")
            return True
        else:
            print("Элемент найден, но не удалён.")
            return False
    else:
        print("Элемент не найден.")


# Главная программа.
while(True):
    dataRaw = input("Введите команду.")


    if(dataRaw == "add"):
        elem = input("Введите значение, которое Вы хотите добавить в дерево.")
        elem = int(elem)
        add(elem, root, None)


    elif(dataRaw == "delete"):
        elem = input("Введите значение, подлежащее удалению из дерева.")
        elem = int(elem)
        delete(elem, root)


    elif(dataRaw == "find"):
        elem = input("Укажите значение для поиска в структуре дерева.")
        elem = int(elem)
        find(elem, root)


    elif(dataRaw == "traversal"):
        traversal(root)
        print()


    elif(dataRaw == "exit"):
        break


    else:
        print("Ошибка ввода команды!")


print("Конец программы.")