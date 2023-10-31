def order(i,N):
    # global ord
    if i ==N:
        ord.append(P[0::])
        return
    else:
        for j in range(i,N):
            P[i],P[j] = P[j],P[i]
            order(i+1,N)
            P[i],P[j] = P[j],P[i]
# 거리를 구하여 result 함수에 append
def comb(arr,r):
    result = []
    # if r > len(arr):
    #     return result
    if r ==1:
        for i in arr:
            result.append([i])
    elif r >1:
        for i in range(len(arr)-r+1):
            for j in comb(arr[i+1:],r-1):
                result.append([arr[i]] + j)
    return result
# def permute(arr,r):
#     result = []
#     if r == 1:
#         for i in arr:
#             result.append([i])
#     elif r >1:
#         for i in range(len(arr)):
#     return



arr = [i for i in range(5)]
print(comb(arr,3))

ord=[]
P = [0,1,2,2]# 1,2,3배치 순열
order(0,4)
print(ord)
