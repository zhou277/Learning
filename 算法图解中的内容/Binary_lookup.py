def binary_search(list, item):
    low = 0
    high = len(list) - 1
    while low <= high:
        mid = (low + high) // 2
        guess = list[mid]
        if guess < item:
            low = mid + 1
        elif guess > item:
            high = mid - 1
        elif guess == item:
            return mid
    return None


# TODO：想用分治策略实现二分查找的，但是m的值会发生变化，因此实现失败了
def bin_search_DC(list, item):
    low = 0
    high = len(list) - 1
    mid = (low + high) // 2
    if len(list) == 1 & list[mid] == item:
        return mid
    elif len(list) != 1 & list[mid] < item:
        return bin_search_DC(list[mid + 1:], item)
    elif len(list) != 1 & list[mid] > item:
        return bin_search_DC(list[:mid - 1], item)


My_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
My_item = 9
print(binary_search(My_list, My_item))
print(bin_search_DC(My_list, My_item))
