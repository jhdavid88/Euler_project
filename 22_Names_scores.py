
f = open("/Users/joohyungkim/Private/3_Python/01_Test/EulerPrj/p022_names.txt", 'r')

name = f.readline() #txt파일 reading
namelist = [ ]
checklist = [ ]
list = [ ]

for i in range(0,len(name)): #각 알파벳을 namelist에 저장
    namelist.append(name[i]) 

for j in range(0,len(namelist)):
    if namelist[j] == "," or namelist[j] == '"': #알파벳이 아니면, 0으로 저장
        checklist.append(0)
    else:
        checklist.append(1) #알파벳이면, 1로 저장

for k in range(0,(len(checklist)-1)):
    if checklist[k] == 0 and checklist[k+1] == 1: #알파벳 시작 확인
        m = k + 1
    if checklist[k] == 1 and checklist[k+1] == 0: #알파벳 끝 확인
        n = k + 1
        
        list.append(name[m:n]) #알파벳만 추려서 list 에 넣음.

list.sort() #alphabetical sorting

score = 0
scorelist = [ ]

for j in range(0,len(list)): #각각 이름 별로 점수 확인
    for i in range(0,len(list[j])): #이름 내 알파벳 별로 점수
        if list[j][i] == 'A':
            score = score + 1
        elif list[j][i] == 'B':
            score = score + 2
        elif list[j][i] == 'C':
            score = score + 3
        elif list[j][i] == 'D':
            score = score + 4
        elif list[j][i] == 'E':
            score = score + 5
        elif list[j][i] == 'F':
            score = score + 6
        elif list[j][i] == 'G':
            score = score + 7
        elif list[j][i] == 'H':
            score = score + 8
        elif list[j][i] == 'I':
            score = score + 9
        elif list[j][i] == 'J':
            score = score + 10
        elif list[j][i] == 'K':
            score = score + 11
        elif list[j][i] == 'L':
            score = score + 12
        elif list[j][i] == 'M':
            score = score + 13
        elif list[j][i] == 'N':
            score = score + 14
        elif list[j][i] == 'O':
            score = score + 15
        elif list[j][i] == 'P':
            score = score + 16
        elif list[j][i] == 'Q':
            score = score + 17
        elif list[j][i] == 'R':
            score = score + 18
        elif list[j][i] == 'S':
            score = score + 19
        elif list[j][i] == 'T':
            score = score + 20
        elif list[j][i] == 'U':
            score = score + 21
        elif list[j][i] == 'V':
            score = score + 22
        elif list[j][i] == 'W':
            score = score + 23
        elif list[j][i] == 'X':
            score = score + 24
        elif list[j][i] == 'Y':
            score = score + 25
        elif list[j][i] == 'Z':
            score = score + 26

    scorelist.append(score) #각 이름 점수를 scorelist 에 저장.
    score = 0

finalscore = 0 #초기값 설정

for i in range(0,len(list)): #총점 구하기
    finalscore = finalscore + (scorelist[i] * (i+1)) #(이름점수 * 순번)의 합계 구하기

print(finalscore) #마지막 정답 도출

    

