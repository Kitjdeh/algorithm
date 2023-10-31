N = int(input())
arr = [0]*N
for i in range(N):
    arr[i] = list(input().split())
q = list(input().split())
#돌아가면서 arr[i][0]을 확인해서 맞으면 pop한다.
#멈추는 조건 1. 한바퀴를 돌았는데 하나도 안나올경우
#멈추는 조건 2. 문장들을 다 사용하였을 경우
cnt = 0
while cnt <N:
    for i in range(N):
        if arr[i] == []:
            cnt +=1
        elif q ==[]:
            cnt +=N
            continue
        elif arr[i][0] == q[0]:
            arr[i].pop(0)
            q.pop(0)
            cnt = 0

        else:
            cnt +=1
ch = 0
for i in range(N):
    ch +=len(arr[i])
if len(q) ==0 and ch ==0:
    print("Possible")
else:
    print("Impossible")