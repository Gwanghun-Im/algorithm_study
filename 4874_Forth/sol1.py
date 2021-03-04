import sys
sys.stdin = open("input.txt")

T = int(input())


for tc in range(1, T+1):
    # 후위 표기식
    postfix = input().split()
    stack = []
    for i in postfix:
        # 시도해봄
        try:
            if i not in '.+-/*':
                stack.append(int(i))
            elif i == '+':
                stack.append(stack.pop() + stack.pop())
            elif i == '*':
                stack.append(stack.pop() * stack.pop())
            elif i == '-':
                stack.append(stack.pop(-2) - stack.pop())
            elif i == '/':
                stack.append(stack.pop(-2) // stack.pop())
            elif i == '.':
                result = stack.pop()
                # 아직도 스택에 있으면 에러
                if stack:
                    result = 'error'
        # 오류가 나면 예외처리, stack 에 2개 미만으로 있는 경우일때를 방지
        except:
            result = 'error'
            break

    print("#{} {}".format(tc, result))

