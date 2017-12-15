import sys

#Given all input data, get the answer to the question
def get_answer(data):
  total_score = 0
  c_score = 0
  in_garbage = False
  ignore_next = False
  for c in data:

    if ignore_next:
      ignore_next = False
      continue
    ignore_next = False

    if not in_garbage:
      if c == '<':
        in_garbage = True
      elif c == '{':
        c_score += 1
      elif c=='}':
        total_score += c_score
        c_score -= 1

    elif in_garbage:
      if c == '>':
        in_garbage = False
      elif c == '!':
        ignore_next = True
    

  return total_score

def main():
  data = input()
  answer = get_answer(data)
  print(answer)

if __name__ == "__main__":
  main()
