def order(i,N):
    if i ==N:
        ord.append(P[0::])
        return
    else:
        for j in range(i,N):
            P[i],P[j] = P[j],P[i]
            order(i+1,N)
            P[i],P[j] = P[j],P[i]
#P = [0,1,2]# 1,2,3배치 순열
# order(0,3)
# print(ord)
# [[0, 1, 2], [0, 2, 1], [1, 0, 2], [1, 2, 0], [2, 1, 0], [2, 0, 1]]
def comb(arr,r):
    result = []
    if r ==1:
        for i in arr:
            result.append([i])
    elif r >1:
        for i in range(len(arr)-r+1):
            for j in comb(arr[i+1:],r-1):
                result.append([arr[i]] + j)
    return result

# arr = [i for i in range(1,4)]
# print(comb(arr,2))
# [[1, 2], [1, 3], [2, 3]]
def permute(arr,r):
    result = []
    if r == 1:
        for i in arr:
            result.append([i])
    elif r >1:
        for i in range(len(arr)):
            for j in permute(arr,r-1):
                if arr[i] not in j:
                    result.append([arr[i]]+j)
    return result

# arr = [i for i in range(1,4)]
# print(permute(arr,2))
# [[1, 2], [1, 3], [2, 1], [2, 3], [3, 1], [3, 2]]
def Pi(arr,r):
    result = []
    if r ==1:
        for i in arr:
            result.append([i])
    elif r > 1:
        for i in range(len(arr)):
            for j in Pi(arr,r-1):
                result.append([arr[i]] + j)
    return result
# arr = [i for i in range(1,4)]
# print(Pi(arr,2))
# [[1, 1], [1, 2], [1, 3], [2, 1], [2, 2], [2, 3], [3, 1], [3, 2], [3, 3]]



arr = [i for i in range(1,4)]

print(comb(arr,2))
print(permute(arr,2))
print(Pi(arr,2))
ord=[]
P = [0,1,2]# 1,2,3배치 순열
order(0,3)
print(ord)
