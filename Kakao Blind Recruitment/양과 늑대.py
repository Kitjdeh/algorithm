info2 = [0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0]
edges2 = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [4, 8], [6, 9], [9, 10]]
info1 = [0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1]
edges1 = [[0, 1], [1, 2], [1, 4], [0, 8], [8, 7], [9, 10], [9, 11], [4, 3], [6, 5], [4, 6], [8, 9]]
# def find_sheep(x, a):
#     global N
#     global arr
#     visited = [0] * (N)
#     way = [[] for _ in range(N)]
#     stack = []
#     stack.append(x)
#     while stack:
#         node = stack.pop()
#         if a == node:
#             break
#         if visited[node] == 0:
#             visited[node] = 1
#             for i in arr[node]:
#                 if info[i] == 1:
#                     way[i] = way[node][::0].append(i)
#                 stack.append(i)
#     return way[node]


def solution(info, edges):
    global N
    N = len(info)
    sheep_list = []
    wolf_list = []
    sheep = 0
    wolf = 0
    arr = [[] for _ in range(N)]
    for i in range(N - 1):
        arr[edges[i][0]].append(edges[i][1])
        arr[edges[i][1]].append(edges[i][0])
    for i in range(N):
        if info[i] == 0:
            sheep_list.append(i)
        else:
            wolf_list.append(i)
    t = 0
    while True:
        if info[t] == 0:
            sheep += 1
            info[t] = -1
            sheep_list.remove(t)
        if len(sheep_list) == 0:
            break
        min_wolfway = N
        min_wolfcnt = N
        for a in sheep_list:
            visited = [0] * (N+1)
            way = [[] for _ in range(N)]
            stack = []
            stack.append(t)
            while stack:
                node = stack.pop()
                if a == node:
                    break
                if visited[node] == 0:
                    visited[node] = 1
                for i in arr[node]:
                    if info[i] == 1:
                        way[i] = way[node] +[i]
                    else:
                        way[i] = way[node]
                    if visited[i] == 0:
                        stack.append(i)
            wolf_contact = way[node]

            if len(wolf_contact) < min_wolfcnt:
                min_wolfway = wolf_contact[0::]
                min_wolfcnt = len(min_wolfway)
                select_sheep = node
        if sheep <= wolf + min_wolfcnt:
            break
        else:
            for i in min_wolfway:
                info[i] = -1
                wolf += 1
            t = select_sheep
    return sheep
print(solution(info2, edges2))

# solution(info2,edges2)

# def solution(info, edges):
#     global N
#     N = len(info)
#     sheep_list = []
#     wolf_list = []
#     sheep = 0
#     wolf = 0
#     arr = [[] for _ in range(N)]
#     for i in range(N - 1):
#         arr[edges[i][0]].append(edges[i][1])
#     for i in range(N):
#         if info[i] == 0:
#             sheep_list.append(i)
#         else:
#             wolf_list.append(i)
#     t = 0
#     while True:
#         if info[t] == 0:
#             sheep += 1
#             info[t] = -1
#             sheep_list.remove(t)
#         if len(sheep_list) == 0:
#             break
#
#         for i in arr[t]:
#             if info[t] == 0:
#                 t = i
#                 break
#
#         min_wolfway = N
#         for a in sheep_list:
#             visited = [0] * (N)
#             way = [[] for _ in range(N)]
#             stack = []
#             stack.append(t)
#             while stack:
#                 node = stack.pop()
#                 if a == node:
#                     break
#                 if visited[node] == 0:
#                     visited[node] = 1
#                 for i in arr[node]:
#                     if info[i] == 1:
#                         way[i] = way[node] + [i]
#                     else:
#                         way[i] = way[node]
#             wolf_contact = way[node]
#             min_wolfcnt = N
#             if len(wolf_contact) < min_wolfcnt:
#                 min_wolfway = wolf_contact
#                 min_wolfcnt = len(min_wolfway)
#                 select_sheep = a
#         if sheep <= wolf + min_wolfcnt:
#             break
#         for i in min_wolfway:
#             info[i] = -1
#             wolf += 1
#         t = select_sheep
#     print(sheep_list)
#     print(wolf)
#     return sheep