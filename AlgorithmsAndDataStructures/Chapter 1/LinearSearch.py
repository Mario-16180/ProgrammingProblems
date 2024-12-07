A = [float(x) for x in input().split()]
v = float(input())
i = None
for j in range(len(A)):
    if v == A[j]:
        i = j
print(i)
