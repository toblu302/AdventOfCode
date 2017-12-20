import sys

def main():
  data = input()

  elements = len(data)
  steps = elements//2

  total_sum = 0
  for i in range(len(data)):
    if data[i] == data[(i+steps)%elements]:
      total_sum += int(data[i])
  print(total_sum)

if __name__ == "__main__":
  main()
