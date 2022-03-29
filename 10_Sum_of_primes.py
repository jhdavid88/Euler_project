
divisor = [ ]
sumOfPrimes = 0
numPrimetill = 2000000

for num in range(1,numPrimetill+1):

    for i in range(1,num+1):
        if num % i == 0:
            divisor.append(i)
    
    if len(divisor) == 2:
        sumOfPrimes = sumOfPrimes + divisor[1]

    divisor = []
print(sumOfPrimes)

