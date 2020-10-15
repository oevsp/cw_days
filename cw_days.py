def isYearLeap(year):
    return (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0)
def daysInMonth(year, month):
    monthDays = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    leapMonthDays = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    for i in leapMonthDays:
        if isYearLeap(year) == True:
            return leapMonthDays[month - 1]
        elif isYearLeap(year) == False:
            return monthDays[month - 1]
        else:
            return None

def dayOfYear(year, month, day):
    days = 0
    for i in range(1, month):
        td = daysInMonth(year, i)
        days += td
    return days + day

yr = int(input("Enter the year: "))
m = int(input("Enter the month: "))
d = int(input("Enter the day: "))

print("Total number of days in year so far are: ", dayOfYear(yr, m, d))
print("Current calendar week is: ", dayOfYear(yr, m, d) // 7 + 1)