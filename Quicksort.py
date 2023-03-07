def quicksort(A, p, q):
    pivot = A[q]
    j = p
    for i in range(p,q+1):
        if A[i] < pivot:
            A[i], A[j] = A[j], A[i]
            j += 1
            continue

        if i == q:
            A[j], A[q] = A[q], A[j]
            quicksort(A, p, j -1)
            quicksort(A, j+1, q)
    return A

Array = [7, 3, 5, 1, 2, 8, 6, 716, 337, 3727, 212, 10, 5]
Arr = quicksort(Array, 0, len(Array)-1)
print(Arr)