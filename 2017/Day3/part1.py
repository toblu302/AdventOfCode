def get_result(square):
  if square == 1:
    return 0

  first_squares = [1, 3, 5, 7]

  result = -1
  for first_step in first_squares:
    step = first_step
    current = 1
    circle = 0
    while current <= square:
      if( current + step > square ):
        test = circle + abs(square-current)

        if test < result or result == -1:
          result = test
          break
      current += step
      step += 8
      circle += 1

  return result

def main():
  square = int(input())
  print( get_result(square) )

if __name__ == "__main__":
  main()
