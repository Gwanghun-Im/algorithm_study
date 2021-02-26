my_list = [3, 9, 4, 7, 5, 0, 1, 6, 8, 4]
my_list1 = [4, 2, 3, 5]


def quick_sort(nums):
    N = len(nums)
    if N <= 1:
        return nums
    else:
        pivot = nums[-1]
        left, right = [], []
        for i in range(N-1):
            if nums[i] > pivot:
                right.append(nums[i])
            else:
                left.append(nums[i])
        l = quick_sort(left)
        r = quick_sort(right)

        return [*l, pivot, *r]


def partition(arr, start, end):
    pivot = arr[start]
    left = start + 1
    right = end
    done = False
    while not done:
        while left <= right and arr[left] <= pivot:
            left += 1
        while left <= right and arr[right] >= pivot:
            right -= 1
        if right < left:
            done = True
        else:
            arr[left], arr[right] = arr[right], arr[left]
    arr[start], arr[right] = arr[right], arr[start]

    return right


def quick_sort2(arr, start, end):
    if start < end:
        pivot = partition(arr, start, end)
        quick_sort2(arr, start, pivot - 1)
        quick_sort2(arr, pivot + 1, end)
    return arr


print(quick_sort2(my_list, 0, len(my_list)-1), 'quick_sort 2')
print(quick_sort2(my_list1, 0, len(my_list1)-1), 'quick_sort 2')
print(quick_sort(my_list), 'quick_sort 1')
