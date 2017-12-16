import sys

def get_steps_to_middle(x, y):
  steps = 0
  while x!=0 or y!=0:
    td = 's'
    lr = ''
    if y<0:
      td = 'n'
    if x>0:
      lr = 'w'
    elif x<0:
      lr = 'e'

    command = td+lr
    dx,dy = command_to_delta(command)
    x += dx
    y += dy
    steps += 1
    
  return steps

def command_to_delta(d):
  x,y = 0,0
  if d == 'n':
    y += 2
  elif d == 'ne':
    y += 1
    x += 2
  elif d == 'se':
    y -= 1
    x += 2
  elif d == 's':
    y -= 2
  elif d == 'sw':
    y -= 1
    x -= 2
  elif d == 'nw':
    y += 1
    x -= 2
  return x,y

def get_location(data):
  data_list = data.split(',')
  x = 0
  y = 0
  for d in data_list:
    dx,dy = command_to_delta(d)
    x += dx
    y += dy
  return x, y

def get_answer(data):
  x,y = get_location(data)
  return get_steps_to_middle(x,y)

def main():
  data = input()
  answer = get_answer(data)
  print(answer)

if __name__ == "__main__":
  main()
