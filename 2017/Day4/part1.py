import sys

def is_valid(passphrase):
  words = passphrase.split()
  used_words = set()
  for word in words:
    if word in used_words:
      return False
    used_words.add(word)
  return True

def main():
  result = 0
  for line in sys.stdin:
    if is_valid(line):
      result += 1

  print(result)

if __name__ == "__main__":
  main()
