def largest_component(graph):
  largest = 0
  visited = set()
  
  for node in graph:
    current = explore(graph, node, visited)
    if current > largest:
      largest = current

  return largest

def explore(graph, src, visited):
  if src in visited:
    return 0

  visited.add(src)
  count=1
  for neighbor in graph[src]:
    count+=explore(graph, neighbor, visited)

  return count
    