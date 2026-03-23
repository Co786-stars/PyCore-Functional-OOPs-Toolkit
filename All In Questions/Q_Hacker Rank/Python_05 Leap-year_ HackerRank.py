'''
def is_leap(year):
    leap = False  # means not leap year

    # Write your logic here
    if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
        leap = True  # means leap year

    return leap


year = int(input())
print(is_leap(year))
'''

# Task/Questions : -
# An extra day is added to the calendar almost every four years as February 29, and the day is called a leap day.
# It corrects the calendar for the fact that our planet takes approximately 365.25 days to orbit the sun.
# A leap year contains a leap day.
#
# In the Gregorian calendar, three conditions are used to identify leap years:
#
# The year can be evenly divided by 4, is a leap year, unless:
# The year can be evenly divided by 100, it is NOT a leap year, unless:
# The year is also evenly divisible by 400. Then it is a leap year.

# This means that in the Gregorian calendar, the years 2000 and 2400 are leap years,
# while 1800, 1900, 2100, 2200, 2300 and 2500 are NOT leap years. Source

# Given a year, determine whether it is a leap year.
# If it is a leap year, return the Boolean True, otherwise return False.
"""
Explain leap year : -

"""
class Year:
    def __init__(self, year):
        self.year = year

    def actions(self):
        if (self.year % 400 == 0) or (self.year % 4 == 0 and self.year % 100 != 0):
            self.leapYear = True
        else:
            self.leapYear = False
        return self.leapYear

class LeapYear(Year):
    def __init__(self, user):
        super().__init__(year=user)

    def display(self):
        # Call actions() here
        self.actions()
        if self.leapYear:
            return f"{self.year} is a leap year"
        else:
            return f"{self.year} is NOT a leap year"

try:
    user_input = int(input("Enter the year : "))
    obj = LeapYear(user=user_input)
    print(obj.display())
except ValueError:
    print("Pls enter the valid number")

