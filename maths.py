# Example: set operations
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

union_set = A.union(B)
intersection_set = A.intersection(B)
difference_set = A.difference(B)

print("Set A:", A)
print("Set B:", B)
print("Union:", union_set)
print("Intersection:", intersection_set)
print("Difference (A - B):", difference_set)
from collections import deque

# Sample graph represented as an adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

# DFS using recursion
def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start, end=" ")
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)
    return visited

print("DFS Traversal starting from A:")
dfs(graph, 'A')
print("\n")

# BFS using a queue
def bfs(graph, start):
    visited = set()
    queue = deque([start])
    while queue:
        vertex = queue.popleft()
        if vertex not in visited:
            visited.add(vertex)
            print(vertex, end=" ")
            queue.extend([n for n in graph[vertex] if n not in visited])

print("BFS Traversal starting from A:")
bfs(graph, 'A')

def sieve_of_eratosthenes(n):
    """Return a list of primes up to n (inclusive)."""
    sieve = [True] * (n + 1)
    sieve[0:2] = [False, False]  # 0 and 1 are not prime.

    for i in range(2, int(n**0.5) + 1):
        if sieve[i]:
            for j in range(i * i, n + 1, i):
                sieve[j] = False

    return [i for i, is_prime in enumerate(sieve) if is_prime]

# Test the function
primes_up_to_50 = sieve_of_eratosthenes(50)
print("Primes up to 50:", primes_up_to_50)
