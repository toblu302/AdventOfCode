import sys

def perform_redistribution(banks):
  length = len(banks)
  maximum = max(banks)
  max_index = banks.index(maximum)
  banks[max_index] = 0
  adding = maximum//len(banks)
  adding_remainder = maximum%length
  
  for i in range(length):
    banks[i] += adding

  for i in range(adding_remainder):
    banks[ (max_index+1+i)%length ] += 1

def get_answer(banks):
  seen_distributions = []
  answer = 0
  while banks not in seen_distributions:
    seen_distributions.append( list(banks) )
    perform_redistribution(banks)
    answer += 1

  return answer - seen_distributions.index(banks)

def main():
  banks = [int(x) for x in input().split()]
  answer = get_answer(banks)
  print(answer)

if __name__ == "__main__":
  main()
