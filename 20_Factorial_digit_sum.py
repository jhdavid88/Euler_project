facto = 100
number = 1
num = 0

while facto > 0:
    number = number * facto
    facto = facto - 1

for i in range(0,len(str(number))):
    num = num + int((str(number)[i]))

print(num)

