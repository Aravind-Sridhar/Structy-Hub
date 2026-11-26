from collections import deque
def closest_carrot(grid, starting_row, starting_col):
  visited = set()
  
  return explore(grid, starting_row, starting_col, visited)

def explore(grid, starting_row, starting_col, visited):
  queue = deque([(starting_row, starting_col, 0)])
  visited.add((starting_row, starting_col))
  dirextions = [
    (1,0),
    (-1,0),
    (0,1),
    (0, -1)
  ]
  while queue:
    r,c,dist = queue.popleft()

    if grid[r][c] == 'C':
      return dist
    

    for dr, dc in dirextions:
      nr = r + dr
      nc = c + dc

      if nr >= 0 and nc >= 0 and nr < len(grid) and nc < len(grid[0]) and (nr,nc) not in visited and grid[nr][nc] != 'X':
        visited.add((nr,nc))
        queue.append((nr,nc,dist+1))
  return -1