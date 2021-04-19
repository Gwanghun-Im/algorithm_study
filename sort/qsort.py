def qsort(arr):
    if len(arr)<=1:
        return arr
    return qsort([x for x in arr[1:] if x < arr[0]]) + [arr[0]] + qsort([x for x in arr[1:] if x >= arr[0]])

array = [97, 200, 100, 101, 211, 107]
arr = qsort(array)
print(arr)