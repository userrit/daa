import heapq

def prim(graph, start_node):
    # Initialize variables
    mst = []
    visited = set()
    pq = [(0, start_node, None)]  # Priority queue for selecting edges

    while pq:
        cost, node, parent = heapq.heappop(pq)

        if node in visited:
            continue
        visited.add(node)
        if parent is not None:
            mst.append((parent,node,cost))
        

        for neighbor, weight in graph[node].items():
            if neighbor not in visited:
                heapq.heappush(pq, (weight, neighbor, node))

    return mst

# Example graph represented as an adjacency dictionary
graph = {
    'A': {'B': 3, 'C': 1},
    'B': {'A': 3, 'C': 4, 'D': 2},
    'C': {'A': 1, 'B': 4, 'D': 5},
    'D': {'B': 2, 'C': 5}
}

start_node = input("Enter the start node: ")

minimum_spanning_tree = prim(graph, start_node)
print("Minimum Spanning Tree:")
for parent,node,weight in minimum_spanning_tree:
    print(f"{parent} - {node} : {weight}")
