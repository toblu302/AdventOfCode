import sys

def get_answer(data):
  answer = 0
  for line in data:
    s_depth = int(line.split(": ")[0])
    s_range = int(line.split(": ")[1])
    if s_depth%(s_range*2-2) == 0:
      answer += s_depth*s_range
  return answer

def main():
  data = []
  for line in sys.stdin:
    data.append(line)
  answer = get_answer(data)
  print(answer)

if __name__ == "__main__":
  main()
