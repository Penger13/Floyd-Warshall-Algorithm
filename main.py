
import unittest



def floyd_warshall(graph):
    """
    Floyd-Warshall algorithm with recursion to calculate the shortest paths between all pairs of vertices
    """

    def recursive_floyd_warshall(i, j, k):
        if k == 0:
            return graph[i][j]
        else:
            return min(recursive_floyd_warshall(i, j, k - 1),
                       recursive_floyd_warshall(i, k, k - 1) + recursive_floyd_warshall(k, j, k - 1))

    n = len(graph)
    dist = [[0
             if i == j
                else float('inf')
                    for j in range(n)]
                        for i in range(n)]

    for i in range(n):
        for j in range(n):
            dist[i][j] = recursive_floyd_warshall(i, j, n - 1)

    return dist

class TestFloydWarshall(unittest.TestCase):
    """
    unittest to test the function
    """
    def test_floyd_warshall(self):
        # Test case 1
        graph1 = [
            [0, 5, float('inf'), 10],
            [float('inf'), 0, 3, float('inf')],
            [float('inf'), float('inf'), 0, 1],
            [float('inf'), float('inf'), float('inf'), 0]
        ]
        result1 = floyd_warshall(graph1)
        self.assertEqual(result1, [
            [0, 5, 8, 9],
            [float('inf'), 0, 3, 4],
            [float('inf'), float('inf'), 0, 1],
            [float('inf'), float('inf'), float('inf'), 0]
        ])




if __name__ == '__main__':
    unittest.main()

