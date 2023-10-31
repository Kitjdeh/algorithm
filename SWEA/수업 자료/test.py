def comb(arr,N):
    result =[]
    if N ==1:
        for i in range(len(arr)):
            result.append([arr[i]])
    else:
        for i in range(len(arr)-N+1):
            for j in comb(arr[i+1:],N-1):
                result.append([arr[i]]+j)
    return result
arr = [i for i in range(10)]
result = []

# print(comb(arr,3))
P= [ i for i in range(4)]
ord = []
def order(i,N):
    if i == N:
        ord.append(P[0::])
        return
    else:
        for j in range(i,N):
            P[i],P[j] = P[j],P[i]
            order(i+1,N)
            P[i], P[j] = P[j], P[i]
order(0,4)
print(ord)