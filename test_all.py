from dijkstra import dijkstra
from a_star import a_star
from simulated_annealing import simulated_annealing

# Simple graph tet case
simple_graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}
simple_heuristic = {'A': 3, 'B': 2, 'C': 1, 'D': 0}

# Complex graph test case
complex_graph = {
    'A': {'B': 2, 'C': 5},
    'B': {'A': 2, 'D': 4, 'E': 7},
    'C': {'A': 5, 'F': 6},
    'D': {'B': 4, 'E': 1, 'G': 3},
    'E': {'B': 7, 'D': 1, 'H': 2},
    'F': {'C': 6, 'H': 1},
    'G': {'D': 3, 'H': 2},
    'H': {'E': 2, 'F': 1, 'G': 2},
    'I': {}  # Disconnected node
}
complex_heuristic = {
    'A': 7, 'B': 6, 'C': 5, 'D': 4,
    'E': 3, 'F': 2, 'G': 2, 'H': 0, 'I': float('inf')
}

print(" Simple Graph Tests ")
print("Dijkstra:", dijkstra(simple_graph, 'A'))
print("A*:", a_star(simple_graph, 'A', 'D', simple_heuristic))
print("Simulated Annealing:", simulated_annealing(simple_graph, 'A', 'D'))

print("\n Complex Graph Test ")
print("Dijkstra:", dijkstra(complex_graph, 'A'))
print("A*:", a_star(complex_graph, 'A', 'H', complex_heuristic))
print("Simulated Annealing:", simulated_annealing(complex_graph, 'A', 'H'))

# test for unreachable node
print("\n Unreachable Node Test ")
print("Dijkstra (to I):", dijkstra(complex_graph, 'A')['I'])  # should be inf
print("A* (to I):", a_star(complex_graph, 'A', 'I', complex_heuristic))
print("Simulated Annealing (to I):", simulated_annealing(complex_graph, 'A', 'I'))
