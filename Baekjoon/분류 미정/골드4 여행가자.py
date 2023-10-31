#I. x -> y 의 여행 계획이가능한지 확인하는 bfs(p,q)정의
#I-1. x의 adj 목록들 추출
#I-2. while q로 확인
#II. bfs 적용
#II-1. N,M 수령
#II-2. adj 함수 생성
#II-3. travel=[]에 경로 input()
#II-4. travel[0]과 travel[1]의 연결 여부 확인
#II-4-1. 연결 => pop(0)후 다시 진행
#II-4-2. 연결X => break NO 출력
#II-5. len(travel)=1이 된다면 종료

#I. x -> y 의 여행 계획이가능한지 확인하는 bfs(p,q)정의
def bfs(x,y):
    q = [x]
    # I-1. x의 adj 목록들 추출
    visited = [0]*(N)
    visited[x-1] =1
    # I-2. while q로 확인
    while q:
        v = q.pop(0)
        for i in range(N):
            if adj[v-1][i] ==1 and visited[i] ==0:
                visited[i] =1
                q.append(i+1)
        if visited[y-1] ==1:
            break
    if visited[y-1] == 1:
        return 1
    else:
        return 0

#II. bfs 적용
#II-1. N,M 수령
N = int(input())
M = int(input())
#II-2. adj 함수 생성
adj = [list(map(int,input().split())) for _ in range(N)]
#II-3. travel=[]에 경로 input()
travel = list(map(int,input().split()))

cnt = 1
#II-5. len(travel)=1이 된다면 종료
while len(travel) !=1:
    # II-4. travel[0]과 travel[1]의 연결 여부 확인
    p,q = travel[0],travel[1]
    # II-4-1. 연결 => pop(0)후 다시 진행
    if bfs(p,q):
        travel.pop(0)
    # II-4-2. 연결X => break NO 출력
    else:
        cnt =0
        break


if cnt == 0:
    print('NO')
else:
    print('YES')