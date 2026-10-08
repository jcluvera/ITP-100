#Name: Joshua Luvera
#Date: 10/8/2026
#Assignment: Module 7 Practice

#Initializes Varibles
student_name=input("Please enter your name: ")
total_hours_studied=0
day = 1

#Gets the hours studied for each of the three days, and adds them to the total hours
while day <= 3:
    hours=float(input(f"Please enter how many hours you studied on day {day}: "))
    #Checks if hours inputted is positive, if it is negative, then repeat the input for the same day
    if hours < 0: 
        print("The value of hours cannot be negative, please retry.")
        continue
    else:
        total_hours_studied += hours
        day += 1

#Calculates the average hours studied
avg_hrs_per_day = total_hours_studied/3

print(f"Summary of hours studied for {student_name} in 3 days:")
print(f"Total Hours Studied: {total_hours_studied:.2f}")
print(f"Average hours studied per day: {avg_hrs_per_day:.2f}")