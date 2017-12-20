import sys

def parse_line(line):
  exec("global p; global v; global a; " + line.replace("<","[").replace(">","]").replace(", ","; "))
  return [list(p),list(v),list(a)]

def dist(x):
  return abs(x[0])+abs(x[1])+abs(x[2])

def tick(particles):
  for particle in particles:
    particle[1][0] += particle[2][0]
    particle[1][1] += particle[2][1]
    particle[1][2] += particle[2][2]
    particle[0][0] += particle[1][0]
    particle[0][1] += particle[1][1]
    particle[0][2] += particle[1][2]

def collision(p1, p2):
  return p1[0]==p2[0] 

def collisions(particles):
  colliding_particles = set()
  for i in range(len(particles)):
    for j in range(i+1,len(particles)):
      if particles[i][0] == particles[j][0]:
        colliding_particles.add(i)
        colliding_particles.add(j)
  return colliding_particles

def get_answer(particles):
  best_index = 0
  total_removed = 0
  stable = 100
  while stable!=0:
    tick(particles)
    colliding = collisions(particles)
    for index in sorted(colliding, reverse=True):
      del particles[index]

    if len(colliding) != 0:
      stable = 100
    stable -= 1
      
  return len(particles)

def main():
  particles = []
  for line in sys.stdin:
    particles.append(parse_line(line))

  answer = get_answer(particles)
  print("Answer:", answer)

if __name__ == "__main__":
  main()
