import sys
sys.stdin = open("input.txt")

T = int(input())

def is_run(s):
    for i in range(len(s)-1):
        if s[i]+1 != s[i+1]:
            return False
    return True

def is_triplet(s):
    temp = s[0]
    for i in s:
        if i != temp:
            return False
    return True

def bubblesort(a):
    for i in range(len(a)-1, 0, -1):
        for j in range(i):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
    return a

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
        return False

    return(nums)


for tc in range(1, T+1):
    num = input()
    nums = []
    result = 0

    for i in num:
        nums += [int(i)]

    nums = bubblesort(nums)
    while nums:
        if (is_run(nums[:3]) or is_triplet(nums[:3])) and (is_run(nums[3:]) or is_triplet(nums[3:])):
            result = 1
            print(nums)
            print(is_run(nums[:3]))
            print(is_run(nums[3:]))
            print(is_triplet(nums[:3]))
            print(is_triplet(nums[3:]))
            break
        nums = next_permutation(nums)


    print("#{} {}".format(tc, result))

