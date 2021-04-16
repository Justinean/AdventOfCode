passwords = open("fuckthis.txt").read().splitlines()
minimum = []
maximum = []
letter = []
password = []

l = 0
for i in passwords:
    temp = i.split(" ")
    temp2 = temp[0].split("-")
    minimum.append(temp2[0])
    maximum.append(temp2[1])
    letter.append(temp[1][0])
    password.append(temp[2])







x = 0
z = 0
def validator(password, z):
    global x
    for words in password:
        if (words[int(minimum[z])-1] == letter[z] and not words[int(maximum[z])-1] == letter[z]) or ((not words[int(minimum[z])-1] == letter[z] and words[int(maximum[z])-1] == letter[z])):
            x += 1
        
         
        z += 1
validator(password, z)

print(x)
