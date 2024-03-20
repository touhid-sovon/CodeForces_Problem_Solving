n = int(input())

s = 0

while(n > 0):
    if n%2 ==1:
        s +=1
    n = int(n/2)

print(s)