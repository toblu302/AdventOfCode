import sys

def RepresentsInt(s):
  try: 
    int(s)
    return True
  except ValueError:
    return False

class Machine:
  registers = {}
  PC = 0
  last_sound = 0
  recovered = 0
  program = []
  visited_states = set()
  times_mul = 0
  breaked = False

  def __init__(self, program):
    self.program = program
    for x in range(26):
      self.registers[ chr(x+ord('a')) ] = 0

  def get_value_of(self, x):
    if RepresentsInt(x):
      return int(x)
    return self.registers[x]

  def i_set(self, x, y):
    self.registers[x] = self.get_value_of(y)

  def i_sub(self, x, y):
    self.registers[x] -= self.get_value_of(y)

  def i_mul(self, x, y):
    self.registers[x] *= self.get_value_of(y)

  def i_jnz(self, x, y):
    if self.get_value_of(x) != 0:
      self.PC += (self.get_value_of(y)-1)
      

  def fetch_and_execute(self):
    if self.PC >= len(self.program) or self.breaked:
      return False

    instruction = self.program[self.PC].split()
    opcode = instruction[0]
    if opcode == "set":
      self.i_set(instruction[1], instruction[2])
    elif opcode == "sub":
      self.i_sub(instruction[1], instruction[2])
    elif opcode == "mul":
      self.i_mul(instruction[1], instruction[2])
      self.times_mul += 1
    elif opcode == "jnz":
      self.i_jnz(instruction[1], instruction[2])

    self.PC += 1
    return True
    

def get_answer(program):
  machine = Machine(program)
  while machine.fetch_and_execute():
    pass
  return machine.times_mul

def main():
  data = []
  for line in sys.stdin:
    data.append(line.strip())
  answer = get_answer(data)
  print("Answer:", answer)

if __name__ == "__main__":
  main()
