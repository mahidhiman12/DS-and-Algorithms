# bfs can only be iterative

# BFS on Graph (Adj List)
def bfs(start,adj):
    queue = deque([start])
    visited = set([start])
    while queue:
        node = queue.popleft()
        # process node here if needed
        for nei in adj[node]:
            if nei not in visited:
                visited.add(nei)
                queue.append(nei)


# BFS Shortest Path (Unweighted Graph) : eg: find min steps

def shortest_path(start, target, adj):
    q = deque([start,0])
    visited = set([start])
    while q:
        node,distance = q.popleft()
        if node == target:
            return distance
        for nei in adj[node]:
            if nei not in visited:
                visited.add(nei)
                q.append((nei , dist+1))

    return -1



# BFS on Grid (Matrix Problems like Islands, Rotting Oranges)
def bfs_grid(start_r, start_c, grid):
    from collections import deque
    rows, cols = len(grid), len(grid[0])
    q = deque([(start_r, start_c)])
    visited = set([(start_r, start_c)])
    
    while q:
        r, c = q.popleft()
        for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
            nr, nc = r+dr, c+dc
            if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited and grid[nr][nc] == 1:
                visited.add((nr, nc))
                q.append((nr, nc))


# Level Order BFS (when u care about levels)
def bfs_levels(start, adj):
    from collections import deque
    q = deque([start])
    visited = set([start])
    level = 0
    
    while q:
        for _ in range(len(q)):
            node = q.popleft()
            # process node at "level"
            for nei in adj[node]:
                if nei not in visited:
                    visited.add(nei)
                    q.append(nei)
        level += 1

    
