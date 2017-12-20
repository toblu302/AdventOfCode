import sys
def main():
  result = 0

  for line in sys.stdin:
    int_list = list( map( int, line.split() ) )
    sorted_list = sorted( int_list )

    found = False
    for e1 in int_list:
      for e2 in int_list:
        if e1 != e2 and e1 % e2 == 0:
          result += e1//e2
          found = True
          break

      if found:
        break

  print(result)
    

if __name__ == "__main__":
  main()
