def selection_sort(N, arr):
    for i in range(N):
        idx = i
        for j in range(i+1, N):
            if arr[j] < arr[i]:
                idx = j
        arr[i], arr[idx] = arr[idx],arr[i]

    return arr

k = [5, 3, 4, 7, 2]
print(selection_sort(5, k))