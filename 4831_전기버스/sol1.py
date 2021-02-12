import sys
sys.stdin = open("input.txt")

T = int(input())


for tc in range(1, T+1):
    K, N, M = map(int, input().split())
    m_list = list(map(int, input().split()))
    charger = [0]*N
    # 충전기의 위치를 1로 표기
    for i in range(N):
        if i in m_list:
            charger[i] = 1
            continue
        charger[i] = 0

    # 충전횟수
    result = 0
    # 남은 기름
    fuel = K
    # 이동한 거리
    i = 0

    while i < N-1:
        #1회 이동시 연료 -1, 이동거리 +1
        fuel -= 1
        i += 1

        # 충전소가 있을때
        if charger[i] == 1:
            # 다음 정류장을 살펴보고
            for j in range(i+1, N):
                # 다음 충전소가 존재할때,
                if charger[j] == 1:
                    # 다음 충전소 거리보다 기름이 적으면 충전
                    if j-i > fuel:
                        # 기름을 K만큼 충전
                        fuel = K
                        # 충천횟수 1증가
                        result += 1
                    break
                # 다음 충전소가 없을 경우, 최종 목적지 까지 거리보다 기름이 적으면 충전
                if j == N-1:
                    fuel = K
                    result += 1

        # 최종 목적지 전에 기름이 바닥나면 종료
        if fuel == 0 :
            result = 0
            break


    print("#{} {}".format(tc, result))

