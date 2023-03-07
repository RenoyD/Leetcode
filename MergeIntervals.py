intervals = [[1, 3], [2, 6], [4, 10], [3, 18]]

# sorting the interval
def quicksort(A, p, q):
    pivot = A[q][0]
    j = p
    for i in range(p, q + 1):
        if A[i][0] < pivot:
            A[i], A[j] = A[j], A[i]
            j += 1
            continue

        if i == q:
            A[j], A[q] = A[q], A[j]
            quicksort(A, p, j - 1)
            quicksort(A, j + 1, q)

quicksort(intervals, 0, len(intervals) - 1)

k = 0
while k+1 < len(intervals):
    if intervals[k+1][0] <= intervals[k][1]:
        # merge
        if intervals[k+1][1] >= intervals[k][1]:
            intervals[k+1][0] = intervals[k][0]
            del intervals[k]
        else:
            del intervals[k+1]
    else:
        k += 1

print(intervals)
