#import calendar.Calender as a
from datetime import date
#setfirstweekday=0
#cal=calendar.Calendar(firstweekday=0)
#for x in cal.iterweekdays():
#    print(x, end='')

#cal=calendar.Calendar()       used to calulate days in the year,month
#for x in cal.itermonthdays(2019,1):
 #   print(x,end=' ')


#cal=calendar.Calendar()  #used to return date,day as tuple
#for x in cal.itermonthdays2(2019,1):
#    print(x)
import calendar
import datetime

def noOfSundaysInMonth(year,month,day):
    li= calendar.Calendar().monthdayscalendar(year, month)
    count=0
    for x in li:
        z=x[day]
        if z!=0:
            count+=1
    return count

def noOfSundaysInYear(year):
    count1=0
    for month in range(1,13):
        li= calendar.Calendar().monthdayscalendar(year, month)
        count=0
        for x in li:
            z=x[day]
            if z!=0:
                count+=1
        count1+=count
    return count1


if __name__ == '__main__':
    year=int(input())
    month=int(input())
    day=int(input())
    result1=noOfSundaysInMonth(year,month,day)
    result2= noOfSundaysInYear(year)
    print(result1)
    print(result2)