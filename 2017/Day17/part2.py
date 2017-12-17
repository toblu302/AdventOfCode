import sys

def get_answer(steps):
  current_position = 0
  current_after_0 = 0
  for x in range(1,50000001):
    current_position = (current_position + steps)%(x)
    if current_position == 0:
      current_after_0 = x
    current_position = (current_position + 1)%(x+1)

  return current_after_0

def main():
  steps = int(input().strip())
  answer = get_answer(steps)
  print(answer)

if __name__ == "__main__":
  main()
