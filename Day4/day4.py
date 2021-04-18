passports = open("Day4\input.txt").read().split("\n\n")
for i in range(len(passports)):
    passports[i] = passports[i].replace("\n", " ")

randList = []

for passport in passports:
    data = passport.split(" ")
    keyCheck = []

    for d in range(len(data)):
        key, value = data[d].split(":")
        keyCheck.append({key: value})
    
    randList.append(keyCheck)

# print(randList)

validity = {}
for passport, value in enumerate(randList):
    for i in value:
        #create thing to check for cid, if, automate getting the dict value
        if len(randList[passport]) == 8 or (len(randList[passport]) == 7 and i["cid"] == False):           
            print(len(randList[passport]), i, True)
            validity[str(passport + 1)] = True
        elif len(randList[passport]) < 8 and int(i["cid"]) >= 0:
            validity[str(passport + 1)] = False
            print(len(randList[passport]), i, False)
            break

print(validity)
x = 0    
for i in validity:
    if validity[i] == True:
        x += 1
    print(i, validity[i])

print(x)