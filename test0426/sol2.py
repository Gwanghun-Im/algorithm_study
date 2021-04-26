import sys
sys.stdin = open("문제2_input.txt")

T = int(input())

for tc in range(1, T+1):
    # n, m
    n, m = map(int, input().split())
    # 찾아야 하는 list
    m_list = list(map(int, input().split()))
    # 정렬된 숫자 리스트
    nums = list(map(int, input().split()))
    # 결과를 담을 창
    r = []
    # 숫자를 뽑는다. : i
    for i in m_list:
        # 시작 인덱스
        s = 0
        # 끝 인덱스
        e = n-1
        # 탐색 횟수
        cnt = 1
        while s <= e:
            # 중간지점
            mid = (s+e)//2
            # 만약 중간 지점이 찾는 숫자와 같다면
            if nums[mid] == i:
                # 카운트와 , 숫자를 r에 추가
                r.append((cnt, i))
                break
            # 만약 찾는 숫자가 작으면
            if nums[mid] < i:
                # 시작지점을 mid+1
                s = mid + 1
            # 만약 찾는 숫자가 크면
            elif nums[mid] > i:
                # 끝 지점을 mid -1
                e = mid - 1
            # 탐색횟수 추가
            cnt += 1
    # r을 카운트 순으로 정렬
    r.sort()
    print("#{} {} {}".format(tc, r[0][1], r[0][0]))

