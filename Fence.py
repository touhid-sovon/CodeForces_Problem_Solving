# n, k = map(int,input().split())
# h = list(map(int,input().split()))
# min_height = 999999
# min_index = 0
#
# for i in range (0,len(h)-k):
#     cur_height = 0
#     j = i
#     while j < (i+k) :
#         cur_height += h[j]
#         j += 1
#
#     if cur_height < min_height :
#         min_height = cur_height
#         min_index = i
#
# print(min_index+1)
#


h =list (map(int,input().split()) )

print(h)