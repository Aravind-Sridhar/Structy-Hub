def prereqs_possible(num_courses, prereqs):
  graph = adj_list(num_courses, prereqs)
  visited, visiting = set(), set()
  for node in range(num_courses):
    if explore(graph, node, visited, visiting):
      return False

  return True

def adj_list(num_courses, prereqs):
  graph = {i: [] for i in range(num_courses)}

  for a,b in prereqs:
    graph[a].append(b)

  return graph

def explore(graph, node, visited, visiting):
  if node in visiting:
    return True
  if node in visited:
    return False
  visiting.add(node)

  for neighbour in graph[node]:
    if explore(graph, neighbour, visited, visiting):
      return True

  visiting.remove(node)
  visited.add(node)
  return False