import sys
from part1 import get_answer as get_on_after_iterations

def main():
  data = []
  for line in sys.stdin:
    data.append( line.strip() )

  answer = get_on_after_iterations(data, 18)
  print("Answer:", answer)

if __name__ == "__main__":
  main()
