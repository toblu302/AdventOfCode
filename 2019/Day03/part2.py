from collections import namedtuple

path1 = input().split(",")
path2 = input().split(",")

Point = namedtuple('Point', ['x', 'y'])

def get_deltas(step):
    dx = 0
    dy = 0
    num = int(step[1:])
    if step[0] == "R":
        dx = num
    elif step[0] == "L":
        dx = num*-1
    elif step[0] == "U":
        dy = num
    else:
        dy = num*-1
    return dx, dy

def between(a, b, c):
    return a < b <= c or c < b <= a

result = 9999999999999999999
c1 = Point(x=0, y=0)
c1steps = 0
for step1 in path1:
    dx1, dy1 = get_deltas(step1)

    c2 = Point(x=0, y=0)
    c2steps = 0
    for step2 in path2:
        dx2, dy2 = get_deltas(step2)

        if (between(c1.x, c2.x, c1.x+dx1) and between(c2.y, c1.y, c2.y+dy2)) or \
            (between(c1.y, c2.y, c1.y+dy1) and between(c2.x, c1.x, c2.x+dx2)):
            totsteps = c1steps+abs(c1.x-c2.x)+c2steps+abs(c1.y-c2.y)
            result = min(result, totsteps)

        c2 = Point(c2.x+dx2, c2.y+dy2)
        c2steps += abs(dx2)+abs(dy2)

    c1 = Point(c1.x+dx1, c1.y+dy1)
    c1steps += abs(dx1)+abs(dy1)

print(result)
