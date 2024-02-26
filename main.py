

def floyd_warshall(graph):
    """
    Floyd Warshall algorithm with recursion to calculate the shortest paths between all pairs of vertices
    """

    def recursive_floyd_warshall(i, j, k):
        if k == 0:
            return graph[i][j]
        else:
            return min(recursive_floyd_warshall(i, j, k - 1),
                       recursive_floyd_warshall(i, k, k - 1) + recursive_floyd_warshall(k, j, k - 1))

    n = len(graph)
    dist = [[0 if i == j
             else float('inf')
             for j in range(n)]
            for i in range(n)]

    for i in range(n):
        for j in range(n):
            dist[i][j] = recursive_floyd_warshall(i, j, n - 1)

    return dist


