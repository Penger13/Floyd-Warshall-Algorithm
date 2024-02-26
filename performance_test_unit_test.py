import unittest

class TestFloydWarshall(unittest.TestCase):
    """
    unittest to test the recursive functions in base and positive cases
    """

    def test_recursive_floyd_warshall_base_case(self):
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

    def test_recursive_floyd_warshall_positive_case(self):
        graph2 = [
            [0, 1, float('inf'), 1],
            [1, 0, 1, float('inf')],
            [float('inf'), 1, 0, 1],
            [1, float('inf'), 1, 0]
        ]
        result2 = floyd_warshall(graph2)
        self.assertEqual(result2, [
            [0, 1, 2, 1],
            [1, 0, 1, 2],
            [2, 1, 0, 1],
            [1, 2, 1, 0]
        ])


import timeit

# Import your Floyd-Warshall algorithm implementation
from main import floyd_warshall

import random


def generate_random_graph(num_vertices, max_weight=10, density=0.5):
    """
    Generates a random weighted directed graph.

    """
    # Initialize an empty graph (all edges are initially set to infinity)
    graph = [[float('inf')] * num_vertices for _ in range(num_vertices)]

    # Add edges randomly based on density
    for i in range(num_vertices):
        for j in range(num_vertices):
            if i != j and random.random() < density:
                # Assign a random weight to the edge
                graph[i][j] = random.randint(1, max_weight)

    return graph


class PerformanceTest(unittest.TestCase):
    def setUp(self):
        # Define a range of graph sizes to test
        self.graph_sizes = [10, 50, 100, 200]

    def test_performance(self):
        for size in self.graph_sizes:
            # Generate a random graph of size 'size'
            graph = generate_random_graph(size)

            # Measures the run time of the algorithm
            time_taken = timeit.timeit(lambda: floyd_warshall(graph), number=1)

            # Print the results
            print(f"Graph size: {size}, Time taken: {time_taken} seconds")


if __name__ == '__main__':
    unittest.main()
