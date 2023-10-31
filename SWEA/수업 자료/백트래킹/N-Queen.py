def backtracking(y, x, arr, N):  # arr[y][x] visited 시 다음 놓는 곳을 확인
    global result
    if y == N - 1:
        result += 1
        return
    else:
        # arr[y+1] 에 놓을 수 있는 곳을 찾아야하니 0~N-1까지 확인을 해야함
        for i in range(N):
            ch = 0
            # 3가지 방향중 한개를 잡고
            for di, dj in dir:
                ni, nj = y + 1, i
                # 0~y 까지 총 y+1번 확인해야한다.
                for j in range(y + 1):
                    ni += di
                    nj += dj
                    # 해당 방향으로 계속 더하다가 1인 곳이 나오면 ch에 넣어 체크
                    if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] == 1:
                        ch += 1
                        break
            # 1이 하나라도 나오면 중복이니 중단
            if ch != 0:
                # print(tc,arr)
                pass
            # 3방향 다 안걸리면 ch ==0
            else:
                arr[y + 1][i] = 1
                backtracking(y + 1, i, arr, N)
                arr[y + 1][i] = 0


dir = [[-1, -1], [-1, 1], [-1, 0]]
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    board = [[0] * N for _ in range(N)]
    result = 0
    for i in range(N):
        board[0][i] = 1
        backtracking(0, i, board, N)
        board[0][i] = 0
    print(f'#{tc} {result}')