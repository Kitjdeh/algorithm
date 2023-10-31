a = [1,9,3,8,4,5,5,9,10,3,4,5]
L = len(a)
tree = [0]*(L**4)

def init(start,end,node):
    if start == end:
        tree[node] = a[start]
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
    tree[node] +=change
    if start == end:
        return
    mid = start + (end-start)//2
    update(start,mid,node*2,index,change)
    update(mid+1,end,node*2+1,index,change)