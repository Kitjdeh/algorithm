# arr에서 arr[i]를 뒤집으려면 arr[i:i+k]가 역순이 된다.
# 오름 차순으로 만들려는 경우
# t 번 동안 나올 수 있는 경우의 수를 확인
# 순열의 오름차순 정답을 미리 세팅


N,K = map(int,input().split())
arr = list(input().split())
# 정답 생성
ans = arr[::]
ans.sort()
ans_Word = "".join(ans)
visited = set()
result = -1

q = [[arr,0]]
while q:
    array,cnt = q.pop(0)
    if array == ans:
        result = cnt
        break
    for i in range(N-K+1):
        temp = array[i:i+K]
        temp.reverse()
        arr2 = array[:i] + temp + array[i+K:]
        new_word = "".join(arr2)
        if new_word not in visited:
            q.append([arr2,cnt+1])
            visited.add(new_word)
print(result)