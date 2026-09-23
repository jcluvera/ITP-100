#Name: Joshua Luvera
#Date: 9/22/2026
#Assignment: Module 5: Practice Assignment

#Get inputs from user
student_name=input("Please enter your name:")
course_name=input("Please enter your course name:")
total_classes=int(input("Please enter how many class meetings have there been so far (POSITIVE WHOLE NUMBERS ONLY):"))
classes_attended=int(input("Please enter how many class meetings you have attended (POSITIVE WHOLE NUMBERS ONLY):"))

#Calculate attendance percentage
attendance_percentage = float((classes_attended/total_classes)*100)
#Calculate classes missed
classes_missed = total_classes-classes_attended

#Display Outputs
print(f"Class Attendance Summary for {student_name}")
print(f"Course: {course_name}")
print(f"Total Class Meetings: {total_classes}")
print(f"Classes Attended: {classes_attended}")
print(f"Classes Missed: {classes_missed}")
print(f"Attendance Percentage: {attendance_percentage:.2f}%")