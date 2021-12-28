# import datetime
# print("Current date and time: " , datetime.datetime.now())
# print("Current year: ", datetime.date.today().strftime("%Y"))
# print("Month of year: ", datetime.date.today().strftime("%B"))
# print("Week number of the year: ", datetime.date.today().strftime("%W"))
# print("Weekday of the week: ", datetime.date.today().strftime("%w"))
# print("Day of year: ", datetime.date.today().strftime("%j"))
# print("Day of the month : ", datetime.date.today().strftime("%d"))
# print("Day of week: ", datetime.date.today().strftime("%A"))

a=int(input("insert year: "))
if (a%4==0 and a%100!=0) or a%400==0:
    print("leap year")
else:
    print("not leap year")
