a = [4,5,6,7,8]
def comb(arr,r):
    for i in range(len(arr)):
        if r == 1:
            yield [arr[i]]
        else:
            for j in comb(arr[i+1:],r-1):
                yield [arr[i]] + j
for i in comb(a,3):
    print(i)