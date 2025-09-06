# dfs can be recursive and iterative

# Recursive DFS (Adjacency List)
def dfs(node,adj,visited):
    if node in visited:
        return 
    visited.add(node)
    for nei in adj[node]:
        if nei not in visited:
            visited.add(nei)
            dfs(nei , adj, visited)


visited = set()
dfs(start, adj, visited)

# iterative dfs
def dfs_iter(start , adj):
    visited = set()
    stack = [start]
    while stack:
        node = stack.pop()
        if node in visited:
            continue
        visited.add(node)
        for nei in adj[node]:
            if nei not in visited:
                stack.append(nei)

# Full Graph DFS (handling disconnected comps)
def dfs_all(n,adj):
    visited = set()
    def dfs(u):
        if u in visited:
            return
        visited.add(u)
        for v in adj[u]:
            dfs(v)
    for node in range(n):
        if node not in visited:
            dfs(node)


# DFS for Cycle Detection (Directed)
def has_cycle(n,adj):
    visited = set()
    path = set()
    def dfs(u):
        if u in path:
            return True
        if u in visited:
            return False
        visited.add(u)
        path.add(u)
        for v in adj[u]:
            if dfs(v):
                return True
        path.remove(u)
        return False
    for i in range(n):
        if dfs(i):
            return True
    return False


# Matrix DFS (grid probs like islands)
def dfs(r, c, grid, visited):
    if (r, c) in visited or r<0 or c<0 or r>=len(grid) or c>=len(grid[0]) or grid[r][c] == 0:
        return
    visited.add((r, c))
    dfs(r+1, c, grid, visited)
    dfs(r-1, c, grid, visited)
    dfs(r, c+1, grid, visited)
    dfs(r, c-1, grid, visited)


