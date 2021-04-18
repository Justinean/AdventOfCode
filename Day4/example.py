passports = open("Day4\example.txt").read().split("\n\n")
for i in range(len(passports)):
    passports[i] = passports[i].replace("\n", " ")

randList = []

for passport in passports:
    data = passport.split(" ")
    keyCheck = []

    for d in range(len(data)):
        key, value = data[d].split(":")
        keyCheck.append(key)
    
    randList.append(keyCheck)

print(randList)

validity = {}
for passport, value in enumerate(randList):
    for i in value:
        if i == "cid":
            validity[str(passport + 1)] = False
            break
        elif i != "cid":
            validity[str(passport + 1)] = True 

x = 0    
for i in validity:
    if validity[i] == True:
        x += 1
    print(i, validity[i])

print(x)