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
  breaked = False

  def __init__(self, program):
    self.program = program
    for x in range(26):
      self.registers[ chr(x+ord('a')) ] = 0

  def get_value_of(self, x):
    if RepresentsInt(x):
      return int(x)
    return self.registers[x]

  def i_snd(self, x):
    print("SND", x, "   (", self.get_value_of(x), ")")
    self.last_sound = self.get_value_of(x)

  def i_set(self, x, y):
    print("SET", x, y, "   (", self.get_value_of(x), self.get_value_of(y), ")")
    self.registers[x] = self.get_value_of(y)

  def i_add(self, x, y):
    print("ADD", x, y, "   (", self.get_value_of(x), self.get_value_of(y), ")")
    self.registers[x] += self.get_value_of(y)

  def i_mul(self, x, y):
    print("MUL", x, y, "   (", self.get_value_of(x), self.get_value_of(y), ")")
    self.registers[x] *= self.get_value_of(y)

  def i_mod(self, x, y):
    print("MOD", x, y, "   (", self.get_value_of(x), self.get_value_of(y), ")")
    self.registers[x] %= self.get_value_of(y)

  def i_rcv(self, x):
    print("RCV", x, "   (", self.get_value_of(x), ")")
    if self.get_value_of(x) != 0:
      self.recovered = self.last_sound
    return self.recovered

  def i_jgz(self, x, y):
    print("JGZ", x, y, "   (", self.get_value_of(x), self.get_value_of(y), ")")
    if self.get_value_of(x) > 0:
      self.PC += (self.get_value_of(y)-1)
      

  def fetch_and_execute(self):
    if self.PC >= len(self.program) or self.breaked:
      return False

    instruction = self.program[self.PC].split()
    opcode = instruction[0]
    if opcode == "snd":
      self.i_snd(instruction[1])
    elif opcode == "set":
      self.i_set(instruction[1], instruction[2])
    elif opcode == "add":
      self.i_add(instruction[1], instruction[2])
    elif opcode == "mul":
      self.i_mul(instruction[1], instruction[2])
    elif opcode == "mod":
      self.i_mod(instruction[1], instruction[2])
    elif opcode == "rcv":
      result = self.i_rcv(instruction[1])
      if result != 0:
        self.breaked = True
    elif opcode == "jgz":
      self.i_jgz(instruction[1], instruction[2])

    self.PC += 1
    return True
    

def get_answer(program):
  machine = Machine(program)
  while machine.fetch_and_execute():
    pass
  return machine.recovered

def main():
  data = []
  for line in sys.stdin:
    data.append(line.strip())
  answer = get_answer(data)
  print("Answer:", answer)

if __name__ == "__main__":
  main()
