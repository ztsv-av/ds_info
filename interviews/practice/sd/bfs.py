def bfs(graph, start, visited=None):
    from collections import deque
    queue = deque()
    queue.append([start])

    visited = set([start])
    
    while queue:
        node = queue.pop()
        for node in graph[node]:
            if node not in visited:
                visited.add(node)
                queue.append(node)
        
    return visited
