def compute_cell(grid, x, y):
  result = 0
  for dx in range(-1,2):
    for dy in range(-1,2):
      result += grid[y+dy][x+dx]

  grid[y][x] = result
  return result

def get_answer(grid, target):
  directions = [ (1,0), (0,-1), (-1,0), (0,1) ]
  c_x = len(grid[0])//2-1
  c_y = len(grid)//2
  c_direction = 0
  c_step = 1

  grid[c_y][c_x] = 1 #starting value

  i=0
  retval = 0
  stop = False
  while not stop:

    dx = directions[c_direction][0]
    dy = directions[c_direction][1]
    c_direction += 1
    c_direction %= 4

    for _ in range(c_step):
      c_x += dx
      c_y += dy

      retval = compute_cell(grid, c_x, c_y)
      if retval > target:
        stop = True
        break

    if i%2 == 1:
      c_step += 1
    i += 1

  return retval

def print_grid(grid):
  for r in grid:
    for c in r:
      print(c,end="\t")
    print("")

def main():
  square = int(input())
  grid = [ [0]*20 for _ in range(20) ]
  answer = get_answer( grid, square )
  print(answer)
  #print_grid(grid)

if __name__ == "__main__":
  main()
