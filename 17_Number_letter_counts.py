import time

start_time = time.time()


i = 0
j = 0 
k = 0
num = 0
prevNum = 0


for i in range(0,10): #100의 자리
    for j in range(0,10): #10의 자리
        for k in range(0,10): #1의 자리

            if i == 0 and (j > 0 or k > 0): #100의 자리는 0
                if j == 0: #10의 자리는 0
                    if k == 1 or k == 2 or k == 6: #1의 자리가 1,2,6일 때
                        num = num + 3
                    if k == 3 or k == 7 or k == 8:
                        num = num + 5
                    if k == 4 or k == 5 or k == 9:
                        num = num + 4
                
                if j == 1: #10의 자리가 1일 때
                    if k == 0:
                        num = num + 3
                    if k == 1 or k == 2:
                        num = num + 6
                    if k == 3 or k == 4 or k == 8 or k == 9:
                        num = num + 8
                    if k == 5 or k == 6:
                        num = num + 7
                    if k == 7:
                        num = num + 9
                
                if j == 2 or j == 3 or j == 8 or j == 9: #10의 자리가 2,3,8,9 일 때  
                    num = num + 6
                    if k == 1 or k == 2 or k == 6:
                        num = num + 3
                    if k == 3 or k == 7 or k == 8:
                        num = num + 5
                    if k == 4 or k == 5 or k == 9:
                        num = num + 4

                if j == 4 or j == 5 or j == 6:
                    num = num + 5
                    if k == 1 or k == 2 or k == 6:
                        num = num + 3
                    if k == 3 or k == 7 or k == 8:
                        num = num + 5
                    if k == 4 or k == 5 or k == 9:
                        num = num + 4

                if j == 7:
                    num = num + 7
                    if k == 1 or k == 2 or k == 6:
                        num = num + 3
                    if k == 3 or k == 7 or k == 8:
                        num = num + 5
                    if k == 4 or k == 5 or k == 9:
                        num = num + 4

            if (i == 1 or i == 2 or i == 6) and (j > 0 or k > 0):
                num = num + 3 + 7 + 3
                if j == 0:
                    if k == 1 or k == 2 or k == 6:
                        num = num + 3
                    if k == 3 or k == 7 or k == 8:
                        num = num + 5
                    if k == 4 or k == 5 or k == 9:
                        num = num + 4
                
                if j == 1:
                    if k == 0:
                        num = num + 3
                    if k == 1 or k == 2:
                        num = num + 6
                    if k == 3 or k == 4 or k == 8 or k == 9:
                        num = num + 8
                    if k == 5 or k == 6:
                        num = num + 7
                    if k == 7:
                        num = num + 9
                
                if j == 2 or j == 3 or j == 8 or j == 9:
                    num = num + 6
                    if k == 1 or k == 2 or k == 6:
                        num = num + 3
                    if k == 3 or k == 7 or k == 8:
                        num = num + 5
                    if k == 4 or k == 5 or k == 9:
                        num = num + 4

                if j == 4 or j == 5 or j == 6:
                    num = num + 5
                    if k == 1 or k == 2 or k == 6:
                        num = num + 3
                    if k == 3 or k == 7 or k == 8:
                        num = num + 5
                    if k == 4 or k == 5 or k == 9:
                        num = num + 4

                if j == 7:
                    num = num + 7
                    if k == 1 or k == 2 or k == 6:
                        num = num + 3
                    if k == 3 or k == 7 or k == 8:
                        num = num + 5
                    if k == 4 or k == 5 or k == 9:
                        num = num + 4

            if (i == 1 or i == 2 or i == 6) and (j == 0 and k == 0):
                num = num + 3 + 7


            if (i == 3 or i == 7 or i == 8) and (j > 0 or k > 0): #three/seven/eight hundred and
                num = num + 5 + 7 + 3
                if j == 0:
                    if k == 1 or k == 2 or k == 6:
                        num = num + 3
                    if k == 3 or k == 7 or k == 8:
                        num = num + 5
                    if k == 4 or k == 5 or k == 9:
                        num = num + 4
                
                if j == 1:
                    if k == 0:
                        num = num + 3
                    if k == 1 or k == 2:
                        num = num + 6
                    if k == 3 or k == 4 or k == 8 or k == 9:
                        num = num + 8
                    if k == 5 or k == 6:
                        num = num + 7
                    if k == 7:
                        num = num + 9
                
                if j == 2 or j == 3 or j == 8 or j == 9: #twenty/thirty/fourty
                    num = num + 6
                    if k == 1 or k == 2 or k == 6:
                        num = num + 3
                    if k == 3 or k == 7 or k == 8:
                        num = num + 5
                    if k == 4 or k == 5 or k == 9:
                        num = num + 4

                if j ==4 or j == 5 or j == 6:
                    num = num + 5
                    if k == 1 or k == 2 or k == 6:
                        num = num + 3
                    if k == 3 or k == 7 or k == 8:
                        num = num + 5
                    if k == 4 or k == 5 or k == 9:
                        num = num + 4

                if j == 7:
                    num = num + 7
                    if k == 1 or k == 2 or k == 6:
                        num = num + 3
                    if k == 3 or k == 7 or k == 8:
                        num = num + 5
                    if k == 4 or k == 5 or k == 9:
                        num = num + 4

            if (i == 3 or i == 7 or i == 8) and (j == 0 and k == 0):
                num = num + 5 + 7


            if (i == 4 or i == 5 or i == 9) and (j > 0 or k > 0):
                num = num + 4 + 7 + 3
                if j == 0:
                    if k == 1 or k == 2 or k == 6:
                        num = num + 3
                    if k == 3 or k == 7 or k == 8:
                        num = num + 5
                    if k == 4 or k == 5 or k == 9:
                        num = num + 4
                
                if j == 1:
                    if k == 0:
                        num = num + 3
                    if k == 1 or k == 2:
                        num = num + 6
                    if k == 3 or k == 4 or k == 8 or k == 9:
                        num = num + 8
                    if k == 5 or k == 6:
                        num = num + 7
                    if k == 7:
                        num = num + 9
                
                if j == 2 or j == 3 or j == 8 or j == 9:
                    num = num + 6
                    if k == 1 or k == 2 or k == 6:
                        num = num + 3
                    if k == 3 or k == 7 or k == 8:
                        num = num + 5
                    if k == 4 or k == 5 or k == 9:
                        num = num + 4

                if j == 4 or j == 5 or j == 6:
                    num = num + 5
                    if k == 1 or k == 2 or k == 6:
                        num = num + 3
                    if k == 3 or k == 7 or k == 8:
                        num = num + 5
                    if k == 4 or k == 5 or k == 9:
                        num = num + 4

                if j == 7:
                    num = num + 7
                    if k == 1 or k == 2 or k == 6:
                        num = num + 3
                    if k == 3 or k == 7 or k == 8:
                        num = num + 5
                    if k == 4 or k == 5 or k == 9:
                        num = num + 4

            if (i == 4 or i == 5 or i == 9) and (j == 0 and k == 0):
                num = num + 4 + 7

            #print("숫자:%d, 문자수: %d 누적문자수:%d)" %(100*i+10*j+k,num-prevNum,num))
            #print(100*i+10*j+k,num-prevNum,num)
            #prevNum = num

num = num + 11 #one thousand = 11
print("정답은: %d" % num)

print("--- %s seconds ---" % (time.time() - start_time))
