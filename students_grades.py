# You should create a script that will help this school organizing their students and their respective grades;
# Here is the list of students and their grades:

class_name = "bellsworth wiston school - second grade b"

students = ["dave braninghan", "susan goodwin",
            "adam lowel", "linda lydon", "jessie boham"]

# Below you can find lists with their grades for each trimester

dave_braninghan_grades = [10.0, 9.2, 8.5, 7.0]
susan_goodwin_grades = [7.0, 8.5, 6.0, 10.0]
adam_lowel_grades = [6.0, 6.0, 8.5, 5.0]
linda_lydon_grades = [9.5, 10.0, 10.0, 5.5]
jessie_boham_grades = [10.0, 3.5, 7.75, 9.0]

# ITERATION 1
# As you can see, the student names are not in order. Look for a Python attribute you can use to sort the students names in alphabetical order.
# Use a print once you do that just to make sure that the names were correctly ordered.
# Once that is done and verified, you can comment out the print
# Your code goes below this line

students.sort()
# print(students)
# print(students[0])

# ITERATION 2
# We currently have all the grades for each student. Calculate the average grade for each student and store the result in a variable.
# Your code goes below this line

dave_average = sum(dave_braninghan_grades) / len(dave_braninghan_grades)
susan_average = sum(susan_goodwin_grades) / len(susan_goodwin_grades)
adam_average = sum(adam_lowel_grades) / len(adam_lowel_grades)
linda_average = sum(linda_lydon_grades) / len(linda_lydon_grades)
jessie_average = sum(jessie_boham_grades) / len(jessie_boham_grades)

# ITERATION 3
# Print a message for each student saying "Hellow *Student Name*. Your final grade this year is *Avarage Grade*"
# As you can see, the student's names are not capitalized and that's just rude. Make sure when you print them, their first letters are capitalized.
# Your code goes below this line

print("Hello, " + students[0].title() + ". Your final grade this year is " + str(adam_average))
print("Hello, " + students[1].title() + ". Your final grade this year is " + str(dave_average))
print("Hello, " + students[2].title() + ". Your final grade this year is " + str(jessie_average))
print("Hello, " + students[3].title() + ". Your final grade this year is " + str(linda_average))
print("Hello, " + students[4].title() + ". Your final grade this year is " + str(susan_average))

# ITERATION 4
# Now, store all the student's avarage grades inside a new list that we will use to calculate the entire class avarage.
# TIP: you can store variables in a list.
# Once you have a list with all students avarage grades, calculate the entire class avarage.
# Your code goes below this line

class_grades = [jessie_average, adam_average, dave_average, linda_average, susan_average]
class_average = sum(class_grades) / len(class_grades)
# print("The entire class average is " + str(round(class_average, 2)))

# ITERATION 5
# Calculate how many students are in this class using a Python function and store it on a variable
# Print a message stating what was the avarage class grade and how many students were in the class.
# The message should have the class name and it should be ALL IN CAPITAL LETTERS.

student_count = len(students)
print("The " + str(student_count) + " students of class " + class_name.upper() + " average grade was " + str(round(class_average, 2)))

# BONUS ITERATION
# Now, if you are feeling courageous, we can go a step ahead and create a function with a conditional
# If the student had an average grade higher than 7, print a message that have made it to the next grade.
# If their grade is lower than 7, they have not made it and will have to go through second grade again.
# I can help you on this one! =)

def evaluateStudent(student_grade):
    if student_grade >= 7:
        return "You made it to the next grade."
    else:
        return "You will have to go through second grade again."

print(students[0].title() + ", your final grade is " + str(adam_average) + ". " + evaluateStudent(adam_average))
print(students[1].title() + ", your final grade is " + str(dave_average) + ". " + evaluateStudent(dave_average))
print(students[2].title() + ", your final grade is " + str(jessie_average) + ". " + evaluateStudent(jessie_average))
print(students[3].title() + ", your final grade is " + str(linda_average) + ". " + evaluateStudent(linda_average))
print(students[4].title() + ", your final grade is " + str(susan_average) + ". " + evaluateStudent(susan_average))