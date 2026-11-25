def connected_components_count(graph):
  visited = set()
  count = 0

  for node in graph:
    if explore(graph, node, visited):
      count+=1
    




def explore(graph, src, visited):
  if src in visited:
    return False

  visited.add(src)

  for neighbor in graph[src]:
    explore(graph, neighbor, visited)

  return True

  