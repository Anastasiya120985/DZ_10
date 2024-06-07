# Есть четыре списка целых. Необходимо их объединить в пятом списке. Полученный результат в зависимости от
# выбора пользователя отсортировать по убыванию или возрастанию. Найти значение, введенное пользователем,
# с использованием линейного поиска.

def linear_search(list1, list2, c = True):
    finalList = []
    if list1[0] <= list2[0]:
        finalList.insert(0, list1.pop(0))
        finalList.insert(1, list2.pop(0))
    else:
        finalList.insert(0, list2.pop(0))
        finalList.insert(1, list1.pop(0))
    for i in range(len(list1)):
        index = ''
        for k in range(len(finalList)):
            if list1[i] <= finalList[k]:
                index = k
                break
            else:
                index = k + 1
        finalList.insert(index, list1[i])
    for i in range(len(list2)):
        index = ''
        for k in range(len(finalList)):
            if list2[i] <= finalList[k]:
                index = k
                break
            else:
                index = k + 1
        finalList.insert(index, list2[i])
    if c:
        return finalList
    else:
        return finalList[::-1]

a = [5, 19, 1, 7, 4]
b = [11, 5, 1, 14, 12, 10, 17]
c = [0, 19, 9, 1, 4]
d = [17, 9, 5, 10, 14, 13, 1]
answer = input('Сортировать оценки по возрастанию или убыванию? (в/у) ')
if answer == 'в':
    e = linear_search(a, b, True)
    f = linear_search(e, c, True)
    result = linear_search(f, d, True)
    print(result)
elif answer == 'у':
    e = linear_search(a, b, False)
    f = linear_search(e, c, False)
    result = linear_search(f, d, False)
    print(result)
else:
    print('Введено некорректное значение!')

# [0, 1, 1, 1, 1, 4, 4, 5, 5, 5, 7, 9, 9, 10, 10, 11, 12, 13, 14, 14, 17, 17, 19, 19]

# Есть четыре списка целых. Необходимо объединить в пятом списке только те элементы, которые уникальны
# для каждого списка. Полученный результат в зависимости от выбора пользователя отсортировать по убыванию или
# возрастанию. Найти значение, введенное пользователем, с использованием бинарного поиска.

def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return -1
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    if arr[-1] < target:
        mid = mid + 1
    if arr[0] < target:
        mid = mid + 1
    return mid

def binary_merge(arr_1, arr_2, a=True):
    arr_1 = sorted(arr_1, reverse=False)
    arr_2 = sorted(arr_2, reverse=False)
    for i in arr_1:
        index = binary_search(arr_2, i)
        if index != -1:
            arr_2.insert(index, i)
    if a:
        return arr_2
    else:
        return arr_2[::-1]

a = [5, 19, 1, 7, 4]
b = [11, 5, 1, 14, 12, 10, 17]
c = [0, 19, 9, 1, 4]
d = [17, 9, 5, 10, 14, 13, 1]
answer = input('Сортировать оценки по возрастанию или убыванию? (в/у) ')
if answer == 'в':
    e = binary_merge(a, b, True)
    f = binary_merge(e, c, True)
    result = binary_merge(f, d, True)
    print(result)
elif answer == 'у':
    e = binary_merge(a, b, False)
    f = binary_merge(e, c, False)
    result = binary_merge(f, d, False)
    print(result)
else:
    print('Введено некорректное значение!')

# [0, 1, 4, 5, 7, 9, 10, 11, 12, 13, 14, 17, 19]