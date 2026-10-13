# Name: Joshua Luvera
# Date: 10/13/2026
# Assignment: Module 8 Practice Assignment

#Calculates the GPA for the student
def calc_gpa(grade_points, courses):
    gpa = grade_points / courses
    return gpa

#Determines what the academic standing is based on the GPA
def determine_academic_standing(gpa):
    if gpa >= 3.0:
        return "Good Academic Standing"
    else:
        return "Needs Attendtion"

#Prints a summary for the student
def print_summary(name,courses,grade_points,gpa,standing):
    print(f"Academic Summary for {name}:")
    print(f"Completed Courses: {courses}")
    print(f"Total Grade Points: {grade_points:.2f}")
    print(f"GPA: {gpa:.2f}")
    print(f"Academic Standing: {standing}")

def main():
    #Gets required inputs
    student_name = input("Please enter your name:")
    completed_courses = int(input("Please enter the the amount of completed courses:"))
    grade_points_earned = float(input("Please enter how many grade points you achived:"))

    gpa = calc_gpa(grade_points_earned, completed_courses)
    academic_standing = determine_academic_standing(gpa)

    print_summary(student_name,completed_courses,grade_points_earned,gpa,academic_standing)

main()