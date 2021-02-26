T = int(input())


for tc in range(1, T+1):
    n, m1, m2 = map(int, input().split())
    block = list(map(int, input().split()))
    block.sort(reverse = -1)
    building = [[], []]
    for i in range(0,n,2):
        try :
            if len(building[0]) < m1:
                building[0].append(block[i])
            else:
                building[1].append(block[i])
        except:
            pass

        try:
            if len(building[1]) < m2:
                building[1].append(block[i+1])
            else:
                building[0].append(block[i+1])
        except:
            pass
    print(building)

    building_kg = 0
    for i in range(len(building)):
        for j in range(len(building[i])):
            building_kg += building[i][j]*(j+1)

    print("#{} {}".format(tc, building_kg))



    while m1 != 0 or m2 != 0:
        m1 -= 1

        m2 -= 1

