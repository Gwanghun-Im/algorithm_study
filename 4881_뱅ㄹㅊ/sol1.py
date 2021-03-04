import sys
sys.stdin = open("input.txt")


def solve(n):
    # 값이 가장 큰 경우를 미리 result로 만듦
    result = 10 * n
    while x_stack:
        now = x_stack.pop()
        # 만약 now의 길이가 n이면
        if len(now) == n:
            temp = 0
            for i in range(n):
                temp += matrix[i][now[i]]
            # result와 비교 후 업데이트
            if result > temp:
                result = temp
        # 아니면 추가
        else:
            # 인덱스를 길이만큼 반복
            for i in range(n):
                temp = 0
                # 가지치기, 지금까지 좌표로 더했을때 ,result보다 크다면 추가 안해도 댐
                for j in range(len(now)):
                    temp += matrix[j][now[j]]
                if temp >= result:
                    break
                # now에 인덱스가 없으면 추가
                if i not in now:
                    x_stack.append(now + [i])
    return result


T = int(input())

for tc in range(1, T+1):
    n = int(input())
    matrix = [list(map(int, input().split())) for _ in range(n)]
    # 먼저 스택에 0번째 열의 인덱스를 삽입(시작점), 스택에는 좌표가 쌓일 예정
    x_stack = [[i] for i in range(n)]

    print("#{} {}".format(tc, solve(n)))

