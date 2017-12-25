import sys

def parse_to_python(line, first=False):
  if first:
    line = line.replace("In state ", "if state == ")
  else:
    line = line.replace("In state ", "elif state == ")
  line = line.replace("If the current value is 0", "if tape[pos] == 0")
  line = line.replace("If the current value is 1", "elif tape[pos] == 1")
  line = line.replace("- Write the value ", "tape[pos] = ").replace(".","")
  line = line.replace("- Move one slot to the right", "pos += 1").replace(".","")
  line = line.replace("- Move one slot to the left", "pos -= 1").replace(".","")
  line = line.replace("- Continue with state", "state = ").replace(".","")
  line = line.replace("A","'A'").replace("B","'B'").replace("C","'C'").replace("D","'D'").replace("E","'E'").replace("F","'F'")
  line = line.replace("  ","\t")
  return line

def get_answer(data):
  global state
  global tape
  global pos

  answer = 0
  state = data[0].split()[-1][0]
  steps = int(data[1].split()[-2])
  tape = {}
  pos = 0

  python_program_list = [parse_to_python(data[3].rstrip(), True)]
  for line in data[4:]:
    python_program_list.append( parse_to_python(line.rstrip()) )

  turing_machine = "global state\nglobal tape\nglobal pos\n" + "\n".join(python_program_list)
  cc = compile(turing_machine, "yolo", "exec")

  #prev_p = 0
  #p = 0

  for i in range(steps):
    #prev_p = p
    #p = int((float(i)/float(steps))*10000.0)
    #if prev_p != p:
    #  print( p/100, "%")

    if not pos in tape:
      tape[pos] = 0
    prev_zero = tape[pos] == 0
    lastpos = pos
    exec(cc)

    if tape[lastpos] == 1 and prev_zero:
      answer += 1
    if tape[lastpos] == 0 and not prev_zero:
      answer -= 1

  return answer

def main():
  data = []
  for line in sys.stdin:
    data.append( line )
  answer = get_answer(data)
  print("Answer:", answer)

if __name__ == "__main__":
  main()
