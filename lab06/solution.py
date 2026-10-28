values = ["ошибка", "запуск", "ошибка", "проверка"]

def count_items(values):
    new_val = {}
    for i in values:
        if i in  new_val.keys():
            new_val[i] += 1
        else:
            new_val[i] = 1
    return new_val

def unique_sorted(values):
    return sorted(set(values))

def common(list1, list2):
    com_list = []
    if len(list1) <= len(list2):
        for i in list1:
            if i in list2:
                com_list += [i]
    else:
        for i in list2:
            if i in list1:
                com_list += [i]
    return sorted(set(com_list))
        
def only_in_first(list1, list2):
    uni_list = []
    if len(list1) <= len(list2):
        for i in list1:
            if i not in list2:
                uni_list += [i]
    else:
        for i in list2:
            if i not in list1:
                uni_list += [i]
    return sorted(set(uni_list))

print(count_items([1, 2, 2, 2]))    # {"ошибка": 2, "запуск": 1, "проверка": 1}
print(unique_sorted([]))  # ["запуск", "ошибка", "проверка"]

print(common(["иванов", "петрова"], ["петрова", "котов"]))        # ["петрова"]
print(only_in_first(["иванов", "петрова"], ["петрова", "котов"])) # ["иванов"]