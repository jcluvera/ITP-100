#Name: Joshua Luvera
#Date: 9/18/2026
#Assignment: Module 4 Practice Assignment

#Initializing variables
student_name=""
textbook_cost=0.0
notebook_cost=0.0
flash_cost=0.0
NUMBER_OF_ITEMS=3

total_cost=0.0
average_cost=0.0 # HAVE TO ROUND TO 2 DECIMAL PLACES

student_name=input("Enter Student name:") #Get student name
textbook_cost=float(input("Enter textbook cost (NUMBER ONLY, NO DOLLAR SIGNS):")) #Get textbook cost
notebook_cost=float(input("Enter notebook cost (NUMBER ONLY, NO DOLLAR SIGNS):")) #Get notebook cost
flash_cost=float(input("Enter flash drive cost (NUMBER ONLY, NO DOLLAR SIGNS):")) #Get flashdrive cost

total_cost=textbook_cost+notebook_cost+flash_cost #Calculate total cost
average_cost=total_cost/NUMBER_OF_ITEMS #Calculate average cost


print(f"Summary of items for {student_name}:")
print(f"Textbook Cost: ${total_cost:.2f}")
print(f"Notebook Cost: ${notebook_cost:.2f}")
print(f"Flash Drive Cost: ${flash_cost:.2f}")
print(f"Total Cost: ${total_cost:.2f}")
print(f"Average Cost: ${average_cost:.2f}") #Print out average cost, rounded to two decimal places