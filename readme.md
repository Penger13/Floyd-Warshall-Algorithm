
## Recursion in Floyd-Warshall Algorithm


This repository now includes a recursive version of the Floyd Warshall algorithm in Python. The recursive approach allows calculating the shortest paths between all pairs of vertices in a weighted graph using a recursive function.
To access in Github follow the link: https://github.com/Penger13/Floyd-Warshall-Algorithm

### Usage


To use the recursive Floyd Warshall algorithm, call the `floyd_warshall(graph)` function with an adjacency matrix representing the weighted graph. The function returns a matrix containing the shortest paths between all pairs of vertices.


```python

# Example Usage

graph = [

    [0, 5, float('inf'), 10],

    [float('inf'), 0, 3, float('inf')],

    [float('inf'), float('inf'), 0, 1],

    [float('inf'), float('inf'), float('inf'), 0]

]


shortest_paths = floyd_warshall(graph)

print(shortest_paths)

