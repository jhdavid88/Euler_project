deficient = [ ]
abundant = [ ]
perfect = [ ]

for number in range(1,28123):

    divisor = [ ]
    for i in range(1,number-1):
        if number % i == 0:
            divisor.append(i)

    #print(divisor)

    check_number = 0
    for j in range(0,len(divisor)):
        check_number = check_number + divisor[j]

    #print(check_number)
    if number > check_number:
        #print("Deficient")
        deficient.append(number)
    elif number < check_number:
        #print("Abundant")
        abundant.append(number)
    elif number == check_number:
        #print("Perfect")
        perfect.append(number)

#print("Deficient list\n" + str(deficient))
#print("Abundant list\n" + str(abundant))
#print("Perfect list\n" + str(perfect))

two_abundant = [ ]
for i in abundant:
    for j in abundant:
        comb = i + j
        if comb <= 28123:
             two_abundant.append(comb)

#print(two_abundant)
set(two_abundant)

all_integer = [ ]
for i in range(1,28124):
    all_integer.append(i)

set(all_integer)
non_abundant = set(all_integer) - set(two_abundant)
list_non_abundant = list(non_abundant)

answer = 0 
for i in range(0,len(non_abundant)):
    answer = answer + list_non_abundant[i]

print(answer)