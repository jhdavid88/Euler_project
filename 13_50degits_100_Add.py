
number = 0
addNumber = 0 

f = open("/Users/joohyungkim/Private/3_Python/01_Test/EulerPrj/13_50degits_100_Add.txt", 'r')

for i in range(0,100):
    line = f.readline()
    number = int(line)
    addNumber = addNumber + number

strNumber = str(addNumber)
print(strNumber[:10])

