# 13
# 1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13
# 4
# 1 2 1 3 3 4 3 5
V = int(input())
arr = list(map(int,input().split()))
E = V-1             #간선 수
ch1 = [0] * (V+1)   #부모 인덱스, 자식번호 저장
ch2 = [0] * (V+1)
par = [0] * (V+1)
def find_root(V):
    for i in range(1,V+1):
        if par[i] == 0:         #부모가 없으면 root
            return i
for i in range(E):
    p,c = arr[2*i],arr[2*i+1]
    if ch1[p] ==0:              #부모 인덱스, 자식 저장
        ch1[p] =c
    else:
        ch2[p] =c
    par[c] = p                  #자식 인덱스, 부모 저장
def preorder(n):
    # global cnt
    if n:
        cnt =n
        #print(n, end=' ')
        preorder(ch1[n])
        preorder(ch2[n])
def inorder(n):
    if n:
        inorder(ch1[n])
        print(n, end = " ")
        inorder(ch2[n])
def postorder(n):
    if n :
        postorder(ch1[n])
        postorder(ch2[n])
        print(n, end = " ")
# preorder(root)
def f(n):                        #global cnt 없이 순회한 정점 수를 리턴하는 함수
    if n == 0:                  #서브트리가 비어있으면
        return 0
    else:
        L = f(ch1[n])
        R = f(ch2[n])
        return L + R + 1
root = find_root(V)
# preorder(root)
# print(cnt)
print(f(1))
print(ch1)
print(ch2)
# print(" ")
# inorder(root)
# print(" ")
# postorder(root)
# for i in inorder(root):
#     print(i)
#     1 2 4 7 12 3 5 8 9 6 10 11 13 1