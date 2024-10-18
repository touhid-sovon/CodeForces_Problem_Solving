a,b = map(int,input().split())
count = 0

while a<b:
    if b % 2 == 0:
        b = b // 2

print(count)
