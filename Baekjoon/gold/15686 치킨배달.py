#각 집에서 치킨집과의 거리는 for N번으로 확인 가능
#각집의 치킨거리를 구하여 치킨거리 Chick_distance 계산가능
#폐업시켜야 하는 치킨집-> 치킨거리의 변동이 최소화 되는 집
N,M = map(int,input().split())
arr = [[0]*N for _ in range(N)]
consumer = []
Chicken = []
for i in range(N):
    arr[i] = list(map(int,input().split()))
    for j in range(N):
        if arr[i][j]==1:
            consumer.append([i,j])
        elif arr[i][j]==2:
            Chicken.append([i,j])
Total_distance=0
for i in range(len(consumer)):
    Chicken_distance = N*N
    for j in range(len(Chicken)):
        distance = abs(consumer[i][0]-Chicken[j][0]) +abs(consumer[i][1]-Chicken[j][1])
        if Chicken_distance>distance:
            Chicken_distance=distance
    Total_distance +=Chicken_distance
min_distance=Total_distance
cnt_Chicken =len(Chicken)
for _ in range(cnt_Chicken-M):
    min_distance = 10000
    loser = -1
    for t in range(len(Chicken)):
        lost_chicken = Chicken[0:]
        print(lost_chicken)
        lost_chicken.pop(t)
        t_distance=0
        for i in range(len(consumer)):
            Chicken_distance = N * N
            for j in range(len(lost_chicken)):
                distance = abs(consumer[i][0] - lost_chicken[j][0]) + abs(consumer[i][1] - lost_chicken[j][1])
                if Chicken_distance > distance:
                    Chicken_distance = distance
            t_distance +=Chicken_distance
        if min_distance > t_distance :
            min_distance = t_distance
            loser = t
        elif min_distance == t_distance and t > -1:
            min_total = 0
            t_total = 0
            for i in range(len(consumer)):
                min_total += abs(consumer[i][0]-Chicken[loser][0])+abs(consumer[i][1]-Chicken[loser][1])
                t_total += abs(consumer[i][0]-Chicken[t][0])+abs(consumer[i][1]-Chicken[t][1])
            if min_total < t_total:
                loser = t
        print(t,t_distance,loser,min_distance)

    Chicken.pop(loser)
print(min_distance)





