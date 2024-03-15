# Question 1(b)
days_of_week = ['Saturday', 'Sunday', 'Tuesday', 'Thursday', 'Friday']

def check_day(day):
    if day == 'Friday':
        return "TOday is Holiday"
    else:
        return "Today is Working Day"
for day in days_of_week:
    print(day ,":",check_day(day))    
