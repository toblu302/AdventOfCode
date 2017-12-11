import sys

def get_answer(offsets):
  jumps = 0
  c = 0

  while c<len(offsets) and c>=0:
    offset = offsets[c]

    if offsets[c] >= 3:
      offsets[c] -= 1
    else:
      offsets[c] += 1

    c += offset
    jumps += 1

  return jumps

def main():
  offsets = []
  for line in sys.stdin:
    offsets.append( int(line) )

  answer = get_answer(offsets)
  print(answer)

if __name__ == "__main__":
  main()
