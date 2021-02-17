def itoa(i):
    # ord 함수를 사용하여 아스키 코드 값으로 변환.
    s = []
    while i != 0 :
        r = i % 10
        s.insert(0,chr(ord('0') + r))
        i //= 10
    return ''.join(s)

print(itoa(123))