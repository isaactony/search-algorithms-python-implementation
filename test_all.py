from dijkstra import dijkstra
from a_star import a_star
from simulated_annealing import simulated_annealing

graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

heuristic = {
    'A': 3,
    'B': 2,
    'C': 1,
    'D': 0
}

print("=== Running Test ===")
print("Dijkstra:", dijkstra(graph, 'A'))
print("A*:", a_star(graph, 'A', 'D', heuristic))
print("Simulated Annealing:", simulated_annealing(graph, 'A', 'D'))
