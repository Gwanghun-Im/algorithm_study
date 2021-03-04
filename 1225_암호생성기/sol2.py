from collections import deque


for t in range(1, 11):
    input()
    array = deque(list(map(int, input().split())))
    delta = 1

    while True:
        cur_num = array.popleft()
        if cur_num - delta <= 0:
            array.append(0)
            break
        else:
            array.append(cur_num - delta)

        delta += 1

        if delta > 5:
            delta = 1

    print('#' + str(t), *array)