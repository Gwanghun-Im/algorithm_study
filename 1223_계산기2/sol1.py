import sys
sys.stdin = open("input.txt")

T = 10


for tc in range(1, T+1):
    n = int(input())
    exp = input()

    postfix = ''
    stack = []
    for i in exp:
        if i not in '+*':
            postfix += i
        else:
            if i == '+':
                while stack:
                    postfix += stack.pop()
                stack.append(i)
            else:
                while stack and stack[-1]=='*':
                    postfix += stack.pop()
                stack.append(i)
    while stack:
        postfix += stack.pop()
    print(postfix)
    for i in postfix:
        temp = 0
        if i == '+':
            temp = int(stack.pop()) + int(stack.pop())
            stack.append(temp)
        elif i == '*':
            temp = int(stack.pop()) * int(stack.pop())
            stack.append(temp)
        else :
            stack.append(i)

    print("#{} {}".format(tc, *stack))

