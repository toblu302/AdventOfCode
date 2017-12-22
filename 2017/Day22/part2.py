import sys

def get_next_dir(c_dir, char):
  if char == '#':
    return (-1*c_dir[1], c_dir[0])

  if char == 'W':
    return c_dir

  if char == 'F':
    return (-1*c_dir[0], -1*c_dir[1])

  return (c_dir[1], -1*c_dir[0])

def get_next_char(char):
  if char == '#':
    return 'F'

  if char == 'W':
    return '#'

  if char == 'F':
    return '.'

  return 'W'

def get_dict(data):
  retval = {}
  for y in range(len(data)):
    for x in range(len(data)):
      if data[y][x] == '#':
        retval[ (x,y) ] = '#'
  return retval

def get_answer(data, steps):
  answer = 0

  world = get_dict(data)
  c_dir = (0,-1)
  x = round(len(data[0])//2)
  y = round(len(data)//2)

  for i in range(steps):

    cchar = "."
    if (x,y) in world:
      cchar = world[ (x,y) ] 
    c_dir = get_next_dir(c_dir, cchar)
    next_char = get_next_char(cchar)
    if next_char == '#':
      answer += 1
    world[ (x,y) ] = next_char

    y += c_dir[1]
    x += c_dir[0]


  return answer

def main():
  data = []
  for line in sys.stdin:
    data.append( list(line.strip()) )

  answer = get_answer(data, 10000000)
  print("Answer:", answer)

if __name__ == "__main__":
  main()
