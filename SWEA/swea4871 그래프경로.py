import sys
sys.stdin = open('swea4871 그래프경로.txt')
def nod(N):                                             #경로2개이상인지 확인
    k= 0
    for i in range(E):
        if dir[i][0] ==N:
            k +=1
    if k>1:
        return True
    else:
        return False
T= int(input())
for tc in range(1,T+1):
    V,E = map(int,input().split())
    dir = [0] * E
    for i in range(E):
        dir[i] = (list(map(int,input().split())))       #node 값들 리스트화
    S, G = map(int,input().split())
    wp = S                                              #이동 위치 wp
    visited = [False]*V                                 #방문 기록
    stack = []                                          #현재위치의 노드 확인 stack
    visited[S-1] = True
    if nod(wp) == True:
        stack.append(wp)
    while True:
        mov = 0
        if wp == G:                                     #1. wp 가 G인경우
            result = 1
            break
        for i in range(E):                              #2 전진할 곳이 있는경우
            if (dir[i][0] == wp) and (visited[dir[i][1]-1] == False):
                wp = dir[i][1]
                visited[dir[i][0] - 1] = True
                mov = 1
                if nod(wp) == True:
                    stack.append(wp)
                    break
        if mov != 1:                                    #3. 진행할 곳이 없고 스택이 없어 뒤로 갈 수 없는 경우
            if len(stack) == 0:
                result = 0
                break
            else:                                       #4. 진행할 곳이 없고 스택이 있어 뒤로 갈 수 있는 경우
                wp = stack.pop()
    if result == 0:
        print(f'#{tc} 0')
    else:
        print(f'#{tc} 1')

