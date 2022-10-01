numRows = 10
answer = []
for i in range(numRows):
    row = []
    for j in range(i+1):

        # 1st element
        if j == 0:
            row.append(1)
            continue

        # last element
        if j == i:
            row.append(1)
            continue

        row.append(answer[i-1][j-1] + answer[i-1][j])

    answer.append(row)

print(answer)

