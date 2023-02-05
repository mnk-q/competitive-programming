from heapq import heapify, heappop, heappush

def dijsktra(graph,nodes, source_node)->dict:
    """Adjacency List Approach
    graph : List[list] or Dict[list]
    nodes : List[int]
    source_node : int
    Returns a dict of the shortest path from source_node to all other nodes
    """
    # Initialize distances to all nodes as infinite and distance to source node as 0
    distances = {node: float('inf') for node in nodes}
    distances[source_node] = 0
    # Initialize parent as None
    parent = {node: None for node in nodes}
    # Initialize priority queue
    pq = [(0, source_node)]
    # While priority queue is not empty
    while pq:
        # Pop the first element from priority queue
        distance, node = heappop(pq)
        # If distance of popped node is infinite, then there is no path to it from source
        if distance == float('inf'):
            break
        # Update distances of all adjacent nodes
        for neighbor, weight in graph[node]:
            if distances[neighbor] > distances[node] + weight:
                distances[neighbor] = distances[node] + weight
                parent[neighbor] = node
                heappush(pq, (distances[neighbor], neighbor))
    return distances, parent
    
