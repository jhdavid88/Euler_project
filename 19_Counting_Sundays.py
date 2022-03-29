import calendar

i = 0
for y in range(1901,2001):
    for m in range(1,13):
        weekday = calendar.weekday(y,m,1)
        if weekday == 6:
            i += 1

print(i)


'''
for i in range(1900,2000):
    weekdey_1_1 = calendar.weekday(i,1,1)
    if weekdey_1_1 == 0:
        day = "Monyday"
    elif weekdey_1_1 == 1:
        day = "Tuesday"
    elif weekdey_1_1 == 2:
        day = "Wednesday"
    elif weekdey_1_1 == 3:
        day = "Thursday"
    elif weekdey_1_1 == 4:
        day = "Friday"
    elif weekdey_1_1 == 5:
        day = "Saturday"
    else:
        day = "Sunday"
    print(i,day)
'''
