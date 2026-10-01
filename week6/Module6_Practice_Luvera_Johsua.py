#Name: Joshua Luvera
#Date: 09/29/2026
#Assignment: Module 6 - Practice Assignment

#Get inputs from user
student_name=input("Please enter your name:")
hours_studied=float(input("Please enter how many hours you studied this week (NUMBERS ONLY):"))
assignments_completed=int(input("Please enter how many assignments you completed this week (WHOLE NUMEBRS ONLY):"))

#Prints a message based on the students progress
if hours_studied >= 10 and assignments_completed >= 3:
    study_status="On Track"

elif hours_studied >= 5:
    study_status="Making Progress"
else:
    study_status="Needs Improvement" 

#Prints the summary of their academic progress
print(f"Study Summary for {student_name}:")
print(f"Hours Studied this week: {hours_studied:.2f}")
print(f"Assignments completed this week: {assignments_completed}")
print(f"Study Status: {study_status}")