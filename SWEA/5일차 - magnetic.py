"""
N극과 S극 둘 중 한종류만 있거나 없는 라인은 카운팅 대상이 아님
N의 개수와 S의 개수를 세로로 확인하여 둘다 존재하는 라인만 체크
0에서 100으로 가면서 N(=1)이 나온 후 S가 몇개인지 확인(N이 나오 기전 S극들은 N극으로 다 떨어지니)
100~0으로 가면서 S가 나온 후 N이 몇개인지 확인
두 숫자를 더하는 식 구함
"""
import sys
sys.stdin = open('magnetic.txt')
for tc in range(1,11):
    N = int(input())
    arr = [0]*100
    result = 0
    for i in range(N):
        arr[i] = list(map(int,input().split()))

    for i in range(N):
        upcnt = 0               #위에서 아래로 가면서 N극 성질이 나온 후 배열된 s의 수
        k = 0
        downcnt = 0
        p = 99
        stack = []
        while arr[k][i] != 1:
            k +=1
            if k==100:
                break
        for j in range(k,100):
            if arr[j][i] != 0:
                stack.append(arr[j][i])
        for t in range(len(stack)):

        while arr[k][i] != 2:
            p += -1
            if p==0:
                break
        for j in range(0,k):
            if arr[j][i] == 1:
                downcnt +=1
        result +=upcnt
        result +=downcnt
    print(result)
