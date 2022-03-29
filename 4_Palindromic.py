
numList = []


for i in range(100,1000):
    for j in range(100,1000):
        k = i * j
        l = str(k)
        if len(l) == 5:
            if (l[0]+l[1]+l[2]+l[3]+l[4]) == (l[4]+l[3]+l[2]+l[1]+l[0]):
                numList.append(k)

        if len(l) == 6:
            if (l[0]+l[1]+l[2]+l[3]+l[4]+l[5]) == (l[5]+l[4]+l[3]+l[2]+l[1]+l[0]):
                numList.append(k)

print("*"*100)
print(max(numList))

