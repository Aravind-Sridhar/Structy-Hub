def minimum_island(grid):
  visited = set()
  count = 0
  smallest = float('inf')

  for r in range(len(grid)):
    for c in range(len(grid[0])):
      count = explore(grid, r, c, visited)

      if count < smallest and count > 0:
        smallest = count

  if smallest == float('inf'):
    return 0

def explore(grid, r, c, visited):
  count = 0
  if r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0]):
    return 0
  if grid[r][c] == 'W':
    return 0
  if (r,c) in visited:
    return 0
  visited.add((r,c))
  count+=1
  dir = [
    (1, 0),
    (-1,0),
    (0,1),
    (0, -1)
  ]

  for dr, dc in dir:
    nr = r+dr
    nc = c+dc

    count+=explore(grid, nr, nc, visited)

  return count