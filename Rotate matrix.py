# import copy
#
matrix = [[1,2,3],[4,5,6],[7,8,9]]
# matrix_f = [ele[:] for ele in matrix]
# m = len(matrix)
# n = len(matrix[0])
# for k in range(m):
#     for l in range(n):
#         print(matrix[k][l], end =" ")
#     print()
# print()
# for i in range(m):
#     for j in range(n):
#
#         print(j, n -i -1, "->", i,j)
#         print(matrix_f[j][n - i - 1], '->',matrix[i][j] )
#         temp = matrix[i][j]
#         matrix_f[j][n - i - 1] = temp
#         print(matrix_f)
#         print()
# matrix = matrix_f
# print(matrix)
#########################
matrix_f = [ele[:] for ele in matrix]
print(matrix_f)
m = len(matrix)
n = len(matrix[0])
for i in range(m):
    for j in range(n):
        matrix_f[j][n - i - 1] = matrix[i][j]
matrix = matrix_f

print(matrix)

######################
matrix[:] = [ [row[i] for row in matrix[::-1] for i in range(len(matrix))]]