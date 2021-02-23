import sys
sys.stdin = open("input.txt")

T = int(input())


for tc in range(1, T+1):
    stick = input()
    # 막대기를 저장할곳
    stack = []
    # 결과
    result = 0

    for i in range(len(stick)):
        # 만약 '('면 바로 스택에 추가
        if stick[i] == '(':
            stack.append(i)

        else:
            # 일단 pop하고
            stack.pop()
            # 이전이 '('면 스택의 길이만큼 결과에 추가
            if stick[i-1] == '(' : result += len(stack)
            # 아니면 1만 추가
            else : result += 1
    print("#{} {}".format(tc, result))

