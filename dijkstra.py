import heapq

def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0

    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            if distance < distances[neighbor]: 
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

# Example graph represented as an adjacency list
graph = {
    1 : {2:10, 5:100},
    2 : {3:50, 1:10,},
    3 : {2: 50, 5: 10, 4: 20},
    4 : {5: 60, 3: 20},
    5 : {1:100, 4 :60}
}

start_node = 1
shortest_distances = dijkstra(graph, start_node)

print("Shortest distances from node", start_node, "to other nodes:")
for node, distance in shortest_distances.items():
    print(node, ":", distance)

#heapq is for min heap (heap is the implementaion of priorit queue...here in min heap smallest elements are given high priority)

# heapify(iterable): Transform a list or other iterable into a heap in-place. This operation has a time complexity of O(n), where n is the length of the iterable.
# heappush(heap, item): Push an item onto the heap while maintaining the min heap property. This operation has a time complexity of O(log n), where n is the size of the heap.
# heappop(heap): Pop the smallest item from the heap while maintaining the min heap property. This operation also has a time complexity of O(log n).
# heapreplace(heap, item): Pop the smallest item from the heap and push a new item onto the heap in one operation. This is more efficient than a pop followed by a push.
# heappushpop(heap, item): Push an item onto the heap and then pop the smallest item from the heap, all in one operation.
# heapq.nlargest(n, iterable, key=None): Return the n largest elements from an iterable, in descending order.
# heapq.nsmallest(n, iterable, key=None): Return the n smallest elements from an iterable, in ascending order.
