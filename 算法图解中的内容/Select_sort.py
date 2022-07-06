def FindSmallest(list):
    smallest = list[0]
    smallest_index = 0
    for i in range(1, len(list)):
        if list[i] < smallest:
            smallest = list[i]
            smallest_index = i
    return smallest_index


def select_sort(list):
    newlist = []
    for i in range(0, len(list)):
        smallest = FindSmallest(list)
        newlist.append(list.pop(smallest))
    return newlist


print(select_sort([1, 3, 5, 8, 9, 4, 7, 6, 7, 2, 9, 7, 1, 2, 8, 3]))
