def is_leap_year(year):
    leap_year=False
    if year%4 ==0:
        leap_year=True
    if year%100==0:
        leap_year=False
    if year%400==0:
        leap_year=True
    if leap_year:
        return f"{year} is a leap_year"
    else:
        return f"{year} is not leap_year"
        
print(is_leap_year(int(input("enter the year: "))))