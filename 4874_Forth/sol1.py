import sys
sys.stdin = open("input.txt")

T = int(input())


for tc in range(1, T+1):
    postfix = input().split()
    stack = []
    for i in postfix:
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
                if stack:
                    result = 'error'
        except:
            result = 'error'
            break

    print("#{} {}".format(tc, result))

