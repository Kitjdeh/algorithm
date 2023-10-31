T = int(input())
for tc in range(1,T+1):
    a,b,c,d = map(int,input().split())
    arr= [0]*101
    cnt = 0
    for i in range(a,b+1):
        arr[i] +=1
    for i in range(c,d+1):
        arr[i] +=1
    for i in range(101):
        if arr[i] ==2:
            cnt+=1
    if cnt == 0:
        result =0
    else:
        result = cnt-1
    print(f"#{tc} {result}")
