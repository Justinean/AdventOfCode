terrain = open("../Day 3/example.txt").read().splitlines()

def trees(increment):
    trees = 0
    dx = 0
    if increment == 6:
        dx = 1
    print(increment)
    for i in terrain:
        if dx > 30:
            print(dx)
            dx -= 31
            print(dx)
        if '#' in i[dx]:
            trees += 1
        dx += increment
    return trees
a = trees(1)
b = trees(3)
c = trees(5)
d = trees(6)

trees = 0
dx = 1
idk = 0
for i in terrain:
    if dx > 30:
        dx -= 31
    if idk % 2 != 0:
        if "#" in i[dx]:
            trees += 1
        dx += 1    
    idk += 1    
e = trees




print(a, b, c, d, e)


