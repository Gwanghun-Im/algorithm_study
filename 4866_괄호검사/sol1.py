import sys
sys.stdin = open("input.txt")

T = int(input())


for tc in range(1, T+1):
    string = input()
    bracket = ['(', ')', '{', '}']
    stack = []
    # 스트링에서 하나하나꺼내와서
    for s in string:
        # 괄호만 간추린다
        if s in bracket:
            # 스택에 있으면
            if stack:
                # 아스키 코드 표를 보면
                # '(' 에서 -1 값이 ')' 가 된다.
                # '{' 에서 -2 값이 '}' 가 된다.
                if ord(stack[-1]) == ord(s)-2 or ord(stack[-1]) == ord(s)-1:
                    stack.pop()
                else:
                    stack.append(s)
            # 스택에 없으면 일단 추가
            else:
                stack.append(s)
    result = 0 if stack else 1

    print("#{} {}".format(tc, result))

