T = int(input())
for tc in range(1,T+1):
    W,N = map(int,input().split())
    arr = []
    for i in range(N):
        arr.append(list(map(int,input().split())))
    total_len = 0
    stack = 0
    total_len +=arr[0][0]                       #처음은 무조건 가야하니 거리를 통으로 넣음
    stack +=arr[0][1]                           #처음은 무조건 가니 쓰레기를 담음
    for i in range(1,N):                #i번째 쓰레기를 담기 직전
        if stack !=0 and stack+arr[i][1] >W:        #stack에 쓰레기(arr[i][1])를 더하면 W보다 클경우
            total_len += arr[i][0] - arr[i - 1][0]  # 우선 i-1에서 i까지 간거리
            total_len +=arr[i][0]*2                 #일단 버리고 와야하니 왔다 갔다 2번
            stack = arr[i][1]                       #쓰레기 버리고 새로 채웠으니 arr[i][1]
        elif stack !=0 and stack+arr[i][1] < W:     #담아도 널널하고 i-1에서 바로 온 경우.
            total_len += arr[i][0] - arr[i - 1][0]
            stack +=arr[i][1]
        elif stack ==0 and stack +arr[i][1] ==W and i <N-1:       #버리고 왔는데 다 담으면 딱 맞을 경우
            total_len += arr[i][0] + arr[i - 1][0]
            stack =0
        elif stack !=0 and stack +arr[i][1] ==W and i <N-1:        #바로 왔는데 다 담으면 딱 맞을 경우
            total_len += arr[i][0] - arr[i - 1][0]  # i-1에서 i까지 간거리
            total_len += arr[i][0]
            stack +=0
    total_len +=arr[N-1][0]              #끝났으니 돌아가는 거리
    print(total_len)

