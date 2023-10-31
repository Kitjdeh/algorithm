import sys
sys.stdin = open("220923미생물 격리.txt")
dir = {
    1:[-1,0],
    2:[1,0],
    3:[0,-1],
    4:[0,1]
}
T = int(input())
for tc in range(1,T+1):
    N,M,K = map(int,input().split())
    arr =[list(map(int,input().split())) for _ in range(K)]
    ch_map = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            ch_map[i][j] = [0]

    for i in range(K):
        ch_map[arr[i][0]][arr[i][1]].append(i)
        ch_map[arr[i][0]][arr[i][1]].pop(0)
    t = 0
    while T != M:
        overlap = []
        L = len(arr)
        for i in range(L):
            ch_map[arr[i][0][arr[i][0]]].pop(0)
            arr[i][0],arr[i][1] = arr[i][0]+dir[arr[i][3]][0],arr[i][1]+dir[arr[i][3]][1]
            ch_map[arr[i][0]][arr[i][1]].append(i)
            if arr[i][0] == 0 or arr[i][1] ==0 :
                arr[i][2] = int(arr[i][2]/2)
        for i in range(N):
            for j in range(N):
                if len(ch_map[i][j]) >1:
                    max_cell = 0
                    max_idx = 0
                    for t in range(len(ch_map[i][j])):
                        if arr[ch_map[i][j][t]][3] > max_cell:
                            max_cell = arr[ch_map[i][j][t][3]]
                            max_idx = ch_map[i][j][t]
                    for t in range(len(ch_map[i][j])):


