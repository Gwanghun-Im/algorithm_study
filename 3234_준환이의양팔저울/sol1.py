import sys, itertools
sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T+1):
    n = int(input())
    li = list(map(int, input().split()))
    li.sort()
    cnt = 0
    k = len(bin(2 ** n)[2:])
    npr = itertools.permutations(li, n)
    for li in npr:
        for j in range(2**n):
            right = 0
            left = 0
            binary = '0'*(k-len(bin(j)[2:])-1)+bin(j)[2:]
            for i in range(n):
                if binary[i] == '1':
                    left += li[i]
                else:
                    right += li[i]
                if right > left:
                    break
            else:
                cnt += 1

    print("#{} {}".format(tc, cnt))

