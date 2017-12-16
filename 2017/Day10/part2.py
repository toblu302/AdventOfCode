import sys

def get_list(data):
  retlist = []
  for c in data:
    retlist.append( ord(c) )
  retlist += [17, 31, 73, 47, 23]
  return retlist

#Given all input data, get the answer to the question
def get_answer(data, list_length=256):
  lengths = get_list(data)
  the_list = [x for x in range(list_length)]
  c_position = 0
  skip_size = 0

  #perform 64 rounds
  for _ in range(64):
    for length in lengths:
      for i in range(length//2):
        pos1 = (c_position+i)%list_length
        pos2 = (c_position+length-1-i)%list_length
        the_list[pos1], the_list[pos2] = the_list[pos2], the_list[pos1]

      c_position = (c_position + length + skip_size)%list_length
      skip_size += 1

  #get the xors
  xor_numbers = []
  for block in range(16):
    num = 0
    for x in the_list[block*16:block*16+16]:
      num ^= x
    xor_numbers.append( num )
  
  #get the string
  retstring = ""
  for num in xor_numbers:
    retstring += hex(num)[2:].zfill(2)


  return retstring

def main():
  data = input().strip()
  answer = get_answer(data)
  print(answer)

if __name__ == "__main__":
  main()
