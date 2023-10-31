a = [i for i in range(1,11)]
def comb(arr,r):
    result = []
    if r > len(arr):
        return result
    if r ==1:
        for i in arr:
            result.append([i])
    elif r >1:
        for i in range(len(arr)-r+1):
            for j in comb(arr[i+1:],r-1):
                print(i,j,arr[i])
                result.append([arr[i]] + j)
                print(result)
    return result
print(comb(a,3))



#     for i in range(len(arr)):
#         if r == 1:
#             yield [arr[i]]
#         else:
#             for j in comb(arr[i+1:],r-1):
#                 yield [arr[i]] + j
# for i in comb(a,3):
#     print(i)