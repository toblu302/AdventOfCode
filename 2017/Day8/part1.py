import sys

def get_register(line):
  return line.split()[0]

def get_sign(line):
  val = line.split()[1]
  if val == "inc":
    return 1
  return -1

def get_value(line):
  return int(line.split()[2])

def get_conditional_register(line):
  return line.split()[-3]

def get_conditional(line):
  return " ".join(line.split()[-2:])

#Given all input data, get the answer to the question
def get_answer(data):
  registers = {}
  for line in data:
    reg = get_register(line)
    sign = get_sign(line)
    value = get_value(line)
    conditional_register = get_conditional_register(line)
    conditional = get_conditional(line)

    if reg not in registers:
      registers[reg] = 0
    if conditional_register not in registers:
      registers[conditional_register] = 0

    c_register_val = registers[conditional_register]
    eval_string = str(c_register_val) + " " + conditional
    if eval(eval_string):
      registers[reg] += sign*value


  found = False
  max_val = 0
  for register in registers:
    if registers[register] > max_val or found==False:
      max_val = registers[register]
      found = True

  return max_val

def main():
  data = []
  for line in sys.stdin:
    data.append(line.strip())
  answer = get_answer(data)
  print(answer)

if __name__ == "__main__":
  main()
