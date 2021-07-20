def count_sort(array):
    sort_arr = []
    count = [0] * (max(array)+1)
    index = 0

    for i in array:
        count[i] += 1

    while index < len(count):
        if count[index] != 0:
            count[index] -= 1
            sort_arr.append(index)
        else:
            index += 1

    return sort_arr

print(count_sort([7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]))
print(count_sort([3, 2, 5, 4, 2, 1, 5, 2, 2, 1]))