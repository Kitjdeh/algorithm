import sys
sys.stdin = open("220923_정식이의 은행업무.txt")
def bi(A):
    n = len(A)
    for i in range(n):
        bi_ch = A[0::]
        if A[i] ==1:
            bi_ch[i] = 0
        elif A[i] ==0:
            bi_ch[i] = 1
        S = 0
        for j in range(n):
            S += bi_ch[j]* 2**(n-j-1)
        list_bi.append(S)
    return
def tri(A):
    n = len(A)
    for i in range(n):
        for j in range(1,3):
            tri_ch = A[0::]
            tri_ch[i] = (tri_ch[i]+j)%3
            S = 0
            for j in range(n):
                S += tri_ch[j]* 3**(n-j-1)
            list_tri.append(S)
    return


T = int(input())
for tc in range(1,T+1):
    arr_bi = list(input())
    arr_tri = list(input())
    for i in range(len(arr_bi)):
        if arr_bi[i] =='1':
            arr_bi[i] = 1
        else:
            arr_bi[i] = 0
    for i in range(len(arr_tri)):
        if arr_tri[i] =='1':
            arr_tri[i] = 1
        elif arr_tri[i] =='2':
            arr_tri[i] = 2
        else:
            arr_tri[i] = 0

    list_bi = []
    list_tri = []
    bi(arr_bi)
    tri(arr_tri)
    for i in list_bi:
        if i in list_tri:
            print(f'#{tc} {i}')