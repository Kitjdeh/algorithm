import sys

N = int(sys.stdin.readline())
par = [0] * (N + 1)  # par[자식놈 인덱스] = 부모인덱스
ch = [0] * (N + 1)  # ch[부모 인덱스] = 자식인덱스
arr = [0] * (N - 1)
for i in range(N - 1):
    arr[i] = list(map(int, sys.stdin.readline().split()))  # input 수령
stack = []
t = [1]
max_h = 0
while len(t) > 0:
    for i in range(len(arr)):
        if t[0] in arr[i] and len(arr[i]) == 2:
            arr[i].remove(t[0])
            par[arr[i][0]] = t[0]
            ch[t[0]] = arr[i][0]
            t.append(arr[i][0])
    t.pop(0)

cnt = 0


def Goja(N):
    Gj = []
    for i in range(1, N + 1):
        if ch[i] == 0:
            Gj.append(i)
    return Gj


def f(N):
    global cnt
    if N == 1:
        return cnt
    else:
        f(par[N])
        cnt += 1


result = Goja(N)
for i in result:
    f(i)
print(cnt)
if cnt % 2 == 0:
    print("No")
else:
    print("Yes")