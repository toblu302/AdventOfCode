import sys
from functools import lru_cache

def get_component(line):
  splitted = line.split("/")
  return ( int(splitted[0]), int(splitted[1]) )

@lru_cache(maxsize=None)
def get_answer_rec(components, current_end, strength):

  best_str = 0

  found = False
  for i in range(len(components)):
    p0 = components[i][0]
    p1 = components[i][1]
    if p1 == current_end:
      p0, p1 = p1, p0

    if p0 == current_end:
      found = True
      best_str = max(best_str, get_answer_rec(components[0:i]+components[i+1:], p1, strength+p0+p1))

  if not found:
    return strength

  return best_str

def get_answer(components):
  answer = 0
  return get_answer_rec(tuple(components), 0, 0)

def main():
  components = []
  for line in sys.stdin:
    components.append( get_component(line.strip()) )
  answer = get_answer(components)
  print("Answer:", answer)

if __name__ == "__main__":
  main()
