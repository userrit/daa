# Using a Python dictionary to act as an adjacency list
graph = {
    '0': ['1', '2','3'],
    '1': ['0', '2', '4'],
    '2': ['0','1','4'],
    '3': ['4','0'],
    '4': ['1','2', '3'],
}

visited = set()  # Set to keep track of visited nodes.


def dfs(visited, graph, node):
    if node not in visited:  # If the node has not been visited
        print(node, end=' ')  # Print the node
        visited.add(node)  # Mark the node as visited
        for child in graph[node]:  # Explore each child of the node
            dfs(visited, graph, child)  # Recursive call to explore child nodes


# Driver Code
print("DFS traversal : ", end= ' ')
dfs(visited, graph, '0')  # Start the DFS traversal from node '0'


"""
----------------------------------------------------------------------------------------------------
Output:-
DFS traversal :  0 1 2 4 3 
----------------------------------------------------------------------------------------------------
Time complexity:
The time complexity of this algorithm depends on the number of vertices (V) and edges (E) in the graph.
In the worst case, each node and edge will be visited exactly once.
Therefore, the time complexity can be approximated as O(2V + E), which simplifies to O(V + E).

Space complexity:
The space complexity is determined by the size of the visited set, which can contain at most all the vertices.
Therefore, the space complexity is O(V), where V is the number of vertices in the graph.

Applications:
----------------------------------------------------------------------------------------------------
Finding a path through a maze.
Detecting and exploring connected components in a social network.
Checking for the existence of a cycle in a graph.
Parsing and evaluating mathematical expressions.
Solving puzzles like Sudoku or the Eight Queens problem.
"""
