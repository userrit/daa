def bellman_ford(graph, start):
    # Step 1: Initialization
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    
    # Step 2: Relaxation
    for _ in range(len(graph) - 1):
        for node in graph:
            for neighbor, weight in graph[node].items():
                if distances[node] + weight < distances[neighbor]:
                    distances[neighbor] = distances[node] + weight
    
    # Step 3: Negative Cycle Detection
    for node in graph:
        for neighbor, weight in graph[node].items():
            if distances[node] + weight < distances[neighbor]:
                raise ValueError("Negative cycle detected")
    
    return distances

# Example graph represented as an adjacency list
graph = {
    'A': {'B': -4,'T':-3},
    'B': {'D': -1, 'E': -2},
    'C': {'B':8,'T':3},
    'D': {'A': 6, 'T': 4},
    'E': {'C': -3,'T':2},
    'T': {}
}

start_node = 'A'
shortest_distances = bellman_ford(graph, start_node)
print("Shortest distances from node", start_node, "to other nodes:")
for node, distance in shortest_distances.items():
    print(node, ":", distance)
