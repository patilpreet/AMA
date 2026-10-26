import heapq

graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'D': 2, 'E': 5},
    'C': {'F': 3},
    'D': {},
    'E': {},
    'F': {}
}

h = {'A': 7, 'B': 6, 'C': 2, 'D': 4, 'E': 3, 'F': 0}

def astar(start, goal):
    pq = [(0, start)]
    cost = {start: 0}

    while pq:
        _, node = heapq.heappop(pq)
        print(node, end=" ")

        if node == goal:
            return

        for nxt, w in graph[node].items():
            new_cost = cost[node] + w
            if nxt not in cost or new_cost < cost[nxt]:
                cost[nxt] = new_cost
                heapq.heappush(pq, (new_cost + h[nxt], nxt))

astar('A', 'F')