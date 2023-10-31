def blend(A,r):
    L = len(A)
    if r == L-1:
        ord.append(A[0::])
    else:
        for i in range(r,L):
            if A[i] ==A[r]:
                blend(A,r+1)
                return
            else:
                A[i], A[r] = A[r], A[i]
                blend(A, r + 1)
                A[i], A[r] = A[r], A[i]
def blending(A,r):
    L = len(A)
    if r == L-1:
        ord.append(A[0::])
        return
    else:

arr =[i for i in range(10)]
result =[]
# print(comb(arr,10,3))
a = [1,5,1,1,5]
b = [1,2]
ord=[]
blend(a,0)
print(ord)
print(len(ord))