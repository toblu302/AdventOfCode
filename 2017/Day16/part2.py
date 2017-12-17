import sys
from part1 import get_answer as do_cycle
from part1 import do_move

def get_answer(moves, letters="abcdefghijklmnop"):
  visited = [letters]
  visited_set = set( [letters] )
  mutation = letters
  cycle_start_index = 0
  remaining_cycles = 0
  for i in range(1000000000):
    mutation = do_cycle(moves, mutation)
    if mutation in visited_set:
      cycle_start_index = visited.index(mutation)
      remaining_cycles = 1000000000-1-i
      break
    visited_set.add(mutation)
    visited.append(mutation)
  
  final_index = (remaining_cycles % (len(visited) - cycle_start_index)) + cycle_start_index
  return visited[final_index]

def main():
  moves = input().split(',')
  answer = get_answer(moves)
  print(answer)

if __name__ == "__main__":
  main()
