def counting_sort(A, B, k):
    C =[0]*k
    for i in range(len(B)):
        C[A[i]] += 1

    for i in range(len(C)):
        C[i] += C[i-1]

    for i in range(len(B)-1, -1, -1):
        B[C[A[i]]-1] = A[i]
        C[A[i]] -= 1