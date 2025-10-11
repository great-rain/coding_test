"""
노드가 3개, 에지가 4개인 그래프
첫줄은 1번 노드에서 2번노드로 가는 가중치 4의 에지

3 4 
1 2 4
2 1 10
1 3 7
3 2 6
"""

N, E = map(int, input().split())

# step 1 빈그래프 만들기
graph = [[] for _ in range(N+1)]

# step 2 그래프에 저장하기
for _ in range(E):
    s, e, w = map(int, input().split())
    graph[s].append((e, w))

print("graph\n", graph)

# step 3 그래프에서 값 꺼내기
for node in range(1, N+1):  # 1번 노드부터 N번 노드까지
    print(f"[노드 {node}]")
    for nextNode, weight in graph[node]:
        print(f"  -> 다음 노드: {nextNode}, 가중치: {weight}")

# 특정 노드에서 값 꺼내기 
for nextNode, weight in graph[1]:
    print(f"next Node {nextNode}, weight = {weight}")