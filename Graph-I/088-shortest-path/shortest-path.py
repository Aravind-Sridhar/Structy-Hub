from collections import deque

def shortest_path(edges, node_A, node_B):
  graph = adj_list(edges)
  visited = set([node_A])
  queue = deque([(node_A, 0)])

  while queue:
    current, dist = queue.popleft()
    
    if current == node_B:
      return dist
      
    for neighbour in graph[current]:
      if neighbour not in visited:
        visited.add(neighbour)
        queue.append((neighbour,dist+1))

  return -1

def adj_list(edges):
  graph = {}

  for a, b in edges:
    if a not in graph:
      graph[a] = []
    if b not in graph:
      graph[b] = []
    graph[a].append(b)
    graph[b].append(a)
  
  return graph