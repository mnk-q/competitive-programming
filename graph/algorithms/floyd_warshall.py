# Floyd Warshall algorithm
# Also called All-Pairs Shortest Paths
# This algorithm is used to find the shortest path between all pairs of vertices in a graph
# It is also used to find the shortest path between all pairs of vertices in a weighted graph
# It requires the graph to be connected
# This file includes multiple implementations of the algorithm
# choose the one that suits your needs



# Implementation 1:
# This implementation uses a matrix to store the shortest path between all pairs of vertices
# Assume that given graph is An Adjacency Matrix
# This Algorithm will perform in-place modification of the matrix

def floyd_warshall(graph: list, num_nodes = None) -> list:
    if num_nodes == None:
        num_nodes = len(graph)
    
    for k in range(num_nodes):
        for i in range(num_nodes):
            for j in range(num_nodes):
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

    
