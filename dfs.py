from collections import deque


def dfs(graph, start):
    visited, stack = list(), [start]
    while stack:
        vertex = stack.pop()
        if vertex in visited:
            continue
        visited.append(vertex)
        stack.extend(graph[vertex] - set(visited))
    return visited


def bfs(graph, start):
    visited, queue = list(), deque([start])
    while queue:
        vertex = queue.popleft()
        if vertex not in visited:
            visited.append(vertex)
            queue.extend(graph[vertex] - set(visited))
    return visited


def test_dfs():
    graph = {
        'A': {'B', 'C'},
        'B': {'D', 'A'},
        'C': {'E', 'A'},
        'D': {'B'},
        'E': {'C'},
    }
    assert dfs(graph, 'A') == ['A', 'C', 'E', 'B', 'D']

def test_bfs():
    graph = {
        'A': {'B', 'C'},
        'B': {'D', 'A'},
        'C': {'E', 'A'},
        'D': {'B'},
        'E': {'C'},
    }
    assert bfs(graph, 'A') == ['A', 'B', 'C', 'D', 'E']
