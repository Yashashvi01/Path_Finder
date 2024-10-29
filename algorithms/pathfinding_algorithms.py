from queue import PriorityQueue
from collections import deque

# BFS Algorithm
def bfs_shortest_path(graph, start, end):
    queue = deque([(start, [start])])
    explored = []

    while queue:
        node, path = queue.popleft()
        explored.append(node)
        
        if node == end:
            return path, explored
        
        for neighbor in graph.get(node, []):
            if neighbor not in explored and neighbor not in [n for n, _ in queue]:
                queue.append((neighbor, path + [neighbor]))

    return None, explored

# Dijkstra's Algorithm
def dijkstra_shortest_path(graph, start, end):
    queue = PriorityQueue()
    queue.put((0, start, [start]))
    distances = {start: 0}
    explored = []

    while not queue.empty():
        dist, node, path = queue.get()
        explored.append(node)
        
        if node == end:
            return path, explored
        
        for neighbor in graph[node]:
            new_dist = dist + 1  # Assuming uniform weight of 1 for simplicity
            if neighbor not in distances or new_dist < distances[neighbor]:
                distances[neighbor] = new_dist
                queue.put((new_dist, neighbor, path + [neighbor]))

    return None, explored

# DFS Algorithm
def dfs_search(graph, start, end):
    stack = [(start, [start])]
    explored = []

    while stack:
        node, path = stack.pop()
        if node in explored:
            continue
        explored.append(node)
        
        if node == end:
            return path, explored
        
        for neighbor in graph.get(node, []):
            if neighbor not in explored:
                stack.append((neighbor, path + [neighbor]))

    return None, explored

# A* Algorithm
def a_star_search(graph, start, end, heuristic):
    open_set = PriorityQueue()
    open_set.put((0, start))
    came_from = {start: None}
    cost_so_far = {start: 0}
    explored = []

    while not open_set.empty():
        current = open_set.get()[1]
        explored.append(current)
        
        if current == end:
            path = []
            while current:
                path.append(current)
                current = came_from[current]
            return path[::-1], explored
        
        for neighbor in graph[current]:
            new_cost = cost_so_far[current] + 1  # Uniform cost
            if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                cost_so_far[neighbor] = new_cost
                priority = new_cost + heuristic(neighbor, end)
                open_set.put((priority, neighbor))
                came_from[neighbor] = current

    return None, explored

# Manhattan Distance Heuristic for A*
def manhattan_distance(node1, node2):
    return abs(node1[0] - node2[0]) + abs(node1[1] - node2[1])
