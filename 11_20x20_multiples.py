
f = open("/Users/joohyungkim/Private/3_Python/01_Test/EulerPrj/11_20x20_numbers.txt", 'r')

row = [ ]
num = 0
parr = []
colu = []
cros = []
cros2 = []

while True:
    line = f.readline()
    if not line: break

    for i in range (0,20):
        num = int(str(line[3*i])+str(line[3*i+1]))
        row.append(num)

for numRow in range(0,20):
    for k in range(20*numRow,20*numRow+17):
        parCal = row[k]*row[k+1]*row[k+2]*row[k+3]
        parr.append(parCal)

for p in range(0,20):
    for l in range(0,17):
        colCal = row[20*l+p]*row[20*l+20+p]*row[20*l+40+p]*row[20*l+60+p]
        colu.append(colCal)


for j in range (0,17):   
    for i in range (0,17):
        crsCal = row[i+20*j]*row[20+1+i+20*j]*row[40+2+i+20*j]*row[60+3+i+20*j]
        cros.append(crsCal)

for j in range (0,17):   
    for i in range (0,17):
        crsCal2 = row[3+i+20*j]*row[20+2+i+20*j]*row[40+1+i+20*j]*row[60+i+20*j]
        cros2.append(crsCal2)

print(cros)
print(max(cros))

print(max(max(parr),max(colu),max(cros),max(cros2)))

f.close()
