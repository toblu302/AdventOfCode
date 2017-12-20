import sys

def parse_line(line):
  exec("global p; global v; global a; " + line.replace("<","(").replace(">",")").replace(", ","; "))
  return p,v,a

def dist(x):
  return abs(x[0])+abs(x[1])+abs(x[2])

def get_answer(particles):
  best_index = 0
  for i in range(len(particles)):
    p = particles[i][0]
    v = particles[i][1]
    a = particles[i][2]
    best_p = particles[best_index][0]
    best_v = particles[best_index][1]
    best_a = particles[best_index][2]
    if dist(a) < dist(best_a):
      best_index = i
    elif dist(a) == dist(best_a):
      if dist(v) < dist(best_v):
        best_index = i
      elif dist(v) == dist(best_v):
        if dist(p) < dist(best_p):
          best_index = i

  return best_index

def main():
  particles = []
  for line in sys.stdin:
    particles.append(parse_line(line))

  answer = get_answer(particles)
  print("Answer:", answer)

if __name__ == "__main__":
  main()
