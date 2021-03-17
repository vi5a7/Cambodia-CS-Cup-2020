i, k = map(int, input().split())

mat = []
if i>=1 and k>=1:
    rowList = []
    for row in range(k):
        rowList.append(1)
    mat.append(rowList)
    for col in range(i):
        mat.append([1])

    for row in range(1,k):
        for col in range(1,i):
            mat[row][col].append(mat[row][col-1] + mat[row-1][col])

    print(mat)



