arr = [55, 7, 78, 12, 42]

def bubblesort(a):
    for i in range(len(a)-1, 0, -1):
        for j in range(i):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]

bubblesort(arr)
print(arr)