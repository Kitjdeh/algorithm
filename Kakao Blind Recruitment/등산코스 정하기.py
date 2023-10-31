#출입로에서 산봉우리까지 가면서 등산로에서 제일 큰 간격의 값이 최소가 되는 산봉우리 지점과 그때의 간격을 구하기
#? 출입로에서 시작하거나 산봉우리에서 시작하거나 똑같음
#산봉우리summits에서 for문 돌리면 계산이 편할듯..?
#함수 DFS에 산봉우리 summits[i]값을 넣으면 dfs로 gates 까지 내려가면서 gates 도착시 가장 큰 거리를 instance에 넣는다.
#가장 큰 거리 instance값은 가지치기로 이미 높으면 걍 거르게 함
#
n=6
paths=[[1, 2, 3], [2, 3, 5], [2, 4, 2], [2, 5, 4], [3, 4, 4], [4, 5, 3], [4, 6, 1], [5, 6, 1]]
gates=[1,3]
summits=[5]


def solution(n,paths,gates,summits):
    result = [0,0]
    def dfs(x,max_length,result):
        for summit_start, dis in adj[x]:
            q = [[summit_start,dis]]
            root_max = dis
            visited=[0]*(n+1)
            visited[x] = 1
            visited[summit_start] = 1
            ch =0
            while q and root_max<max_length:
                check_summit,check_dis = q.pop()
                for next_summit,next_dis in adj[check_summit]:
                    if visited[next_summit] == 0:
                        if next_dis>root_max:
                            root_max=next_dis
                        visited[next_summit] = 1
                        q.append([next_summit,next_dis])
                if check_summit in gates:
                    ch = 1
                    break
            if max_length>root_max and ch ==1:
                max_length=root_max
                result = [x,root_max]
                print(result)
            elif max_length==root_max and ch ==1 and result[0]<x:
                result = [x,root_max]
                print(result)
    adj = [[]for _ in range(n+1)]
    for p,q,r in paths:
        adj[p].append([q,r])
        adj[q].append([p,r])
    max_length=10000000000000000

    for i in summits:
        dfs(i,max_length,result)
        print(result,11,i)
    answer = []
    return result
print(solution(n,paths,gates,summits))



def dfs(x,root_max):
    if x in gates:k
        return max(distance)
    elif root_max> result[1]:
        return
    else:
        for node,r in adj[x]:
            if visited[node] ==0:
                visited[node] =1
                dfs(x,max(r,root_max))
                visited[node] = 0