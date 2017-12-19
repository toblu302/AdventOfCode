import sys

def in_map(data, x, y):
  if x >= len(data[y]) or x < 0:
    return False
  if y >= len(data) or y < 0:
    return False
  return True

def get_answer(data):
  seen_letters = ""

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
      #seen letters?
      if data[y][x] not in [" ", "+", "|", "-"]:
        seen_letters += data[y][x]
    else:
      finished = True

  return seen_letters
      

def main():
  data = []
  for line in sys.stdin:
    if line != "":
      data.append(line.strip("\n"))

  answer = get_answer(data)
  print("Answer:", answer)

if __name__ == "__main__":
  main()
