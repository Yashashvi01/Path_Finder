import random

def create_grid_graph(rows, cols):
    graph = {}
    node_positions = {}
    for i in range(rows):
        for j in range(cols):
            node = (i, j)
            graph[node] = []
            node_positions[node] = (j, -i)
            # Add neighbors (4-directional)
            for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                ni, nj = i + di, j + dj
                if 0 <= ni < rows and 0 <= nj < cols:
                    graph[node].append((ni, nj))
    return graph, node_positions

def add_obstacles(graph, node_positions, num_obstacles, start_node, end_node):
    potential_obstacles = [node for node in node_positions.keys() if node not in [start_node, end_node]]
    obstacles = random.sample(potential_obstacles, min(num_obstacles, len(potential_obstacles)))
    
    for obs in obstacles:
        if obs in graph:
            graph.pop(obs)
            for neighbor in list(graph.keys()):
                if obs in graph[neighbor]:
                    graph[neighbor].remove(obs)
    return graph
