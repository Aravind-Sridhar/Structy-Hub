def island_count(grid):
  visited = set()
  count = 0

  for r in range(len(grid)):
    for c in range(len(grid[0])):
      if grid[r][c]


  return count
  
def explore(grid, r, c, visited):
  if r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0]):
    return False
    
  if grid[r][c] == 'W':
    return False

  if (r,c) in visited:
    return False

  visited.add((r,c))

  dir = [
    (1,0),
    (-1,0),
    (0,1),
    (0,-1)
  ]

  for dr, dc in dir:
    nr = r+dr
    nc = c+dc

    explore(grid, nr, nc, visited)

  return True
