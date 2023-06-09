import calendar

class Date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

def printCalendar(date):
    month = date.month
    year = date.year

    # create a calendar object
    cal = calendar.Calendar()

    first_day, number_of_days = calendar.monthrange(year, month)

    print()
    print(calendar.month_name[month], year)
    print()

    print("Mo Tu We Th Fr Sa Su")

    for i in range(first_day):
        print("   ", end="")

    for day in range(1, number_of_days + 1):
        print(f"{day:2}", end=" ")
        first_day += 1

        if first_day == 7:
            first_day = 0
            print()

    if first_day > 0:
        print()

# Example use case:
for i in range(1, 13):
    date = Date(1, i, 2023)
    printCalendar(date)
    
