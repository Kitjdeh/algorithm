def msort(A):
    global cnt
    N = len(A)
    if N ==1:
        return A
    else:
        left = A[0:N//2]
        right = A[N//2:N]
        left = msort(left)
        right = msort(right)
        A = []
        if left[-1] > right[-1]:
            cnt+=1
        while len(left)>0 and len(right)>0:
            if left[0] < right[0]:
                A.append(left.pop(0))
            else:
                A.append(right.pop(0))
        if len(left)>0:
            A += left
        if len(right)>0:
            A += right
        return A
T= int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = list(map(int,input().split()))
    cnt = 0
    arr = msort(arr)
    print(f'#{tc} {arr[N//2]} {cnt}')