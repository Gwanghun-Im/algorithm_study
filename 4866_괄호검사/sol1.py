import sys
sys.stdin = open("input.txt")

T = int(input())


for tc in range(1, T+1):
    string = input()
    bracket = ['(', ')', '{', '}']
    stack = []
    for s in string:
        if s in bracket:
            if stack:
                if ord(stack[-1]) == ord(s)-2 or ord(stack[-1]) == ord(s)-1:
                    stack.pop()
                else:
                    stack.append(s)
            else:
                stack.append(s)
    result = 0 if stack else 1

    print("#{} {}".format(tc, result))

