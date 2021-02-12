import sys
sys.stdin = open("input.txt")

T = 10


for tc in range(1, T+1):
    # 건물 갯수
    N = int(input())
    # 건물의 높이를 리스트로
    building = list(map(int, input().split()))
    # 여기에 결과를 저장!
    result = 0

    # 좌우로 2칸은 항상 0 이기에 검사할 필요가 없다.
    for i in range(2, N-2):
        # 주변에서 가장 높은 건물의 높이를 담는 변수
        high_around = 0
        # 좌우 2칸까지 가장 높은 건물 탐색
        for j in range(i-2, i+3):
            # 자기 자신일 경우 건너 뛴다.
            if i == j:
                continue
            # 더 높은 건물일 경우 update
            if building[j] > high_around:
                high_around = building[j]

        # 만약 현재 건물의 높이가 주변 건물의 높이보다 클 경우
        if building[i] > high_around:
            # 현재 건물에서 주변에서 가장높은 건물의 높이를 뺀값을 결과에 저장
            result += (building[i] - high_around)

    print("#{} {}".format(tc, result))

