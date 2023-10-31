# 가장 큰값들만 빼내어서 전부 방문하면
T = int(input())
for tc in range(1,T+1):
    max_sum = 0
    N = int(input())
    visited = [[0] * N] * 2
    arr = [0,0]
    arr[0] = list(map(int,input().split()))
    arr[1] = list(map(int,input().split()))
    direct = [-1, 0, 1]
    while True:
        hei = -1            #더이상 값이 없으면 break해야하니 확인용으로 음수처리
        wid = -1
        max_arr = 0
        for i in range(2):
            for j in range(N):
                if arr[i][j] > max_arr and visited[i][j] == 0:
                    max_arr = arr[i][j]
                    hei, wid = i, j
                if arr[i][j] == max_arr:                                                                #만약 같은 값들이 걸리면 주변 값들 합이 제일 큰놈을 살리기
                    ch1 = 0
                    ch2 = 0
                    for di in direct:
                        for dj in direct:
                            if -1 < i+di < 2 and -1 < j+dj < N-1 and visited[i+di][i+dj] ==0:
                                ch2 +=arr[i+di][j+dj]
                            if -1 < hei+di < 2 and -1 < wid+dj< N-1 and visited[hei+di][wid+dj] ==0:
                                ch1 +=arr[hei+di][wid+dj]
                    if ch2>ch1:
                        max_arr = arr[i][j]
                        hei, wid = i, j
        if wid <0 or hei <0 :
            break
        for di in direct:
            for dj in direct:
                ni = hei + di
                nj = wid + dj
                if -1 < ni < 2 and -1 < nj < N:
                    visited[ni][nj] = 1
        max_sum += arr[hei][wid]
    print(max_sum)