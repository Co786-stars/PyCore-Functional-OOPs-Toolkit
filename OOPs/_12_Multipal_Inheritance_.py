"""
In this module we are Discuss __________________What is multipal Inheritance_______________How we use it____________
"""

# What is multipal Inheritance ?
# Multiple inheritance is an object-oriented programming (OOP) concept in which a class can inherit attributes and methods
# from more than one parent class, enabling the child class to combine functionalities from multiple sources.

# In simple way : -
# Multiple inheritance means a class can have more than one parent, so it gets the features of all those parents.


# visualization of Example of Multipal Inheritance : -
# Parent Class 1     Parent Class 2
#      |                   |
#      +------+   +--------+
#             |   |
#          Child Class
#       (Inherits from both)



# ➡➡➡➡  Multipal Inheritance ➡➡➡➡➡➡➡
#➡ ➡ ➡ ➡ ➡ ➡ ➡ ➡ ➡ ➡ ➡ ➡ ➡ ➡ ➡ ➡ ➡ ➡ ➡
class MyParents:   # parents1st
    def fun1(self):
        self.msg1 = "My Parents"
        return f"{self.msg1}"

class UrParents:   # parents2nd
    def fun2(self):
        self.msg2 = "Ur Parents"
        return f"{self.msg2}"

class Family(MyParents, UrParents):  # child class
    def __init__(self):
        """constructor initialize the attribute"""
        pass

Myfamily = Family()  #  we are access the first and second function via child class
print(f"{Myfamily.fun1()} and {Myfamily.fun2()} like a family")

#➡ ➡ ➡ ➡ ➡ ➡ ➡ ➡ ➡ ➡ ➡ ➡ ➡ ➡ ➡ ➡ ➡ ➡ ➡




# CODES/SYNTAX : -
class Parents1st:
    def __init__(self):
        """init initialize the attribute"""
        self.var1 = "1st value"

class Parents2nd:
    def __init__(self):
        self.var2 = "2nd value"

class Child(Parents1st, Parents2nd):
    def __init__(self):
        Parents1st.__init__(self)
        Parents2nd.__init__(self)

obj = Child()
print(obj.var1, obj.var2)  # output is display






# CODE/SYNTAX : -
class ProgrammerClass:
    """this is first parents class"""
    def __init__(self, coder_name, language):
        """constructor initialize the attribute"""
        self.name = coder_name
        self.programming_language = language

    def code(self):
        """try to display the name of coder"""
        return f"{self.name} is coding in {self.programming_language}"

    def get_language(self):
        """try to display name of programming language"""
        return f"language : {self.programming_language}"


class ManagerClass:
    """try to display the team management"""
    def __init__(self, manager_name, size):
        """constructor initialize the attribute"""
        self.name = manager_name
        self.team_size = size

    def manage(self):
        """try to print the manager name"""
        return f"{self.name} is managing {self.team_size} people"

    def get_team_size(self):
        """try to display the size to a team"""
        return f"Team size {self.team_size}"


class TeachLead(ProgrammerClass, ManagerClass):
    """try to display the inheritance"""
    def __init__(self,  m_name, l_name, t_size, project):
        ProgrammerClass.__init__(self, coder_name=m_name, language=l_name)   # calling the Parent_1st
        ManagerClass.__init__(self, manager_name=m_name, size=t_size)    # calling the Parent_2nd
        self.project_name = project

    def lead_project(self):
        """access the value of name using child class"""
        return f"{self.name} is leading {self.project_name}"

    def manage_project(self):
        """displaying child inherit both parents property"""
        return f"{super().code()}\n{super().manage()}" # calling child class from property
try:
    name = str(input("Enter the coder name : "))
    programming_language = str(input("Enter programming language : "))
    team_size = int(input("Enter the team size : "))
    my_project = input("Enter name of project : ")
    if __name__ == '__main__':
        p1 = ProgrammerClass("Wizard", "Python") # creating object of Parent1 class
        p2 = ManagerClass("Wizard", 10)  # creating object of  Parent2 class
        p3 = TeachLead(m_name=name , l_name=programming_language, t_size=team_size,  project=my_project) # obj of child class


        # straight forward example calling both parents properties class from child
        var1 = p3.lead_project() # assigning the function output to var1
        var2 = p3.manage_project() # assign the function output to var2
        print(var1)
        print(var2)

except ValueError as v:
    print(f"Pls enter valid output above are wrong {v}")
