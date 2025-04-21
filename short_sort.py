T = int(input())

while T:
    str = input()
    position = 0
    if str[0] != 'a':
        position += 1
    if str[1] != 'b':
        position += 1
    if str[2] != 'c':
        position += 1

    print("YES" if mismatch_count <= 2 else "NO")
    position = 0
    T -= 1