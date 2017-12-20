import sys

def RepresentsInt(s):
  try: 
    int(s)
    return True
  except ValueError:
    return False

class Machine:

  def __init__(self, program, p):
    self.program = program
    self.registers = {}
    for x in range(26):
      self.registers[ chr(x+ord('a')) ] = 0
    self.registers['p'] = p
    self.queue = []
    self.waiting = False
    self.terminated = False
    self.snd_count = 0
    self.PC = 0

  def get_value_of(self, x):
    if RepresentsInt(x):
      return int(x)
    return self.registers[x]

  def set_reciever(self,other):
    self.other_machine = other

  def i_snd(self, x):
    self.other_machine.queue.append( self.get_value_of(x) )
    self.snd_count += 1

  def i_set(self, x, y):
    self.registers[x] = self.get_value_of(y)

  def i_add(self, x, y):
    self.registers[x] += self.get_value_of(y)

  def i_mul(self, x, y):
    self.registers[x] *= self.get_value_of(y)

  def i_mod(self, x, y):
    self.registers[x] %= self.get_value_of(y)

  def i_rcv(self, x):
    if len(self.queue) > 0:
      self.registers[x] = self.queue[0]
      del self.queue[0]
      self.waiting = False
    else:
      self.waiting = True

  def i_jgz(self, x, y):
    if self.get_value_of(x) > 0:
      self.PC += (self.get_value_of(y)-1)
      

  def fetch_and_execute(self):
    if self.terminated:
      return False
    self.waiting = False

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
      self.i_rcv(instruction[1])
    elif opcode == "jgz":
      self.i_jgz(instruction[1], instruction[2])

    if not self.waiting:
      self.PC += 1

    if self.PC >= len(self.program):
      self.terminated = True
    if (self.waiting and self.other_machine.waiting):
      self.terminated = True
    if (self.waiting and self.other_machine.terminated):
      self.terminated = True

    #self.print_state()

    return True
    

def get_answer(program):
  machine1 = Machine(program, 0)
  machine2 = Machine(program, 1)
  machine1.set_reciever(machine2)
  machine2.set_reciever(machine1)

  while not machine1.terminated:
    machine1.fetch_and_execute()
    machine2.fetch_and_execute()

  return machine2.snd_count

def main():
  data = []
  for line in sys.stdin:
    data.append(line.strip())
  answer = get_answer(data)
  print("Answer:", answer)

if __name__ == "__main__":
  main()
