T = int(input())

while T:
    n = int(input())
    s = list(map(int, input().split()))
    if len(s) == 2 and s[1] - s[0] >1:
        print("YES")
    else:print("NO")


    T -= 1

