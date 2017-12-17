import sys

def get_answer(steps):
  circular_buffer = [0]
  current_position = 0
  for x in range(1,2018):
    current_position = (current_position + steps)%len(circular_buffer)
    circular_buffer.insert(current_position+1, x)
    current_position = (current_position + 1)%len(circular_buffer)

  index = circular_buffer.index(2017)
  return circular_buffer[(index+1)%len(circular_buffer)]

def main():
  steps = int(input().strip())
  answer = get_answer(steps)
  print(answer)

if __name__ == "__main__":
  main()
