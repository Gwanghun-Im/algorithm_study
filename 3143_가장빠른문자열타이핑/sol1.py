import sys
sys.stdin = open("input.txt")

T = int(input())


for tc in range(1, T+1):
    a, b = input().split()

    print(a.count(b))
    print("#{} {}".format(tc, len(a)-(len(b)-1)*a.count(b)))