# a = [[1, 2, 3],
#      [4, 5, 6],
#      [7, 8, 9]]
#
# for i in range(len(a)):
#     for j in range(len(a[0])):
#         if i > j :
#             a[i][j],a[j][i] = a[j][i],a[i][j]
#
# print(a)


a = [1, 2, 3, 4]

for i in range(1<<len(a)):
    print('******',i,end='\n')
    for j in range(len(a)):
        if i & (1 << j):
            print(a[j],end=' ')
    print()
