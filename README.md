# Search Algorithms in Python

This repository contains Python implementations of three widely-used search algorithms:

- **Dijkstra’s Algorithm** (Shortest Path)
- **A\*** (A-Star) **Search Algorithm**
- **Simulated Annealing Algorithm** (Heuristic Optimization)

Each algorithm is applied on a graph represented as a dictionary and can be run independently or tested together using the provided `test_all.py` script.



## Overview

This project demonstrates three different approaches to finding the shortest path in a graph:

- **Dijkstra’s Algorithm** guarantees the shortest path using a greedy approach.
- **A\* Search** improves upon Dijkstra by using a heuristic to prioritize promising paths.
- **Simulated Annealing** is a probabilistic optimization technique useful for escaping local minima.

These algorithms are commonly used in navigation systems, AI pathfinding, and optimization tasks.




## Requirements

- Python 3.6 or higher
- Standard library only (no external packages needed)



## How to Run

### 1. Clone the Repository

```bash
git clone https://github.com/isaactony/search-algorithms-python-implementation.git
cd search-algorithms-python

python dijkstra.py
python a_star.py
python simulated_annealing.py


python test_all.py


