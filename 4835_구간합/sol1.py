import sys
sys.stdin = open("input.txt")

def bubblesort(a):
    for i in range(len(a)-1, 0, -1):
        for j in range(i):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
    return a

T = int(input())


for tc in range(1, T+1):
    # 정수의 개수 N과 구간의 개수 M
    N, M = map(int, input().split())
    # N 개의 정수
    a = list(map(int, input().split()))

    # 구간합을 담을 공간
    section = []

    # 구간합을 계산한다
    # 구간은 정수 N개에서 구간의 길이만큼 뺀 값에 1을 더한만큼 나온다.
    for i in range(N-M+1):
        # 구간합을 더할 공간
        temp = 0
        # 현재 위치에서 +M 만큼의 값을
        for j in range(i, i+M):
            # temp에 더한다.
            temp += a[j]
        # 구간합을 담는다.
        section += [temp]
    # 구간합을 정렬한다.
    section = bubblesort(section)
    # 구간합의 마지막 위치(가장 큰 수)에서 첫번째 위치(가장 작은수)를 뺀다.
    result = section[-1] - section[0]

    print("#{} {}".format(tc, result))

