import sys

INFINITY = sys.maxsize

# 최소 거리를 가지는 정점을 찾는 함수
def find_min_vertex(distances, visited):
    min_vertex = -1
    for i in range(len(distances)): #distances 배열의 길이만큼 반복. 즉 정점의 개수만큼 반복
        #현재 정점 'i'가 방문되지 않았고,(and) 'min_vertex'가 아직 설정되지 않았거나(or) distances[i]가 distances[min_vertex]보다 작을 경우에 조건이 참이 됨
        #최소 거리를 가지는 정점을 찾기 위한 조건이라는 뜻
        if not visited[i] and (min_vertex == -1 or distances[i] < distances[min_vertex]):
            min_vertex = i # mit_vertex 변수에 현재 정점 'i'를 할당합니다.
                           # 이는 현재까지 찾은 최소 거리를 가지는 정점의 인덱스를 업데이트 하는것
    return min_vertex # 반환

# 출발지로부터 각 정점까지의 최단 거리를 계산하는 함수
def find_shortest_distances(graph, source):
    n = len(graph) # len(graph)는 'graph' 리스트의 첫 번째 차원의 길이 반환.
    distances = [INFINITY] * n  # 모든 정점까지의 거리를 무한대로 초기화
    visited = [False] * n  # 방문 여부를 저장하는 배열

    distances[source] = 0  # 출발지까지의 거리는 0으로 설정

    for _ in range(n - 1):
        min_vertex = find_min_vertex(distances, visited)  # 최소 거리를 가지는 정점 선택
        visited[min_vertex] = True  # 해당 정점을 방문으로 표시

        for j in range(n):
            # 아직 방문하지 않은 정점이고, 경로가 존재하며, 더 짧은 경로인 경우 최단 거리 업데이트
            if not visited[j] and graph[min_vertex][j] != INFINITY and distances[min_vertex] + graph[min_vertex][j] < distances[j]:
                distances[j] = distances[min_vertex] + graph[min_vertex][j]

    return distances

# 그래프 정의
graph = [
    [0, 2, 5, 1, INFINITY],
    [2, 0, 3, 2, INFINITY],
    [5, 3, 0, 3, 1],
    [1, 2, 3, 0, 1],
    [INFINITY, INFINITY, 1, 1, 0]
]

source = int(input("출발지(0 ~ 4)를 입력하세요 : "))

# 가격 정보
prices = [0, 0, 0, 0, 0] # 충전소 0부터 4까지 가격 저장할 배열
for i in range(len(prices)):
    if i != source: #출발지 제외
        price_input = input("충전소 {}의 충전 가격(1kWh/원): " .format(i))
        prices[i] = float(price_input)

while True:
    
    distances = find_shortest_distances(graph,source)  # 최단 거리 계산


    ask = int(input("탐색 기준을 선택하세요 (최단경로: 1 가격: 2 호환성: 3 종료: -1) -> "))
    print()
    if ask == 1: # 최단경로 경우
        print("출발지로부터 각 충전소에 대한 최단 거리와 각 충전소의 가격")
        for i in range(len(distances)):
            if i != source: #출발지 제외
                print("충전소", i, ":", distances[i], ", 가격:", prices[i])

        print("출발지로부터 가장 가까운 충전소")
        min_value = min(distances[index] for index in range(len(distances)) if index != source)  # 출발지 제외
        for i in range(len(distances)):
            if distances[i] == min_value and i != source:  # 출발지 제외
                print("충전소", i, ":", distances[i])
        print()


    elif ask == 2: #가격 경우
        print("가장 싼 가격의 충전소")
        min_price = min(prices[index] for index in range(len(prices)) if index != source)  # 출발지 제외
        for i in range(len(prices)):
            if prices[i] == min_price and i != source:  # 출발지 제외
                print("충전소", i, ":" ,prices[i])

        print("가장 싼 가격의 충전소 중 가장 가까운 충전소의 거리")
        min_price = min(prices[index] for index in range(len(prices)) if index != source)  # 출발지 제외
        min_price_vertices = [i for i in range(len(prices)) if prices[i] == min_price and i != source]  # 가장 싼 가격의 충전소들
        min_distance = INFINITY
        min_vertices = []

        for vertex in min_price_vertices:
            if distances[vertex] < min_distance:
                min_distance = distances[vertex]
                min_vertices = [vertex]
            elif distances[vertex] == min_distance:
                min_vertices.append(vertex)

        if min_vertices:
            for vertex in min_vertices:
                print("충전소", vertex, ":", distances[vertex])
        else:
            print("가장 싼 가격의 충전소가 없습니다.")
        print()

        

    elif ask == -1: #종료
        break


    


