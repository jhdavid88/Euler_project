
#num = int(input("확인할 숫자를 입력하세요: "))
num = 600851475143
divisor = [ ]
tempPrimeFactor = [ ]
lastPrimeFactor = [ ]

#약수 구하기
for i in range(1,8462696833):

    if num % i == 0:
        divisor.append(i)
        print(i)




#약수 중에 소수 구하기
for j in range(0,len(divisor)): #약수 list 값 하나하나 검사
    for k in range(1,divisor[j]+1):
        if divisor[j] % k == 0:
            tempPrimeFactor.append(k)
        setPrimeFactor  = set(tempPrimeFactor)
        PrimeFactor = list(setPrimeFactor)
        PrimeFactor.sort()

    if len(PrimeFactor) == 2:
        lastPrimeFactor.append(divisor[j])
    tempPrimeFactor = [ ]

#출력
print("%d의 약수는                   " % num + str(divisor))
print("%d의 소인수는                  " %num + str(lastPrimeFactor))
print("%d의 소인수 중에 가장 큰 값은      " %num + str(max(lastPrimeFactor)))







