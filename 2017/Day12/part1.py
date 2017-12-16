import sys

def get_graph(data):
  graph = {}
  for line in data:
    splitted = line.split(" <-> ")
    node = splitted[0].strip()
    neighbors = [x.strip() for x in splitted[1].split(", ")]
    graph[node] = neighbors
  return graph

def get_reachable_from(graph, node):
  to_visit = [node]
  visited = set()
  while to_visit:
    current = to_visit[0]
    visited.add(current)
    to_visit = to_visit[1:]
    if current not in graph:
      continue
    for neighbor in graph[current]:
      if neighbor not in visited:
        to_visit.append(neighbor)
  return visited

def get_answer(data):
  graph = get_graph(data)
  return len(get_reachable_from(graph, '0'))

def main():
  data = []
  for line in sys.stdin:
    data.append(line)
  answer = get_answer(data)
  print(answer)

if __name__ == "__main__":
  main()
