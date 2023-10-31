from sys import stdin
input = stdin.readline

def f(x,y,c):
    # 2-1. cnt 값이 maxV인지 우선 확인한다.
    global maxV
    if maxV < len(dict_visited):
        maxV = len(dict_visited)
    # 3. 동서남북 좌표를 for문으로 확인한다.
    for di,dj in direction:
        ni,nj = x+di,y+dj
        # 4-1. idx 값이 문제 없으며
        if 0<=ni<R and 0<=nj<C:
            # 4-2. board[ni][nj]가 dict_a에 없으면
            # word = board[ni][nj]
            if dict_visited.get(board[ni][nj]) ==None:
                # 4-3. 해당 값을 dict_a에 넣는다.
                dict_visited[board[ni][nj]]=1
                # 5. 재귀를 넣으면서 cnt를 +1 한다.
                f(ni,nj,c+1)
                # 6. 재귀가 끝나면 del을 하여 다른 변수에 영향을 주지 않게한다.
                # del(dict_visited[board[ni][nj]])

# 1. R,C값과 board 값을 받는다.
R,C = map(int,input().split())
board = [list(input()) for _ in range(R)]
direction=[[1,0],[-1,0],[0,1],[0,-1]]
dict_visited={}
first_word = board[0][0]
dict_visited[first_word] = 1
maxV=0
f(0,0,1)
print(maxV)