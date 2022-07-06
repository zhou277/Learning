def Csum(list):
    if not list:
        return 0
    else:
        return list[0] + Csum(list[1:])


def Ccount(list):
    if not list:
        return 0
    else:
        return 1 + Ccount(list[1:])


def Cmax(list):
    if len(list) == 2:
        if list[0] >= list[1]:
            return list[0]
        else:
            return list[1]
    else:
        return max(list[1:])


def qsort(list):
    if len(list) < 2:
        return list
    else:
        pivot = list[0]
        less = [i for i in list[1:]
                if i < pivot]
        greater = [i for i in list[1:]
                   if i > pivot]
        return qsort(less) + [pivot] + qsort(greater)


Mylist = [1, 8, 16, 5, 11, 6, 9, 10]
print(qsort(Mylist))
