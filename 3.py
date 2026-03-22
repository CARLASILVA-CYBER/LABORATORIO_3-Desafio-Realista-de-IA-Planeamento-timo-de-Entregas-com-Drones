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

def astar(grid, start, goal):
    rows, cols = len(grid), len(grid[0])
    open_list = [(0, start)]
    cost = {start: 0}

    while open_list:
        _, current = heapq.heappop(open_list)

        if current == goal:
            return cost[current]

        for dx, dy in [(1,0),(-1,0),(0,1),(0,-1)]:
            nx, ny = current[0]+dx, current[1]+dy

            if 0 <= nx < rows and 0 <= ny < cols:
                new_cost = cost[current] + grid[nx][ny]

                if (nx, ny) not in cost or new_cost < cost[(nx, ny)]:
                    cost[(nx, ny)] = new_cost
                    priority = new_cost + heuristic(goal, (nx, ny))
                    heapq.heappush(open_list, (priority, (nx, ny)))

    return None

print("Cost:", astar(grid, start, goal))
