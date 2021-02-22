stack = []

input_str = '()()(()))((()()()'

for s in input_str:
    if s == '(':
        stack.append(s)
    else:
        if len(stack) == 0:
            result = False
            break
        stack.pop()
else:
    if stack:
        result = False
    else:
        result = True

print(result)