import sys
sys.stdin = open("input.txt")

T = 10


for tc in range(1, T+1):
    n, m = input().split()
    stack = []
    for i in m:
        if not stack:
            stack.append(i)
        else:
            if i == stack[-1]:
                stack.pop()
            else:
                stack.append(i)

    print("#{} {}".format(tc, ''.join(stack)))

