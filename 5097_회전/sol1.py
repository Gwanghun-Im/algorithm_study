import sys
sys.stdin = open("input.txt")

T = int(input())


for tc in range(1, T+1):
    n, m = map(int, input().split())
    li = list(map(int, input().split()))
    # m 번만큼 반복
    for i in range(m):
        # 앞의 요소를빼서 맨뒤에 더한다
        li.append(li.pop(0))
    print("#{} {}".format(tc, li[0]))

