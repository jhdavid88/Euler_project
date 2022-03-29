i = 0
number = 0
numOfPrime= []
numPrime = 0

for number in range(1, 100000000000000000000):

    for i in range(1, number+1):
        if number % i == 0:
            numOfPrime.append(i)
    
    if len(numOfPrime) == 2:
        numPrime = numPrime + 1
        print("%d번째 소수는 %d입니다." %(numPrime, numOfPrime[1]))        
    
    if numPrime == 10001:
        break

    numOfPrime = [ ]
    

    