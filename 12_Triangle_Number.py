
array = [ ]
i = 12374
while len(array) < 500:
    number = int(i*(i+1)/2)
    for j in range(1,number+1):
        if number % j == 0:
            array.append(j)
            if number == j:
                if len(array) >= 500:
                    print(i,number,len(array))
                    #print(array[len(array)-1])
                    continue
                    
                else:
                    print(i,number,len(array))
                    array = [ ]
    
    i = i + 1
    if i > 100000:
        break


                    

'''
num_array = [ ]
number = 0
divisor_array = [ ]
divisor = []

for i in range (1,20):
    number = number + i 
    divisor_array.append(number)
    
print(divisor_array)

for j in range(0,len(divisor_array)):
    for k in range(1,1000):
        if divisor_array[j] >= k:
            if divisor_array[j] % k == 0:
                divisor.append(k)
                print(divisor_array[j],k,divisor)
                if divisor_array[j] == k:
                    if len(divisor) >= 6:
                        print(divisor[len(divisor)-1])
                        print("*"*100)
                    
        else:
            divisor = [ ]
    
'''
        
 
      
    