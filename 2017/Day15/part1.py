import sys

def lowest_16_bits_are_equal(a, b):
  return (a&0xFFFF) == (b&0xFFFF)

def get_answer(a, b):
  answer = 0
  a_factor = 16807
  b_factor = 48271
  divider = 2147483647
  for _ in range(40000000):
    a *= a_factor
    a %= divider
    b *= b_factor
    b %= divider
    if lowest_16_bits_are_equal(a, b):
      answer += 1
  return answer

def main():
  a = int(input().split()[-1])
  b = int(input().split()[-1])
  answer = get_answer(a, b)
  print(answer)

if __name__ == "__main__":
  main()
