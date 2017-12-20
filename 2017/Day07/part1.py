import sys

#Given a line, get the parent (the name to the left)
def get_parent(line):
  return line.split("(")[0].strip()

#Given a line, get the children (the names on the right)
def get_children(line):
  splitted = line.split("> ")
  if len(splitted) > 1:
    return splitted[1].split(", ")
  return []

#Given all input data, get the index of the names (first name is 0)
def get_node_indices(data):
  index = 0
  retval = {}
  for line in data:
    parent = get_parent(line)
    retval[parent] = index
    index += 1
  return retval

#Given an index, get the name from the node
def get_index_name(indices, index):
  for n in indices:
    if indices[n] == index:
      return n

#Given all input data, get an adjacency matrix, where adj_matrix[a][b] means that b is a children of a
def get_adj_matrix(data):
  adj_matrix = [[0]*len(data) for _ in range(len(data))]
  indices = get_node_indices(data)
  for i in range(len(data)):
    adj_matrix[i][i] = 1

  for line in data:
    parent = get_parent(line)
    children = get_children(line)
    parent_index = indices[parent]
    
    for child in children:
      child_index = indices[child]
      adj_matrix[parent_index][child_index] = 1

  return adj_matrix

#Given all input data, get the answer to the question
def get_answer(data):
  adj_matrix = get_adj_matrix(data)
  indices = get_node_indices(data)
  num_nodes = len(data)
  for x in range(num_nodes):
    possible = True
    for y in range(num_nodes):
      if adj_matrix[y][x] == 1 and x!=y:
        possible = False
        break

    if possible:
      return get_index_name(indices, x)

def main():
  data = []
  for line in sys.stdin:
    data.append(line.strip())
  answer = get_answer(data)
  print(answer)

if __name__ == "__main__":
  main()
