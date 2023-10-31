N = int(input())
ch1 = [0]*(N+1)         #ch1[부모인덱스]=자식놈인덱스
ch2 = [0]*(N+1)
arr = [0]*(N+1)         #각 숫자의 노드번호 부착
for i in range(1,N+1):
    p, c1, c2 = input().split()
    arr[i] = p
    p = i               #순서대로 들어론 p를 int i로 바꿔주고 기록해둠
    if c1 != '.':
        ch1[i] = c1

    if c2 != '.':
        ch2[i] = c2
def preorder(n):
    if n:
        print(n, end='')
        preorder(ch1[arr.index(n)])
        preorder(ch2[arr.index(n)])

def inorder(n):
    if n:
        inorder(ch1[arr.index(n)])
        print(n, end='')
        inorder(ch2[arr.index(n)])
def postorder(n):
    if n:
        postorder(ch1[arr.index(n)])
        postorder(ch2[arr.index(n)])
        print(n, end='')
preorder('A')
print()
inorder('A')
print()
postorder('A')