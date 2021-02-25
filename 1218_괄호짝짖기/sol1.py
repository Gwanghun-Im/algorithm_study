import sys
sys.stdin = open("input.txt")

T = 10


for tc in range(1, T+1):
    n = int(input())
    string = input()
    stack = []
    # 스트링에서 꺼내온다
    for s in string:
        if stack:
            # 아스키 코드 표를 참고하면
            # -1, -2 의 규칙성을 가진다
            if ord(stack[-1]) == ord(s) - 2 or ord(stack[-1]) == ord(s) - 1:
                stack.pop()
            else:
                stack.append(s)
        else:
            stack.append(s)
    result = 0 if stack else 1

    print("#{} {}".format(tc, result))

