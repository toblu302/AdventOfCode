import sys
from functools import lru_cache

def get_component(line):
  splitted = line.split("/")
  return ( int(splitted[0]), int(splitted[1]) )

@lru_cache(maxsize=None)
def get_answer_rec(components, current_end, strength, leng):

  best_str = 0
  best_length = 0

  found = False
  for i in range(len(components)):
    p0 = components[i][0]
    p1 = components[i][1]
    if p1 == current_end:
      p0, p1 = p1, p0

    if p0 == current_end:
      found = True
      test, length = get_answer_rec(components[0:i]+components[i+1:], p1, strength+p0+p1, leng+1)
      if length > best_length:
        best_str = test
        best_length = length
      if length == best_length:
        best_str = max(best_str, test)

  if not found:
    return strength, leng

  return best_str, best_length

def get_answer(components):
  answer = 0
  return get_answer_rec(tuple(components), 0, 0, 0)[0]

def main():
  components = []
  for line in sys.stdin:
    components.append( get_component(line.strip()) )
  answer = get_answer(components)
  print("Answer:", answer)

if __name__ == "__main__":
  main()
