# M개의 여행을 출발 순으로 정렬
# M개의 여행 중 i 번째 여행을 갈 경우
# 곂치지 않는 처음 여행을 그 다음 여행으로 잡는다.
# 각 여행을 잡을 때 마다 간격의 값을 확인
# 여러 간격 중 가장 큰 값을 D[i]의 값으로 설정
# i 다음 i+2이 곂치지 않는 경우
# i+1 다음 i+3가 곂치지 않는 경우
N = int(input())
M = int(input())
schedule = [0]*M
for i in range(M):
    p,q = map(int,input().split())
    schedule[i] = [p,q]
schedule.sort(key = lambda x : (x[0],-x[1]))
