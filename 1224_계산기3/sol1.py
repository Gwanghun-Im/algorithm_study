import sys
sys.stdin = open("input.txt")

T = 10


for tc in range(1, T+1):
    priority = {'*': 3, '+': 2, '(': 1}
    n = int(input())
    exp = input()

    postfix = ''
    stack = []
    for i in exp:
        if i not in '+*()':
            postfix += i
        else:
            if i == '(':
                stack.append(i)
            elif i in '+*':
                if stack and priority[stack[-1]] >= priority[i]:
                    postfix += stack.pop()
                    stack.append(i)
                else:
                    stack.append(i)
            else:
                while stack[-1] != '(':
                    postfix += stack.pop()
                stack.pop()
        print(stack)
    while stack:
        postfix += stack.pop()

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