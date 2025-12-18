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

def dfs(graph, start, type, visited=None):
    if type == "recursive":
        if visited == None:
            visited = set()
        visited.add(start)
        for node in graph[start]:
            if node not in visited:
                dfs(graph, node, type, visited)
        return visited
    elif type == "stack":
        if visited == None:
            visited = set()
        stack = [start]
        for node in stack:
            node = stack.pop()
            if node not in visited:
                visited.add(node)
                stack.extend(reversed(graph[node]))
        return visited
