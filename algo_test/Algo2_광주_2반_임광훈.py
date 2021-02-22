import sys
sys.stdin = open("2번_input.txt")

T = int(input())


for tc in range(1, T+1):
    # 먼저 플레이하는 사람을 입력
    first_player = input()
    # 두번째 플레이어는 first_player에 따라 다르다
    second_player = 'B' if first_player == 'A' else 'A'

    # a의 주사위를 입력
    dice_a = list(map(int, input().split()))
    # b의 주사위를 입력
    dice_b = list(map(int, input().split()))

    #첫번째 플레이어의 주사위 위치
    first = -1
    # 두번째 플레이어의 주사위 위치
    second = -1
    # 승자의 결과, 현재는 무승부로 둔다.
    result = 'AB'

    # 주사위 실행 순서를 저장한다.
    # 만약 첫번째 플레이어가 A라면
    if first_player == 'A':
        # dice변수에 A의 주사위를 먼저 입력시키고
        dice = [dice_a, dice_b]
    # B가 먼저라면
    else:
        # dice변수에 B의 주사위를 먼저 입력한다.
        dice = [dice_b, dice_a]

    # 총 10번의 길이만큼 반복한다.
    for i in range(10):
        # 첫번째 플레이어먼저 시작해서
        first += dice[0][i]
        # 만약 옮긴 위치가 두번째 플레이어와 같다면
        if first == second:
            # 두번째 플레이어의 주사위 위치를 초기화 시켜준다.
            second = -1
        # 만약 첫번째 플레이어의 주사위 위치가 19이상이면 게임은 끝나고
        # 승자는 첫번째 플레이어가 된다.
        if first >= 19:
            result = first_player
            break

        # 두번째 플레이어도 주사위를 굴리고
        second += dice[1][i]
        # 만약 첫번째 플레이어의 위치와 겹친다면
        if first == second:
            # 첫번째 플레이어의 위치를 초기화 한다.
            first = -1
        # 두번째 플레이어의 위치가 19 이상이면
        # 게임을 끝내고 승자는 두번째 플레잉어가 된다.
        elif second >= 19:
            result = second_player
            break
    # 게임이 끝나도 break에 걸리지 않았으면 자동으로 무승부가 되어,
    # 결과는 'AB'가 된다.


    print("#{} {}".format(tc, result))

