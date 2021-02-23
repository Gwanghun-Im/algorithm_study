import sys
sys.stdin = open("input.txt")

T = int(input())


for tc in range(1, T+1):
    string = input()
    stack = []
    cnt = 0

    for s in string:
        if not stack:
            stack.append(s)
        else:
            if s == stack[-1]:
                stack.pop()
            else:
                stack.append(s)

    print("#{} {}".format(tc, len(stack)))

