test = int(input())

while test > 0:
    n = int(input())
    if (n % 10) % 2 != 0:
        print("YES")
    else:
        print("NO")
    test -= 1