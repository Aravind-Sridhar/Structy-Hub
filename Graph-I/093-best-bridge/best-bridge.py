from collections import deque
def best_bridge(grid):
# 3 components - Finding first land using DFS - returning a set of all the grid positions, from those positions BFS to find the nearest land
  first_island = None
  for r in range(len(grid)):
    for c in range(len(grid[0])):
      first_land = explore(grid, r, c, set())

      if len(first_land)>0:
        first_island = first_land

  visited = set(first_island)
  queue = deque([])
  
  for val in first_island:
    r,c = val
    queue.append((r,c,0))

  while queue:
    r, c , dist = queue.popleft()

    if grid[r][c] == 'L' and (r,c) not in first_island:
      return dist -1

    directions = [
      (1,0),
      (-1,0),
      (0,1),
      (0,-1)
    ]

    for dr, dc in directions:
      nr = r+dr
      nc = c+dc

      new_pos = (nr,nc)

      if check_boundary(grid,new_pos) and (nr,nc) not in visited:
        queue.append((nr,nc,dist+1))
        visited.add((nr,nc))
  

def explore(grid, r, c, visited):
  pos = (r,c)
  if not check_boundary(grid,pos) or grid[r][c] == 'W':
    return visited

  if pos in visited:
    return visited

  visited.add(pos)

  explore(grid, r+1,c,visited)
  explore(grid, r-1,c,visited)
  explore(grid, r, c+1, visited)
  explore(grid, r, c-1, visited)

  return visited

def check_boundary(grid,pos):
  r,c = pos
  if r < 0 or c < 0 or r >=len(grid) or c >= len(grid[0]):
    return False
  return True