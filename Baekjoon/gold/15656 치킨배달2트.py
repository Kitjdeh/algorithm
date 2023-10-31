def comb(arr,r):
    result=[]
    if r == 1:
        for i in arr:
            result.append([i])
    elif r > 1 :
        for i in range(len(arr)-r+1):
            for j in comb(arr[i+1:],r-1):
                result.append([arr[i]]+j)
    return result
N, M = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
consumer=[]
chicken = []
for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            consumer.append([i,j])
        elif arr[i][j] ==2 :
            chicken.append([i,j])

max_distance = 10000

for combination in comb(chicken,M):                     #M개의 치킨집을 남기는 모든 경우의 수를 for문 돌림
    chic_distance = 0
    for consume in consumer:                            #거리를 측정할 소비자집
        short_distance = 1000
        for chic in combination:                        # M개의 치킨집이 있는 경우 combination의 모든 치킨집을 돌아볼 chic
            t_distance = abs(consume[0]-chic[0])+abs(consume[1]-chic[1])    #consume과 chic 사이 거리 측정
            if short_distance > t_distance:                                 #consum한테 제일짧은 chic 거리 확인
                short_distance = t_distance
        chic_distance += short_distance                                     #각 consume들의 제일 짧은 chic거리 더하기

    if max_distance > chic_distance:                                        #제일 짧은 chic_distacne경우 찾기
        max_distance = chic_distance
print(max_distance)

