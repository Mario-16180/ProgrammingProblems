n = int(input())
A = [int(x) for x in input().split()]
h, sh = 0, 0
ih, ish = 0, 0
for i in range(n):
    if A[i] > h:
        sh = h
        ish = ih
        h = A[i]
        ih = i
    elif A[i] > sh:
        sh = A[i]
        ish = i
print(ih + 1, sh)
