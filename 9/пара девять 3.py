def calculate(*args):
    list_of_all = []
    new_list = []
    for arg in args:
        list_of_all.append(arg)
    number = sum(list_of_all) / len(list_of_all)
    for el in list_of_all:
        if el > number:
            new_list.append(el)
    tuple_ = (number, new_list)
    return tuple_