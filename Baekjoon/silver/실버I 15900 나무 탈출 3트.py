import sys

N = int(sys.stdin.readline())
par = [0] * (N + 1)  # par[자식놈 인덱스] = 부모인덱스
ch = [0] * (N + 1)  # ch[부모 인덱스] = 자식인덱스
arr = [0] * (N + 1) # 노드와 연관 관계인 점
for i in range(N - 1):
    a, b= map(int, sys.stdin.readline().split())  # input 수령
    arr[a] +=[b]
    arr[b] +=[a]
stack = [1]
while True:
