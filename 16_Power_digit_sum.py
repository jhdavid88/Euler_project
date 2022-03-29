
number = 1000
pwrOfNumber = 2 ** number
stringOfPwrOfNumber = str(pwrOfNumber)
addNumber = 0 

print(len(stringOfPwrOfNumber)) #pwrOfNumber의 자릿수

for i in range(0,len(stringOfPwrOfNumber)):
    num = int(stringOfPwrOfNumber[i])
    addNumber = addNumber + num

print(addNumber)