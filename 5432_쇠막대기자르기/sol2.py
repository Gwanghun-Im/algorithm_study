import sys
sys.stdin = open("input.txt")

T = int(input())


for tc in range(1, T+1):
    stick = input()
    answer = 0

    temp = 0
    for i in range(len(stick)):
        # 여는 괄호일땐 막대를 추가
        if stick[i] == '(':
            temp += 1
        # 닫는 괄로일때
        else:
            #
            temp -= 1
            # 전괄호가 여는 괄호이면 레이저이므로 answer에 저장한 막대를 추가
            if stick[i-1] == '(':
                answer += temp
            # 여는괄호가 아니면 막대의 마지막 부분이므로 1만 추가
            else:
                answer += 1

    print("#{} {}".format(tc, answer))

