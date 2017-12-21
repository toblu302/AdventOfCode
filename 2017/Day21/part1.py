import sys

def get_tuple(data):
  return tuple([tuple(x) for x in data.split("/")])

def get_flipped_h(t):
  retval = []
  for r in t:
    retval.append( r[::-1] )
  return tuple(retval)

def get_flipped_v(t):
  return t[::-1]

def get_rotated(t):
  ret_list = [ [0]*len(t) for _ in range(len(t)) ]
  for r in range(len(t)):
    for c in range(len(t)):
      ret_list[r][len(t)-1-c] = t[c][r]
  return tuple([tuple(x) for x in ret_list])

def get_all_lhs(t):
  retval = set([t])
  for _ in range(4):
    retval.add( t )
    retval.add( get_flipped_v(t) )
    retval.add( get_flipped_h(t) )
    t = get_rotated(t)

  return retval

def get_rules(data):
  rules = {}
  for line in data:
    splitted = line.split(" => ")
    rhs = get_tuple(splitted[1])
    f_lhs = get_tuple(splitted[0])
    lhss = get_all_lhs(f_lhs)
    for lhs in lhss:
      rules[lhs] = rhs
  return rules

def do_iteration(rules, pattern):
  div = 3
  if len(pattern)%2 == 0:
    div = 2

  new_size = (len(pattern)//div)*(div+1)
  new_pattern = [ [0]*new_size for _ in range(new_size)]
  replacements = []
  for Y in range(len(pattern)//div):
    for X in range(len(pattern)//div):
      slice_list = []
      for i in range(div):
        slice_list.append( tuple(pattern[Y*div+i][X*div:X*div+div]) )
      the_slice = tuple(slice_list)

      replacement = rules[the_slice]
      replacements.append( replacement )
      for y in range(len(replacement)):
        for x in range(len(replacement)):
          new_pattern[Y*(div+1)+y][X*(div+1)+x] = replacement[y][x]
  return new_pattern

def count_on(pattern):
  answer = 0
  for row in pattern:
    answer += row.count("#")
  return answer

def get_answer(data, iterations):
  rules = get_rules(data)
  pattern = [[".","#","."],
             [".",".","#"],
             ["#","#","#"]]
  for _ in range(iterations):
    pattern = do_iteration(rules, pattern)
  return count_on(pattern)


def main():
  data = []
  for line in sys.stdin:
    data.append( line.strip() )

  answer = get_answer(data, 5)
  print("Answer:", answer)

if __name__ == "__main__":
  main()
