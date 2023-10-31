def f(i,N,e,cnt):
    global result
    if i ==N:
        if result >cnt and e>=0:
            result =cnt
        return
    else:
        if e <0 or cnt>=result:
            return
        elif e ==0:
            f(i+1,N,arr[i]-1,cnt+1)             #정류장에서 교체
        else:
            f(i+1,N,arr[i]-1,cnt+1)             #정류장에서 교체
            f(i+1,N,e-1,cnt)                    #정류장에서 교체X
T = int(input())
for tc in range(1,T+1):
    arr = list(map(int,input().split()))
    N = arr[0]
    result = N
    f(2,N,arr[1]-1,0)                           #출발지 제외
    print(f'#{tc} {result}')
