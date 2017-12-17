import sys

def get_answer(steps):
  current_position = 0
  before_0 = 0
  after_0 = 0
  current_after_0 = 0
  for x in range(1,50000001):
    current_position = (current_position + steps)%(before_0+1+after_0)
    #print(current_position)
    if current_position == before_0:
      #inserting something right after 0
      current_after_0 = x
    if current_position < before_0:
      before_0 += 1
    else:
      after_0 += 1
    #print(current_after_0)
    current_position = (current_position + 1)%(before_0+1+after_0)

  return current_after_0

def main():
  steps = int(input().strip())
  answer = get_answer(steps)
  print(answer)

if __name__ == "__main__":
  main()
