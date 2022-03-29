
list = [ ]
list.append(1)
list.append(2)
evenList = []
sum = 0

for i in range(1,100):

    numNext = list[i-1] + list[i]
    if numNext < 4000000:
        list.append(numNext)
    else: break
    

for j in range(0,len(list)):
    if list[j] % 2 == 0:
        evenList.append(list[j])
    
print(evenList)

for k in range(0,len(evenList)):
    sum = sum + evenList[k]

print(sum)


