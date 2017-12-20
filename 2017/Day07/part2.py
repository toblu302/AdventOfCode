import sys
from part1 import get_parent
from part1 import get_children

#Given a line, get the weight (the name to the left)
def get_weight(line):
  splitted = line.split("(")[1].strip()
  return int(splitted.split(")")[0].strip())

#Given a graph and a node, get the total weight of the node
def get_total_weight(graph, weights, node):
  total_weight = weights[node]
  for child in graph[node]:
    total_weight += get_total_weight(graph, weights, child)
  return total_weight

#Given a graph and a node, get true iff all children has the same weight
def is_balanced(graph, weights, node):
  child_weights = []
  for child in graph[node]:
    child_weights.append( get_total_weight(graph, weights, child) )

  if len(child_weights) == 0 or child_weights.count( child_weights[0] ) == len(child_weights):
    return True
  return False

#Given all input data, get a graph and all the weights
def get_graph_and_weights(data):
  graph = {}
  weights = {}
  for line in data:
    parent = get_parent(line)
    weight = get_weight(line)
    children = get_children(line)

    graph[parent] = children
    weights[parent] = weight

  return graph, weights

#recursively search for the answer
def get_answer_rec(graph, weights, node):
  #if the current node is not balanced, but each children is,
  #then one of the children must change their weight
  if not is_balanced(graph, weights, node):
    for child in graph[node]:
      if not is_balanced(graph, weights, child):
        return get_answer_rec(graph, weights, child)

    total_child_weights = {}
    for child in graph[node]:
      t_w = get_total_weight(graph, weights, child)
      if t_w not in total_child_weights:
        total_child_weights[t_w] = [child]
      else:
        total_child_weights[t_w].append(child)

    target = 0
    offending = 0
    offending_name = ""
    for weight in total_child_weights:
      if len( total_child_weights[weight] ) == 1:
        offending = weight
        offending_name = total_child_weights[weight][0]
      else:
        target = weight

    diff = target-offending
    return weights[offending_name]+diff

#Given all input data, get the answer to the question
def get_answer(data):
  graph, weights = get_graph_and_weights(data)

  #get root node
  nodes = set()
  child_nodes = set()
  for node in graph:
    for child in graph[node]:
      child_nodes.add( child )
    nodes.add(node)
  root_node = list(nodes-child_nodes)[0]

  answer = get_answer_rec(graph, weights, root_node)
  return answer

def main():
  data = []
  for line in sys.stdin:
    data.append(line.strip())
  answer = get_answer(data)
  print(answer)

if __name__ == "__main__":
  main()
