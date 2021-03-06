import sys
from part1 import in_map

def get_answer(data):
  steps_taken = 1

  y = 0
  x = 0
  c_dir = (0,1) #(dx, dy)

  #find starting x
  for cx in range(len(data[0])):
    if data[0][cx] == '|':
      x = cx
      break

  finished = False
  while not finished:
    dx = c_dir[0]
    dy = c_dir[1]

    #handle crossings
    if data[y][x] == '+':
      #going left/right
      if dx != 0:
        #if we can not continue forward, try to turn
        if not (in_map(data,x+dx,y) and data[y][x+dx] not in [" ", "|"]):
          #try to turn
          if in_map(data, x, y-1) and data[y-1][x] not in [" ", "-"]: #go up
            c_dir = (0,-1)
          elif in_map(data, x, y+1) and data[y+1][x] not in [" ", "-"]: #go down
            c_dir = (0,1)

      #going up/down
      elif dy != 0:
        #if we can not continue forward, try to turn
        if not (in_map(data,x,y+dy) and data[y+dy][x] not in [" ", "-"]):
          if in_map(data, x+1, y) and data[y][x+1] not in [" ", "|"]: #go right
            c_dir = (1,0)
          elif in_map(data, x-1, y) and data[y][x-1] not in [" ", "|"]: #go right
            c_dir = (-1,0)

    #continue straigt for as far as possible
    dx = c_dir[0]
    dy = c_dir[1]

    if in_map(data,x+dx,y+dy) and data[y+dy][x+dx] != ' ':
      x += dx
      y += dy
      steps_taken += 1
    else:
      finished = True

  return steps_taken
      

def main():
  data = []
  for line in sys.stdin:
    data.append(line.strip("\n"))

  answer = get_answer(data)
  print("Answer:", answer)

if __name__ == "__main__":
  main()
