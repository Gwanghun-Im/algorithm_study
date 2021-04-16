import sys
sys.stdin = open("input.txt")

for tc in range(1, int(input())+1):
    n = int(input())
    r = []
    print("#{}".format(tc))
    for i in [50000,10000,5000,1000,500,100,50,10]:
        r.append(n//i)
        n %= i
    print(*r)