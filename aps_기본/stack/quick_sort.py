my_list = [3, 9, 4, 7, 5, 0, 1, 6, 8, 4]


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


print(quick_sort(my_list))
