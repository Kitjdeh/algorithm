'''
정점 번호 v: 1~(E+1)
간선 수
부모-자식 순
4
1 2 1 3 3 4 3 5
'''
def find_root(V):
    for i in range(1,V+1):
        if par[i] == 0:     #부모가 없으면 root
            return i

def preorder(n):        #전위 순회
    if n:
        print(n)        #visit(n)
        preorder(ch1[n])
        preorder(ch2[n])
def inorder(n):         #중위 순회
    if n:
        inorder(ch1[n])
        print(n)
        inorder(ch2[n])
def postorder(n):       #후위 순회
    if n:
        postorder(ch1[n])
        postorder(ch2[n])
        print(n)
E= int(input())
arr = list(map(int,input().split()))
V= E+1
root=1
#부모를 인덱스로 자식번호 저장
# 4
# 1 2 1 3 3 4 3 5
ch1 = [0]*(V+1)
ch2 = [0]*(V+1)

#자식을 인덱스로 부모번호 저장
par = [0]*(V+1)

for i in range(E):
    p, c = arr[i*2], arr[i*2+1]
# for j in range(0,2*E,2):
#     p, c = arr[j],arr[j+1]
    if ch1[p] == 0:             #아직 자식이 없으면
        ch1[p] = c
    else:
        ch2[p] = c
    par[c]=p


# print(par)
# print(find_root(V))
'''
정점 번호 v: 1~(E+1)
간선 수
부모-자식 순
4
1 2 1 3 3 4 3 5
'''
# print(ch1)
# [0, 2, 0, 4, 0, 0]
# print(ch2)
# [0, 3, 0, 5, 0, 0]

# preorder(root)
# #1,2,3,4,5
# inorder(root)
# #2,1,4,3,5
# postorder(root)
# #2,4,5,3,1