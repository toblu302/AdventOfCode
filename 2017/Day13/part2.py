import sys

def is_hit(data, delay):
  for line in data:
    s_depth = int(line.split(": ")[0])+delay
    s_range = int(line.split(": ")[1])
    if s_depth%(s_range*2-2) == 0:
      return True
  return False

def get_answer(data):
  for delay in range(10000000):
    if not is_hit(data, delay):
      return delay

def main():
  data = []
  for line in sys.stdin:
    data.append(line)
  answer = get_answer(data)
  print(answer)

if __name__ == "__main__":
  main()

5,2,6,6
