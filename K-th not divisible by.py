i = int(input())

while(i):
    n , k = map(int,input().split())
    try:
        div = k//(n-1)
    except:
        print("zero")
    if n == k:
        res = n+1
    elif (k % div) == 0:
        res = (n*div) - 1
    else:
        res = n * (div) + (k%div)
    print(res)

    i -= 1
