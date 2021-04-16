example = open("input.txt").readlines()

newList = []

for i in example:
    newList.append(int(i))

for i in newList:
    for h in newList: 
        for j in newList:
            if (i+h+j) == 2020:
                break
        if (i+h+j) == 2020:
            break
    if (i+h+j) == 2020:
        break
        
print(i)
print(h)
print(j)
print(i*h*j)