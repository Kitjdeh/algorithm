import sys
sys.stdin = open("백만장자 프로젝트.txt")
def f(a):
    if len(a)==0:
        return False

    global result
    max_idx = 0
    max_v=0
    for i in range(len(a)):
        if max_v < a[i]:
            max_idx = i
            max_v = a[i]
    for j in range(max_idx):
        result +=max_v-a[j]
    b = a[max_idx+1:]
    if len(b) != 0:
        f(b)
T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = list(map(int,input().split()))
    result = 0
    f(arr)
    print(f"#{tc} {result}")