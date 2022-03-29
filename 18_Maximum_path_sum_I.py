import time

start_time = time.time()

line1 = [75] 
line2 = [95,64]
line3 = [17,47,82]
line4 = [18,35,87,10]
line5 = [20,4,82,47,65]
line6 = [19,1,23,75,3,34]
line7 = [88,2,77,73,7,63,67]
line8 = [99,65,4,28,6,16,70,92]
line9 = [41,41,26,56,83,40,80,70,33]
line10 = [41,48,72,33,47,32,37,16,94,29]
line11 = [53,71,44,65,25,43,91,52,97,51,14]
line12 = [70,11,33,28,77,73,17,78,39,68,17,57]
line13 = [91,71,52,38,17,14,91,43,58,50,27,29,48]
line14 = [63,66,4,68,89,53,67,30,73,16,69,87,40,31]
line15 = [4,62,98,27,23,9,70,98,73,93,38,53,60,4,23]

numlist = [ ]
caselist = [ ]

for a in range(0,1):
    for b in range(a,a+2):
        for c in range(b,b+2):
            for d in range(c,c+2):
                for e in range(d,d+2):
                    for f in range(e,e+2):
                        for g in range(f,f+2):
                            for h in range(g,g+2):
                                for i in range(h,h+2):
                                    for j in range(i,i+2):
                                        for k in range(j,j+2):
                                            for l in range(k,k+2):
                                                for m in range(l,l+2):
                                                    for n in range(m,m+2):
                                                        for o in range(n,n+2):
                                                            number = line1[a]+line2[b]+line3[c]+line4[d]+line5[e]+line6[f]+line7[g]+line8[h]+line9[i]+line10[j]+line11[k]+line12[l]+line13[m]+line14[n]+line15[o]
                                                            numlist.append(number)
                                                            caselist.append([a,b,c,d,e,f,g,h,i,j,k,l,m,n,o])

print("*"*100)
print("최대값은: %d" %max(numlist))
#print(numlist.index(max(numlist)))
maxCase = caselist[numlist.index(max(numlist))]
#print(maxCase)
print("더하기 조합은: %d+%d+%d+%d+%d+%d+%d+%d+%d+%d+%d+%d+%d+%d+%d" %(line1[maxCase[0]], line2[maxCase[1]], line3[maxCase[2]], line4[maxCase[3]], line5[maxCase[4]], line6[maxCase[5]], line7[maxCase[6]], line8[maxCase[7]], line9[maxCase[8]], line10[maxCase[9]], line11[maxCase[10]], line12[maxCase[11]], line13[maxCase[12]], line14[maxCase[13]], line15[maxCase[14]]))
print("*"*100)
print("--- %s seconds ---" % (time.time() - start_time))

