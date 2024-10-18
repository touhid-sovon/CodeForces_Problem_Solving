T = int(input())

while T:
    n = int(input())
    if n%2==0:
        print("-1")
    else:
        print(*range(1, n // 2 + 1), *range(n, n // 2, -1))
    T-=1



# Binary to decimal

# s1 = "1011"
#
# dec = 0
# j = 0
# for i in range(len(s1)-1,-1,-1):
#     dec += int(s1[i]) * 2 ** j
#     j += 1
# print(dec)

# using an API

