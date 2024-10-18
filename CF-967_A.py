T = int(input())

while T:
    m = int(input())
    a = list(map(int,input().split()))
    a.sort()
    count = 1
    max_count = 1
    for i in range(1,m):
        if a[i] == a[i-1]:
            count += 1
        else:
            count = 1
        max_count = max(max_count,count)
    print(m-max_count)
    T -= 1