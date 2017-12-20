def main():
  data = input()
  total_sum = 0
  for i in range(-1,len(data)-1):
    if data[i] == data[i+1]:
      total_sum += int(data[i])
  print(total_sum)

if __name__ == "__main__":
  main()
