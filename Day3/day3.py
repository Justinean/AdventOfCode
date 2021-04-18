terrain = open("Day3\input.txt").read().splitlines()
answer = 1
a = (1, 1)
b = (3, 1)
c = (5, 1)
d = (7, 1)
e = (1, 2)
variables = [a, b, c, d, e]
product = []
def trees(slope):
    x = 0
    y = 0
    dx, dy = slope
    trees = 0
    for i in range(len(terrain)):
        if x > (len(terrain[0]) - 1):
            x -= len(terrain[0])
        if y > len(terrain):
            pass
        else:
            if terrain[y][x] == "#":
                trees += 1
        x += dx
        y += dy
    return trees

for i in variables:
    listItem = trees(i)
    product.append(listItem)
print(product)

for i in range(len(product)):
    answer *= product[i]
print(answer)