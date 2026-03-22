from collections import deque
import heapq

grid = [
    [1,1,1,1,1],
    [1,5,5,1,1],
    [1,1,1,1,1],
    [1,1,999,1,1],
    [1,1,1,1,1]
]

start = (0,0)
goal = (4,4)

def heuristic(a, b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])

# BFS
def bfs(grid, start, goal):
    queue = deque([start])
    visited = set([start])
    count = 0

    while queue:
        current = queue.popleft()
        count += 1

        if current == goal:
            return count

        for dx, dy in [(1,0),(-1,0),(0,1),(0,-1)]:
            nx, ny = current[0]+dx, current[1]+dy
            if 0 <= nx < 5 and 0 <= ny < 5:
                if (nx, ny) not in visited:
                    visited.add((nx, ny))
                    queue.append((nx, ny))
    return None

# A*
def astar(grid, start, goal):
    open_list = [(0, start)]
    cost = {start: 0}
    count = 0

    while open_list:
        _, current = heapq.heappop(open_list)
        count += 1

        if current == goal:
            return count

        for dx, dy in [(1,0),(-1,0),(0,1),(0,-1)]:
            nx, ny = current[0]+dx, current[1]+dy

            if 0 <= nx < 5 and 0 <= ny < 5:
                new_cost = cost[current] + grid[nx][ny]

                if (nx, ny) not in cost or new_cost < cost[(nx, ny)]:
                    cost[(nx, ny)] = new_cost
                    priority = new_cost + heuristic(goal, (nx, ny))
                    heapq.heappush(open_list, (priority, (nx, ny)))

    return None

print("BFS nodes:", bfs(grid, start, goal))
print("A* nodes:", astar(grid, start, goal))
