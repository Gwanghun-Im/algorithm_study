import sys
sys.stdin = open("input.txt")

T = int(input())

# 페이지를 찾는데 걸리는 횟수를 찾는 함수
def page(p, n):
    # 시작(left) 페이지, right는 p로 생각
    l = 1

    cnt = 0
    # 현재 페이지 temp
    temp = 0
    #만약 찾는페이지가 처음과 끝이 아니라면
    if n != p and 1 != n:
        #페이지를 찾고
        temp = int((l + p) / 2)
        # 횟수를 추가
        cnt += 1

    # 위 과정을 반복한다. 단,
    while temp != n:
        # 현재 페이지가 n 보다 작으면
        if temp < n:
            # 시작페이지를 현재페이지로 바꿔준다
            l = temp
        # 현재 페이지가 n보다 크면
        else:
            # 끝 페이지를 현재페이지로 바꿔준다.
            p = temp
        # 다음페이지 계산
        temp = int((l + p) / 2)
        # 횟수를 추가
        cnt += 1

    return cnt

for tc in range(1, T+1):
    P, Pa, Pb = map(int, input().split())
    result = 0
    cnt_a = page(P, Pa)
    cnt_b = page(P, Pb)
    # 둘 값이 다를때 실행
    if cnt_a != cnt_b:
        result = 'A' if cnt_a < cnt_b else 'B'

    print("#{} {}".format(tc, result))

