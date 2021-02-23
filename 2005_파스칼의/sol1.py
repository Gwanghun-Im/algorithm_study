import sys
sys.stdin = open("input.txt")

T = int(input())


for tc in range(1, T+1):
    n = int(input())
    #첫번째 어레이 1을 2차원 배열로 생성
    arr = [[1]]

    print("#{}".format(tc, ))

    print(*arr[0])
    #첫번째 열이 출력되었기 때문에 n-1만큼만 출력하면 된다.
    for i in range(n-1):
        # 지금 존재하는 행을 사용
        row = [1]
        # 가장 아래에 존재하는 열을 확인하고
        # 길이릐 -1 만큼 숫자를 더해준다.
        for j in range(len(arr[-1]) - 1):
            temp = arr[-1][j] + arr[-1][j+1]
            # 지금행에 더해준다
            row.append(temp)
        # 끝을 1로 채워준다
        row += [1]
        #배열에 더한다
        arr += [row]
        #바로 row를 출력
        print(*row)