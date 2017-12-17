import sys

def lowest_16_bits_are_equal(a, b):
  return (a&0xFFFF) == (b&0xFFFF)

def get_next_a(a):
  while True:
    a *= 16807
    a %= 2147483647
    if a%4 == 0:
      return a

def get_next_b(b):
  while True:
    b *= 48271
    b %= 2147483647
    if b%8 == 0:
      return b

def get_answer(a, b):
  answer = 0
  for _ in range(5000000):
    a = get_next_a(a)
    b = get_next_b(b)
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
