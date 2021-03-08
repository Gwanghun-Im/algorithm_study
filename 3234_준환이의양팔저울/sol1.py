import sys
sys.stdin = open("input.txt")


def next_permutation(nums):
    i = l = len(nums)-1
    while i > 0:
        if nums[i] > nums[i-1]:
            temp = 0
            for j in range(l, i-1, -1):
                if nums[j] > nums[i-1]:
                    temp = j
                    break
            nums[i-1], nums[temp] = nums[temp], nums[i-1]
            for j in range(i, i+1+(l-i)//2):
                nums[j], nums[l+i-j] = nums[l+i-j], nums[j]
            break
        i -= 1

    if i == 0:
        return -1

    return nums


T = int(input())

for tc in range(1, T+1):
    n = int(input())
    li = list(map(int, input().split()))
    li.sort()
    cnt = 0

    while li != -1:
        right = 0
        left = 0
        for i in range(n):

            pass
        li = next_permutation(li)

    print("#{} ".format(tc, ))

