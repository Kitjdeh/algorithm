"""
N극과 S극 둘 중 한종류만 있거나 없는 라인은 카운팅 대상이 아님
N의 개수와 S의 개수를 세로로 확인하여 둘다 존재하는 라인만 체크
0에서 100으로 가면서 N(=1)이 나온 후 S가 몇개인지 확인(N이 나오 기전 S극들은 N극으로 다 떨어지니)
100~0으로 가면서 S가 나온 후 N이 몇개인지 확인
두 숫자를 더하는 식 구함
"""
import sys
sys.stdin = open('magnetic.txt')
for tc in range(1, 11):
    N = int(input())
    arr = [0] * 100
    result = 0
    for i in range(N):
        arr[i] = list(map(int, input().split()))

    for j in range(N):
        stack = []
        ch = []
        for i in range(N):
            if arr[i][j] != 0:
                stack.append(arr[i][j])             #1과2를 순서대로 받는다.
        while stack[0] != 1:                        #stack의 index[0] 방향은 N극이니 N성분이 나오기 전 S들은 다 떨어진다.
            stack.pop(0)
        while stack[-1] != 2:                       #stack의 index[-1] 방향은 S극이니 S성분이 나오기 전 N들은 다 떨어진다.
            stack.pop()
        for i in range(len(stack)):
            if stack[i]==1 and stack[i+1] ==2:      #충돌 일어나는 기점이니 1이나 2 중 한개를 기준으로 다른 수가 나오는 지점 들만 카운팅한다.
                result +=1

    print(f"#{tc} {result}")