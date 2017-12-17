import sys
sys.path.append('../')
from Day10.part2 import get_answer as get_knot_hash 

def get_answer(data):
  answer = 0
  for i in range(128):
    row_string = data + "-" + str(i)
    row_hash = get_knot_hash(row_string)
    row_bits = bin(int(row_hash, 16))[2:]
    answer += row_bits.count('1')
  return answer

def main():
  data = input().strip()
  answer = get_answer(data)
  print(answer)

if __name__ == "__main__":
  main()
