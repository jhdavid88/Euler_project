import time

start_time = time.time()

number = 10000
addNum = 0 
div = [ ]
revDiv = [ ]
addRevNum = 0
amiNum = [ ]
amiNumSum = 0 

for m in range(2,number+1): #number 이하의 수

    for i in range(1,m): #m 의 약수 구하기 (number 제외)
        if m % i == 0:
            div.append(i)
    
    for j in range(0,len(div)): #number 의 약수의 합 구하기
        addNum = addNum + div[j]
    
    for k in range(1,addNum): #약수의 합(addNum)이 amicable number 인지 확인
        if addNum % k == 0:
            revDiv.append(k)
    
    for l in range(0,len(revDiv)): 
        addRevNum = addRevNum + revDiv[l]

    if addRevNum == m and addNum != addRevNum:
        amiNum.append(addRevNum)

    addNum = 0 #초기화
    div = [ ] #초기화
    addRevNum = 0
    revDiv = [ ]

#print(amiNum)

for h in range(0,len(amiNum)):
    amiNumSum = amiNumSum + amiNum[h]

print(amiNumSum)
print("******** %s ********" %(time.time()-start_time))

