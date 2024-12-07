params = [int(x) for x in input().split()]
a, x, y = params[0], params[1], params[2]

if x < 0 or y < 0: 
    print(2)
elif x < a and y < a:
    print(0)
elif (x == a and y <= a) or (y == a and x <= a):
    print(1)
else:
    print(2)