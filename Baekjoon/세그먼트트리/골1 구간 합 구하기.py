N,M,K = map(int,input().split())
arr = [0]*N
for i in range(N):
    arr[i] = int(input())

tree = [0]*(N*4)

def init(start,end,node):
    if start == end:
        tree[node] = arr[start]
        return  tree[node]
    else:
        mid = start + (end-start)//2
        tree[node] = init(start,mid,node*2) + init(mid+1,end,node*2+1)
        return tree[node]

def rangesum(start,end,node,left,right):
    #범위 밖에 있는 경우
    if left>end or right <start:
        return 0
    elif left <=start and end <= right:
        return tree[node]
    else:
        mid = start + (end-start)//2
        return rangesum(start,mid,node*2, left, right) + rangesum(mid+1,end,node*2+1,left,right)


def update(start,end,node,index,change):
    if index < start or index > end:
        return
    tree[node] += change
    if start != end:
        mid = start + (end-start)//2
        update(start,mid,node*2,index,change)
        update(mid+1,end,node*2+1,index,change)


init(0,N-1,1)

for i in range(M+K):
    a,b,c = map(int,input().split())
    if a == 1:
        update(0,N-1,1,b-1,c-arr[b-1])
        arr[b - 1] = c
    else:
        print(rangesum(0,N-1,1,b-1,c-1))