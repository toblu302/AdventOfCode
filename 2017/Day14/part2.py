import sys
sys.path.append('../')
from Day10.part2 import get_answer as get_knot_hash 

def flood_fill(grid, x, y):
  if x<0 or x>127 or y<0 or y>127:
    return
  if grid[y][x] == '0':
    return
  grid[y][x] = '0'
  for dx, dy in [(1,0), (0,1), (-1,0), (0,-1)]:
    flood_fill(grid, x+dx, y+dy)

def get_regions(grid):
  regions = 0
  for y in range(128):
    for x in range(128):
      if grid[y][x] == '1':
        regions += 1
        flood_fill(grid, x, y)
  return regions

def get_answer(data):
  #get the grid
  grid = []
  for i in range(128):
    row_string = data + "-" + str(i)
    row_hash = get_knot_hash(row_string)
    row_bits = list(bin(int(row_hash, 16))[2:].zfill(128))
    grid.append( row_bits )
  return get_regions(grid)

def main():
  data = input().strip()
  answer = get_answer(data)
  print(answer)

if __name__ == "__main__":
  main()
