def undirected_path(edges, node_A, node_B):
  graph = build_adj(edges)
  return has_path(graph, node_A, node_B, set())
  

def has_path(graph, src, dst, seen):
  if src == dst:
    return True
  if src in seen:
    return False
  seen.add(src)

  for neighbour in graph[src]:
    if has_path(graph, neighbour, dst, seen):
      return True

  return False


def build_adj(edges):
  graph = {}
  for edge in edges:
    a,b = edge

    if a not in graph:
      graph[a] = []
    if b not in graph:
      graph[b] = []

    graph[a].append(b)
    graph[b].append(a)

  return graph