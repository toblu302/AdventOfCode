import sys
def main():
  result = 0

  for line in sys.stdin:
    int_list = list( map( int, line.split() ) )
    largest = max(int_list)
    smallest = min(int_list)

    result += (largest-smallest)

  print(result)
    

if __name__ == "__main__":
  main()
