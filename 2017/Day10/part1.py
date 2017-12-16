import sys

#Given all input data, get the answer to the question
def get_answer(lengths, list_length=256):
  the_list = [x for x in range(list_length)]
  c_position = 0
  skip_size = 0

  for length in lengths:
    for i in range(length//2):
      pos1 = (c_position+i)%list_length
      pos2 = (c_position+length-1-i)%list_length
      the_list[pos1], the_list[pos2] = the_list[pos2], the_list[pos1]

    c_position = (c_position + length + skip_size)%list_length
    skip_size += 1

  return the_list[0]*the_list[1]

def main():
  length_sequence = [int(x) for x in input().split(',')]
  answer = get_answer(length_sequence)
  print(answer)

if __name__ == "__main__":
  main()
