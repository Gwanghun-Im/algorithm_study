import sys
sys.stdin = open("문제1_input.txt")

T = int(input())


for tc in range(1, T+1):
    # 입력을 리스트로 바꿔준다
    li = list(map(int, list(input())))
    # 입력받은 숫자의 개수를 세어준다
    nums = [0 for i in range(10)]
    for i in li:
        nums[i] += 1

    # triplet과 run의 초기값
    triplet = 0
    run = 0
    # triplet조사
    for i in range(10):
        while nums[i] >= 3:
            nums[i] -= 3
            triplet += 1
    # run 조사
    for i in range(1, 9):
        while nums[i-1] and nums[i] and nums[i+1]:
            nums[i-1] -= 1
            nums[i] -= 1
            nums[i+1] -= 1
            run += 1
    # triplet과 run의 합이 2 이상이면 1, 아니면 0
    r = 1 if triplet+run >= 2 else 0

    print("#{} {}".format(tc, r))

