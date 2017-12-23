def isPrime(num):
  if num%2 == 0:
    return True
  for i in range(3, num, 2):
    if num%i == 0:
      return True
  return False

answer = 0
for c in range(109900, 126901, 17):
  if isPrime(c):
    answer += 1

print(answer)
