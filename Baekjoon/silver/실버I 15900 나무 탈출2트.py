import sys
N = int(sys.stdin.readline())
par = [0]*(N+1)                                     # par[자식놈 인덱스] = 부모인덱스
ch = [0]*(N+1)                                      # ch[부모 인덱스] = 자식인덱스
h = [0]*(N+1)                                       # h[본인 인덱스] = 몇대손인지 (1은 0대손)
arr = [0]*(N-1)
for i in range(N-1):
    arr[i] = list(map(int,sys.stdin.readline().split()))         #input 수령
t = [1]
result = 0
while len(t)>0:
    cnt = 0
    for i in range(len(arr)):
        if t[0] in arr[i] and len(arr[i])==2:       #아직 찢지 못한 부모(t[0])와 자식놈(arr[i]의 다른수)가 있다?
            arr[i].remove(t[0])                     #부모 캇 -> 남은건 자식놈
            # par[arr[i][0]] = t[0]                   #부모par에 넣음
            ch[t[0]]=arr[i][0]                      #ch[부모 인덱스] = 자식인덱스
            h[arr[i][0]] = h[t[0]] +1           #진행해온 높이h에 1추가 ->자식놈 생겼으니
            t.append(arr[i][0])
            cnt =1
    if cnt == 0:
        result +=h[t[0]]
    t.pop(0)                                        #t[0]이 부모인거 다 정리했으니 버리기
# result =0
# for i in range(1,N+1):                              #자손없는놈 고르기
#     if ch[i] ==0:
#         result +=h[i]
print(result)
if result % 2 == 0:
    print("No")
else:
    print("Yes")
    # if max_h < h[arr[i][0]]:
    #     max_h = h[arr[i][0]]
    #     cnt = 1
    # elif max_h == h[arr[i][0]]:
    #     cnt +=1
# def f(N):
#     global cnt
#     if N ==1:
#         return cnt
#     else:
#         f(par[N])
#         cnt +=1
#
# result = Goja(N):
# for i in result:
#     f(i)
# if cnt %2 == 0:
#     print("No")
# else:
#     print("Yes")
#
