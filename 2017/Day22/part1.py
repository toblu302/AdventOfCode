import sys

def pad_grid(grid, padding):
  top_down_pad = ["."]*(len(grid)+2*padding)
  left_right_pad = ["."]*padding
  new_grid = [["."]*(len(grid)+2*padding) for _ in range(padding)]
  for row in grid:
    new_grid += [(left_right_pad + row + left_right_pad)]
  new_grid += [["."]*(len(grid)+2*padding) for _ in range(padding)]
  return new_grid

def get_next_dir(c_dir, infected):
  if infected:
    return (-1*c_dir[1], c_dir[0])
  return (c_dir[1], -1*c_dir[0])

def get_answer(grid, steps):
  answer = 0

  c_dir = (0,-1)
  x = round(len(grid[0])//2)
  y = round(len(grid)//2)

  padding = steps//2
  grid = pad_grid(grid, padding)
  x += padding
  y += padding

  for _ in range(steps):
    c_dir = get_next_dir(c_dir, grid[y][x] == '#')
    if grid[y][x] == '#':
      grid[y][x] = '.'
    else:
      grid[y][x] = '#'
      answer += 1
    y += c_dir[1]
    x += c_dir[0]

  return answer

def main():
  data = []
  for line in sys.stdin:
    data.append( list(line.strip()) )

  answer = get_answer(data, 10000)
  print("Answer:", answer)

if __name__ == "__main__":
  main()
