# wap to print the year is leap or not 
# wap to print the year is leap or not 
class Year:

    def __init__(self):
        self.year = int(input("Enter year : "))
    
    def isleapyear(self, year):

        if year%400 == 0:
            if year%100 != 0 and year%400 == 0:
                print(f"{year} is a leap year")
        else:
            print(f"{year} is not leap year")
obj = Year()
obj.isleapyear(obj.year)
print(obj.year%400)



# wap to print the year is leap or not 
# class Year:

#     def __init__(self):
#         self.year = int(input("Enter year : "))
    
#     @staticmethod  
#     def isleapyear(year): # not need to self memory refrance 

#         if year%4 == 0:
#             print(f"{year} is a leap year")
#         else:
#             print(f"{year} is not leap year")
# obj = Year
# obj.isleapyear(obj.year)
 





