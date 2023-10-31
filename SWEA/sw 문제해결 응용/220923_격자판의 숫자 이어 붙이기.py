def f(x,y,result):
    global ord
    global cnt
    direction = [[-1,0],[1,0],[0,1],[0,-1]]

    if len(result)==7:
        if result in ord:
            return
        else:
            ord.append(result)
            return
    else:
        for j in range(4):
            ni,nj =x+direction[j][0],y+direction[j][1]
            if 0<=ni<4 and 0<=nj<4:
                f(ni,nj,result+arr[ni][nj])

T = int(input())
for tc in range(1,T+1):
    arr = [list(input().split()) for _ in range(4)]
    ord = []
    result = ''
    for i in range(4):
        for j in range(4):
            f(i,j,arr[i][j])
    print(f'#{tc} {len(ord)}')

# def dfs(s_i, s_j, n, k, arr):
#     global check
#
#     if n == k:
#         check.add(''.join(arr))
#     else:
#         for l in range(4):
#             ni, nj = s_i + di[l], s_j + dj[l]
#             if 0 <= ni < 4 and 0 <= nj < 4:
#                 dfs(ni, nj, n + 1, k, arr + [area[ni][nj]])
#
#
# di = [-1, 1, 0, 0]
# dj = [0, 0, -1, 1]
#
# for tc in range(1, int(input()) + 1):
#     area = [list(input().split()) for _ in '_' * 4]
#
#     check = set()
#
#     for i in range(4):
#         for j in range(4):
#             dfs(i, j, 0, 6, [area[i][j]])
#
#     print(f'#{tc} {len(check)}')
