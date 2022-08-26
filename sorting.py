#Sort an array by insertion sort method
def insertion_sort(arr):
    for i in range(1, len(arr)):
        temp = arr[i]
        j = i - 1

        while j >= 0 and temp < arr[j]:
            arr[j + 1] = arr[j]
            j = j - 1


        arr[j + 1] = temp


arr = [9, 8, 6, 7, 1, 3]
print("Unsorted Array:", arr)
insertion_sort(arr)
print('Sorted Array: ', arr)