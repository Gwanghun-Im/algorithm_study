import sys
sys.stdin = open("input.txt")

T = int(input())


for tc in range(1, T+1):
    d, a, b, f = map(int, input().split())
    # d(a+b) = 기차가 충돌하기까지 걸린시간
    # 시간*f(파리의 속력) = 파리가 달린 거리
    result = d/(a+b) * f

    print("#{} {}".format(tc, result))

