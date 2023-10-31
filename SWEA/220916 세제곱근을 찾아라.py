T = int(input())
arr = [[i,i**3] for i in range(1,10**6+1)]
for tc in range(1,T+1):
    N = int(input())
    result =0
    for i in arr:
        if i[1] ==N:
            result = i[0]
    if result == 0:
        print(f"#{tc} -1")
    else:
        print(f"#{tc} {result}")
T = int(input())
for tc in range(1,T+1):
    N = int(input())
    result =0
    for i in range(1,N+1):
        if i**3 == N:
            result = i
        elif i**3 >N:
            break
    if result != 0:
        print(f"#{tc} {result}")
    else:
        print(f'#{tc} -1')
