# 정사각형 블록으로 표현 된 단위들 의 합을 나타낸다.
# 특정 점[x,y] 에서 동일한 블럭이 어디까지 표현되는지 확인 하는 함수 check(x,y)
# 만약(1,0) -> [(2,0),(1,1),(2,1)] 확인해야함
# => 전부다 [1,0]와 같으면 다음 단계 아니면 return
# 그 다음 -> [(3,0),(3,1),(3,2),(2,2),(1,2)] 확인 (-> 이전 단계들을 각각 +1,0 / +1,+1 / +0,+1 하도 set 처리
# 확실한 단계 에서 전부 visited 처리 하고 해당 값을 result 에 (값,지름 규격)을 넣는다.
(0,4),(0,2),(0,2),(1,2),(1,2)