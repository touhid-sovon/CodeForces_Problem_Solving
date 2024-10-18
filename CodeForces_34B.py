n, m = map(int,input().split())
tvs = list(map(int,input().split()))

tvs.sort()
c = 1
income = 0
for tv in tvs:
    if tv < 0 and c <= m:
        income += abs(tv)
        c+=1
    if tv > 0:
        break
print(income)
