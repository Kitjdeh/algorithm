def inorder(n):
    if n <N+1:
        # Tree[n] = num.pop(0)
        inorder(2*n)
        Tree[n] = num.pop(0)
        inorder(2*n+1)
        # Tree[n] = num.pop(0)
T = int(input())
for tc in range(1,T+1):
    N = int(input())
    Tree = [0]*(N+1)
    num = [i for i in range(1,N+1)]
    inorder(1)
    print(Tree)
    print(f'#{tc} {Tree[1]} {Tree[N//2]}')
