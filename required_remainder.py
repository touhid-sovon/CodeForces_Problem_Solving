t = int(input())
while t > 0:
    x,y,n = map(int,(input().split()))
    rem = n % x
    res = 0
    if rem == y:
        res = n
    elif rem < y:
        res  = n - rem - (x-y)
    elif rem > y:
        res = n - (rem - y)

    print(res)
    t -= 1
