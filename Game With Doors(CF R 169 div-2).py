# T = int(input())
#
# while T:
#     A = list(map(int,input().split()))
#     B = list(map(int,input().split()))
#
#     # case 1 : when two bounds are in the same region
#     if A[0] == B[0] and A[1] == B[1]:
#         print(A[1]-A[0])
#     # case 2: when two bounds are in different regions
#     if A[1] < B[0]:
#         print(B[0]-A[1])
#     if B[1] < A[0]:
#         print(B[1]-A[0])
#     # case 3: overlapping bounds
#     # sub-case1: bound 1 is in the middle of bound 2 or vice versa
#     if A[0] < B[0] and A[1] > B[1]:
#         print(B[1]-B[0]+2)
#     if B[0] < A[0] and B[1] > A[1]:
#         print(A[1]-A[0]+2)
#     # sub-case2: if any of the bound is from the middle to the one end
#     if A[0] == B[0]:
#         if A[1] > B[1]:
#             print(B[1]-B[0]+1)
#         elif B[1] > A[1]:
#             print(A[1]-A[0]+1)
#     if A[1] == B[1]:
#         if A[0] < B[0]:
#             print(B[1]-B[0]+1)
#         elif B[0] < A[0]:
#             print(A[1]-A[0]+1)
#     T -= 1

T = int(input())
while T:
    l,r = map(int,input().split())
    L,R = map(int,input().split())
    result = max(min(r,R)-max(L,l) + int(L!=l) + int(R!=r),1)
    print(result)
    T -= 1
