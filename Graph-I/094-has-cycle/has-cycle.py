def has_cycle(graph):

  visited, visiting = set(), set()

  for node in graph:
    if explore(graph, node, visited, visiting):
      return True

  return False

def explore(graph, node, visited, visiting):

  if node in visited:
    return False

  if node in visiting:
    return True

  visiting.add(node)

  for neighbour in graph[node]:
    if explore(graph, neighbour, visited, visiting):
      return True

  visited.add(node)
  visiting.remove(node)

  return False
  