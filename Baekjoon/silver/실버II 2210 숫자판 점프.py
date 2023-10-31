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
direct = [[-1,0],[1,0],[0,1],[0,-1]]
list_arr = [list(input().split()) for _ in range(5)]
result = []
for i in range(5):
    for j in range(5):
        for k in Pi(direct,5):
            a = list_arr[i][j]
            ni,nj = i,j
            for t in range(5):
                ni += k[t][0]
                nj += k[t][1]
                if 0 <= ni <5 and 0<= nj <5:
                    a += list_arr[ni][nj]
            # for t in result:
            #     if a == result:
            #         a = ''
            if len(a)==6:
                result.append(a)
result = set(result)
print(len(result))