import sys
sys.stdin = open("input.txt")

T = int(input())


for tc in range(1, T+1):
    stick = '0'.join(input().split('()'))

    answer = 0

    temp = 0
    for i in stick:
        # 쇠막대를 넣고
        if i == '(':
            temp += 1
        # 지금까지 넣은 쇠막대를 작두로 내리친다.
        if i == '0':
            # 지금까지 넣은 쇠막대의 길이만큼 추가
            answer += temp
        # 쇠막대 하나의 꼬투리
        if i == ')':
            # 결과에 하나 추가하고
            answer += 1
            # 넣은 쇠막대는 하나 사라진다.
            temp -= 1

    print("#{} {}".format(tc, answer))