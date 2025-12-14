# Nested List
# Given the names and grades for each student in a class of students, store them in a nested list and 
# print the name(s) of any student(s) having the second lowest grade.

if __name__ == '__main__':
    records = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        records.append([name, score])
    
    numbers =  sorted(set(numbers for numbers, numbers in records))
   
    if True:
        second_lowest = numbers[1]
        
        #second lowest grade student name
        student_name = [name for name, student_name in records if student_name == second_lowest]
        
        student_name.sort()
        for second_lowest_grade in student_name:
            print(second_lowest_grade)
    else:
        print("Thre is no second element")


"""
Note: If there are multiple students with the second lowest grade, order their names alphabetically and print each name on a new line.

Example
The ordered list of scores is , so the second lowest score is . There are two students with that score:

. Ordered alphabetically, the names are printed as:

alpha
beta

Input Format

The first line contains an integer,
, the number of students.
The subsequent lines describe each student over

lines.
- The first line contains a student's name.
- The second line contains their grade.

Constraints

    There will always be one or more students having the second lowest grade.

Output Format

Print the name(s) of any student(s) having the second lowest grade in. If there are multiple students, order their names alphabetically and print each one on a new line.

python students = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]

The lowest grade of
belongs to Tina. The second lowest grade of belongs to both Harry and Berry, so we order their names alphabetically and print each name on a new line.

"""