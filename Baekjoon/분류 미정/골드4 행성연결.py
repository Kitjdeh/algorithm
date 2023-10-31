# 각 행성 간의 연결 최솟값 -> 최소 스패닝 트리 && 크루스깔
# 부모리스트 생성
# 간선 정보를 오름차순 정렬
# 간선 값이 낮은 곳 부터 입력
# 입력 시 싸이클이 형성 되지 않는다
# == 포함하고 a,b중 부모 노드 값 낮은 애로 바꿈

#1. 비용 오름차순으로 노드 정렬
#2. 본인을 보는 parent
#3. 낮은 값부터 꺼내서 p,q 넣으면 싸이클 형성 여부 확인 --- find(p),find(q)
#4. 문제 없으면 union

def find(x):
    if parent[x] !=x:
        parent[x] = find(parent[x])
    return parent[x]

def union(p,q):
    x,y = find(p),find(q)
    if x < y:
        parent[y] = x
    else:
        parent[x] = y


N = int(input())
node = []
result = 0
for i in range(N):
    arr = list(map(int,input().split()))
    for j in range(N):
        if i == j :
            pass
        else:
            node.append([arr[j],i,j])
node.sort()
parent = [i for i in range(N)]
for price,p,q in node:
    if find(p) != find(q):
        union(p,q)
        result +=price
print(result)