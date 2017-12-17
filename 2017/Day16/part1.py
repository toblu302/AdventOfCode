import sys

def do_move(programs, move):
  if move[0] == 's':
    spin = int( move[1:] )
    programs = programs[-spin:] + programs[:-spin]
    return programs
  if move[0] == 'x':
    pos0 = int(move[1:].split('/')[0])
    pos1 = int(move[1:].split('/')[1])
    programs[pos0], programs[pos1] = programs[pos1], programs[pos0]
    return programs
  if move[0] == 'p':
    p0 = move[1]
    p1 = move[3]
    pos0 = programs.index(p0)
    pos1 = programs.index(p1)
    programs[pos0], programs[pos1] = programs[pos1], programs[pos0]
    return programs
  

def get_answer(moves, letters="abcdefghijklmnop"):
  programs = [x for x in letters]
  
  for move in moves:
    programs = do_move(programs, move)

  return ''.join(programs)

def main():
  moves = input().split(',')
  answer = get_answer(moves)
  print(answer)

if __name__ == "__main__":
  main()
