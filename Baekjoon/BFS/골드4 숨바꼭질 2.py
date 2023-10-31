from collections import deque

#1. N에서 갈 수 있는 곳은 N-1, N+1, 2*N 3가지
#2. 한턴에 *3곳을 방문 하여 visited 처리
#3. K값이 나올 때 가지의 cnt를 구한다.


#1.input 수령
#2.while visited[K] == 0: 의 순환을 시작
#3.q에서 점 x pop
#4.x의 3가지 x+1,x-1,2*x 값 생성
#5.visited여부 확인하여 visited하지 않으면 many에 값을 추가
#6.temp에 중복 되지 않도록 many[x] 가 0일 경우만 추가
#7.다시 q = temp로 변경하며 이제 visited에 넣는다 (한턴(cnt)에 visited를 한번에 처리)



#1.input 수령
N,K = map(int,input().split())

visited = [0]*100001
many = [0]*100001
p= [N]
visited[N] =1
many[N] =1
cnt = 0
q = deque(p)
temp = deque([])
#2.while visited[K] == 0: 의 순환을 시작
while visited[K]==0:
    cnt += 1
    while q:
        # 3.q에서 점 x pop
        x = q.popleft()
        # 4.x의 3가지 x+1,x-1,2*x 값 생성
        a,b,c = x-1,x+1,x*2
        extension = [a,b,c]
        for i in extension:
            # 5.visited여부 확인하여 visited하지 않으면 many에 값을 추가
            if 0<=i<=100000 and visited[i] == 0:

                # 6.temp에 중복 되지 않도록 many[x] 가 0일 경우만 추가
                if many[i] ==0:
                    temp.append(i)
                many[i] += many[x]

    # 7.다시 q = temp로 변경하며 이제 visited에 넣는다 (한턴(cnt)에 visited를 한번에 처리)
    while temp:
        c = temp.popleft()
        q.append(c)
        visited[c] = 1

print(cnt)
print(many[K])


# N,K = map(int,input().split())
#
# visited = [0]*100001
#
# q= [N]
# visited[N] =1
# cnt = 0
# method = 0
# while visited[K]==0:
#     temp = []
#
#     while q:
#         x = q.pop(0)
#         a,b,c = x-1,x+1,x*2
#         extension = [a,b,c]
#         for i in extension:
#             if 0<i<100000 and visited[i] == 0:
#                 visited[i] = 1
#                 temp.append(i)
#             if i ==K:
#                 method +=1
#     cnt +=1
#     q = temp
# print(cnt)
# print(method)
