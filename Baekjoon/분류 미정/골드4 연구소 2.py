#1-1. nCr 함수 정의
#1-2. 바이러스를 놓을 수 있는 2 지점의 좌표를 수집
#1-3. 전체 바이러스가 퍼질 수 있는
#2. nCm으로 바이러스를 둘 지점을 고르는 모든 경우의 수를 파악
#3. 각 경우의 수 마다 해당 위치가 바이러스인 3으로 설정
#3-1. 깊은 복사로 설정
#3-2.
# 바이러스를 둔 후 BFS로 분산시킨후 걸리는 시간을 파악한다.







#1-1 nCr 함수 정의
def combination(arr,r):
    result = []
    if r==1:
        for i in arr:
            result.append([i])
    elif r >1:
        for i in range(len(arr)-r+1):
            for j in combination(arr[i+1:],r-1):
                result.append([arr[i]]+j)
    return result

N,M = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
#1. 바이러스를 놓을 수 있는 2지점의 좌표 수집
culture =[]
# 종료 지점을 파악하기 위해 더 퍼질 바이러스가 있는지 확인하는 cnt 값 확인
total_cnt= 0
for i in range(N):
    for j in range(N):
        if arr[i][j] == 2:
            culture.append([i,j])
            total_cnt +=1
        elif arr[i][j] == 1:
            arr[i][j] = '-'
        else:
            total_cnt +=1
virus_group = combination(culture,M)
print(viru)
L = len(virus_group)
min_time = 10000000000
while virus_group:
    #3-1. 깊은복사하여 해당 값을 3으로 변경
    virus = virus_group.pop(0)
    list_vir = [[] for _ in range(N)]
    for j in range(N):
        list_vir[j] = arr[j][:]
    for i in range(M):
        x,y = virus[i][0],virus[i][1]
        list_vir[x][y] = 3
    # for i in range(N):
    #     print(list_vir[i])
    cnt = M
    parasite_time =0
    # 턴제로
    while total_cnt != cnt:
        # 퍼진 지점에서 3인 값들은 전부 퍼지게 한다.
        new_virus = []
        for vir in virus:
            x,y = vir[0],vir[1]
            for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
                ni,nj = x+di,y+dj
                if 0<=ni<N and 0<=nj<N and list_vir[ni][nj] != '-' and list_vir[ni][nj] != 3:
                    list_vir[ni][nj] = 3
                    #감연된 좌표 저장
                    new_virus.append([ni,nj])
                    cnt +=1
        #지금 있는 바이러스 다 퍼졌으니 다음 턴으로 가야하니 시간 +1
        parasite_time +=1
        #감염 된 곳에서 다시 시작해야하는데 감연 된것이 없으면 끝
        if new_virus == []:
            break
        #감연된 곳에서 다시 시작
        virus = new_virus
        #시간 더걸리면 볼 필요 없으니 컷
        if min_time < parasite_time:
            break
    #숫자가 다르면 덜 감연된거니 패스
    if total_cnt !=cnt:
        pass
    elif min_time > parasite_time:
        min_time = parasite_time
if min_time== 10000000000:
    print(-1)
else:
    print(min_time)

    # [3, 0, 3, 0, '-', '-', 0]
    # [0, 0, '-', 0, '-', 3, 0]
    # [0, '-', '-', 3, '-', 0, 0]
    # [2, '-', 0, 0, 0, 0, 2]
    # [0, 0, 0, 2, 0, '-', '-']
    # [0, '-', 0, 0, 0, 0, 0]
    # [2, '-', 0, 0, 2, 0, 2]