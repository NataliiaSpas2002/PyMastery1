def binary_search(my_list, item):
    low = 0
    high = len(my_list) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = my_list[mid]

        if guess == item:
            return mid

        if guess < item:
            low = mid + 1
        else:
            high = mid - 1
    return None

my_list2 = [1, 3, 5, 7, 9]

print(binary_search(my_list2, 9))
# print(binary_search(my_list2, -1))

def findSmallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index
def selectionSort(arr):
    newArr = []
    for i in range(len(arr)):
        smallest = findSmallest(arr)
        newArr.append(arr.pop(smallest))
    return newArr

print(selectionSort([5, 3, 6, 2, 10]))