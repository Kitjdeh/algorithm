info2 = [0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0]
edges2 = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [4, 8], [6, 9], [9, 10]]
info1 = [0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1]
edges1 = [[0, 1], [1, 2], [1, 4], [0, 8], [8, 7], [9, 10], [9, 11], [4, 3], [6, 5], [4, 6], [8, 9]]

result = 0


def f(visited, i, sheep, way, wolf, info, arr):
    global result
    if info[i] == 0:
        sheep += 1
    elif info[i] == 1:
        wolf += 1
    visited[i] = 1
    for j in arr[i]:
        if visited[j] == 0:
            way.append(j)
    if sheep <= wolf:
        if result<sheep:
            result = sheep
        return
    elif len(way) == 0:
        if result < sheep:
            result = sheep
        return
    else:
        for j in range(len(way)):
            new_way = way[0::]
            t = new_way.pop(j)
            # print((t, sheep, wolf))
            f(visited, t, sheep, new_way, wolf, info, arr)
            visited[t] = 0

def solution(info, edges):
    global N
    global result

    N = len(info)
    sheep_list = []
    wolf_list = []
    result = 0
    arr = [[] for _ in range(N)]
    for i in range(N - 1):
        arr[edges[i][0]].append(edges[i][1])
        arr[edges[i][1]].append(edges[i][0])
    for i in range(N):
        if info[i] == 0:
            sheep_list.append(i)
        else:
            wolf_list.append(i)
    visited = [0] * N
    way = []
    cnt = 0

    f(visited, 0, 0, way, 0, info, arr)
    return result

print(solution(info1, edges1))
