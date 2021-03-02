import sys
sys.stdin = open("input.txt")

T = int(input())


for tc in range(1, T+1):
    N, M, K = map(int,input().split())
    Ns = list(map(int, input().split()))
    # 일단 사람을 정렬하자
    Ns.sort()

    # 붕어빵 개수
    fishbread = 0
    # 현재 경과시간
    t = 0
    # 일단은 가능
    ans = 'Possible'
    # 다음 붕어빵 추가시간
    next_t = M

    # 언제까지? -> 대기하는 사람이 있을때 까지
    while Ns:
        # 만약 추가시간이면
        if t == next_t:
            # 붕어빵 추가하고
            fishbread += K
            # 다음붕어빵 시간 업데이트함
            next_t += M
        # 아직 대기하는 사람이 있을때 ( 같은시간에 여러명이 올걸 생각하고)
        while Ns and t == Ns[0]:
            # 대기 사람에게 붕어빵을 준다
            Ns.pop(0)
            fishbread -= 1
        # 붕어빵 개수가 부족해?
        if fishbread < 0:
            # 그럼 못주는거지 ;;
            ans = 'Impossible'
            break
        t += 1

    print("#{} {}".format(tc, ans))

