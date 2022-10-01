matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]

zero_r = list()
zero_c = list()
m = len(matrix)
n = len(matrix[0])

# finding all positions of 0
for i in range(m):
    for j in range(n):
        print(matrix[i][j])
        if matrix[i][j] == 0:
            # append in zero_r and _c
            if i not in zero_r:
                zero_r.append(i)
            if j not in zero_c:
                zero_c.append(j)

# updating the rows
for i in zero_r:
    for j in range(n):
        matrix[i][j] = 0

# updating the columns
for i in zero_c:
    for j in range(m):
        matrix[j][i] = 0

print(matrix)