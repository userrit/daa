def find(parent, vertex):
    # Find the root of the disjoint set to which the vertex belongs.
    if parent[vertex] == vertex:
        return vertex
    parent[vertex] = find(parent, parent[vertex])
    return parent[vertex]

def union(parent, rank, x, y):
    # Perform the union operation of the disjoint sets.
    root_x = find(parent, x)
    root_y = find(parent, y)

    if rank[root_x] < rank[root_y]:
        parent[root_x] = root_y
    elif rank[root_x] > rank[root_y]:
        parent[root_y] = root_x
    else:
        parent[root_y] = root_x
        rank[root_x] += 1

def kruskal(graph):
    """
    Find the minimum spanning tree (MST) of a weighted undirected graph using Kruskal's algorithm.
    """
    edges = []  # List to store all edges
    mst = []    # Minimum spanning tree

    # Create a disjoint set for each vertex
    parent = {vertex: vertex for vertex in graph}
    rank = {vertex: 0 for vertex in graph}
    
    

    # Create a list of all edges in the graph
    for u in graph:
        for v, weight in graph[u]:
            edges.append((u, v, weight))

    # Sort the edges in ascending order of their weights
    edges.sort(key=lambda x: x[2])

    for u, v, weight in edges:
        root_u = find(parent, u)
        root_v = find(parent, v)

        # If including the edge does not form a cycle, add it to the MST
        if root_u != root_v:
            mst.append((u, v, weight))
            union(parent, rank, root_u, root_v)

    return mst

# Driver Code
graph = {
    '1': [('5', 5), ('2', 10)],
    '2': [('1', 10), ('3', 1), ('4', 6)],
    '3': [('2', 1), ('4', 2), ('5', 7)],
    '4': [('5', 3), ('2', 6), ('3', 2)],
    '5': [('1', 5), ('3', 7), ('4', 3)]
}
minimum_spanning_tree = kruskal(graph)

#Calculate weight of MST
weight = sum(x[2] for x in minimum_spanning_tree)
print("Weight of MST = ", weight)

print("Edges of MST : ")
for edge in minimum_spanning_tree:
    print(edge)


"""
Output:-

Weight of MST =  11
Edges of MST : 
('2', '3', 1)
('3', '4', 2)
('4', '5', 3)
('1', '5', 5)

--------------------------------------------------

APPLICATIONS of Kruskal's Algorithm:

Minimum Spanning Tree: Kruskal's algorithm is specifically designed to find the minimum spanning tree (MST) of a weighted undirected graph. It is commonly used in network design, transportation planning, and other scenarios where finding the minimum cost connectivity is essential.

Network Clustering: Kruskal's algorithm can be applied to cluster data points based on their pairwise distances. By treating the data points as vertices and the distances as edge weights, the algorithm can identify the most significant connections between data points, leading to effective clustering.

Image Segmentation: Kruskal's algorithm can be utilized in image segmentation tasks, where the goal is to partition an image into distinct regions based on certain criteria.

--------------------------------------------------

TIME COMPLEXITY of Kruskal's Algorithm:

The time complexity of Kruskal's algorithm depends on the sorting step and the union-find operations performed on the edges of the graph.

Sorting Step: The algorithm sorts the edges of the graph based on their weights, which takes O(E log E) time, where E is the number of edges in the graph. Sorting the edges dominates the time complexity of the algorithm.

Union-Find Operations: The algorithm performs union-find operations on the vertices to check for cycles and merge sets. These operations typically take O(log V) time, where V is the number of vertices. Since the number of edges (E) is generally much larger than the number of vertices (V) in a graph, the union-find operations have a relatively smaller impact on the overall time complexity.

Therefore, the time complexity of Kruskal's algorithm is O(E log E) due to the sorting step, where E is the number of edges in the graph.

____________________________________________________________________________________________________________________________________________________________________
"""