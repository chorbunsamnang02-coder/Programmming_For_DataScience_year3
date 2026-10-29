def is_leap(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

#### part B
def days_in_month(year, month):
    if month < 1 or month > 12:
        return "Invalid month"
    
    if month == 2:
        return 29 if is_leap(year) else 28
    elif month in [4, 6, 9, 11]:
        return 30
    else:
        return 31

#### part C
for year in [1900 , 200 ,2024 , 2026]:
    print(year, "->", is_leap(year))

### Part D
count_year=0
for year in range(2000 , 2100):
    if is_leap(year):
        count_year += 1

print("Number of leap years between 2000 and 2100:", count_year)
