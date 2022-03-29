numberOfTrial = [ ]

for n in range(1,1000000):
    trial = 1
    while n != 1:
        if n % 2 == 0:
            n = n/2
            trial += 1

        else:
            n = 3*n+1
            trial += 1

    #print(trial)
    numberOfTrial.append(trial)

print((numberOfTrial.index(max(numberOfTrial))+1))





