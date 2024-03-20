''' Football'''

n = int(input())
count = 0
str2 = ""
for i in range(n):
    str1 = input()
    if i == 0:
        temp = str1
        count = 1
    else:
        if str1 == temp:
            count+=1
        else:
            str2 = str1
            count -= 1

if count > 0:
    print(temp)
else:
    print(str2)




