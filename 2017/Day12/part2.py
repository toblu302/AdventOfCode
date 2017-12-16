import sys
from part1 import get_graph
from part1 import get_reachable_from

def get_answer(data):
  graph = get_graph(data)
  group_count = 0
  visited = set()
  for node in graph:
    if node not in visited:
      visited |= get_reachable_from(graph, node)
      group_count += 1

  return group_count

def main():
  data = []
  for line in sys.stdin:
    data.append(line)
  answer = get_answer(data)
  print(answer)

if __name__ == "__main__":
  main()
