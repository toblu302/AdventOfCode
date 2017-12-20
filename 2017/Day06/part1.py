import sys

def perform_redistribution(banks):
  maximum = max(banks)
  max_index = banks.index(maximum)
  banks[max_index] = 0
  adding = maximum//len(banks)
  adding_remainder = maximum%len(banks)

  banks = [x+adding for x in banks]
  for i in range(adding_remainder):
    banks[ (max_index+1+i)%len(banks) ] += 1
  return banks

def get_answer(banks):
  seen_distributions = set()
  answer = 0
  while tuple(banks) not in seen_distributions:
    seen_distributions.add( tuple(banks) )
    banks = perform_redistribution(banks)
    answer += 1

  return answer

def main():
  banks = [int(x) for x in input().split()]
  answer = get_answer(banks)
  print(answer)

if __name__ == "__main__":
  main()
