newNumber = 0
numArray = []

f = open("/Users/joohyungkim/Private/3_Python/01_Test/EulerPrj/8_Add_Number.txt", 'r')
number= f.readline()

for n in range(0,987):
    newNumber = int(number[n]) * int(number[n+1]) * int(number[n+2]) * int(number[n+3]) * int(number[n+4]) * int(number[n+5]) * int(number[n+6]) * int(number[n+7]) * int(number[n+8]) * int(number[n+9]) * int(number[n+10]) * int(number[n+11]) * int(number[n+12])
    numArray.append(newNumber)

print(max(numArray))
print(numArray.index(max(numArray)))





