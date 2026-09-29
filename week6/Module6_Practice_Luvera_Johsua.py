#Name: Joshua Luvera
#Date: 09/29/2026
#Assignment: Module 6 - Practice Assignment

#Get inputs from user
student_name=input("Please enter your name:")
hours_studied=float(input("Please enter how many hours you studied this week (NUMBERS ONLY):"))
assignments_completed=float(input("Please enter how many assignments you completed this week (NUMEBRS ONLY):"))

#Prints summary of inputs
print(f"Student Name: {student_name}")
print(f"Hours Studied this week: {hours_studied:.1f}")
print(f"Assignments completed this week: {assignments_completed:.0f}")

#Prints a message based on the students progress
if hours_studied >= 10 and assignments_completed >= 3:
    print("Congratuations! You are on track!")

elif hours_studied >= 5:
    print("You are making progress, keep up the good work!")

else:
    print("Looks like your work needs some improvement.")
