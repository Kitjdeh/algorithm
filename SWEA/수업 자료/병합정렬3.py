def msort(A):
    N = len(A)
    if N==1:                #원소가 한 ㅏ남은 경우 분할 중지
        return A
    else:
        left = A[0:N//2]                        #반반
        right = A[N//2:N]
        left = msort(left)                      #반반을 정리한 거
        right = msort(right)
        A =[]

        while len(left) > 0 and len(right) > 0 : #양쪽에 원소가 있으면
            if left[0] < right[0]:
                A.append(left.pop(0))
            else:
                A.append(right.pop(0))
        if len(left)>0:
            A += left
        if len(right) > 0:
            A += right
        return  A

T= int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = list(map(int,input().split()))
    arr = msort(arr)
    print(arr)