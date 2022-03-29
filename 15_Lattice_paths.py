rowTot = 20
columeTot = 20
prevRow = [ ]
nextRow = [ ]

for i in range(0,rowTot+1):
    prevRow.append(1)

for k in range(1,columeTot+1):

    nextRow.append(1) #첫번째 intial row 정의

    for j in range(1,rowTot+1):
        nextRow.append(prevRow[j]+nextRow[j-1])

    if k == columeTot and j == rowTot: #grid 반복 후에는 출력
        print(nextRow[20])
    
    else: #아직 끝나지 않았으면 계속 반복
        prevRow = nextRow
        nextRow = [ ]




