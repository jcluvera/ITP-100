#Name: Joshua Luvera
#Date: 9/20/2026
#Assignment: Module 4 Personal Budjet Planner, Part 1

#Get inputs from user
income=float(input("Enter weekly income (NUMBERS ONLY, NO DOLLAR SIGNS):"))
food=float(input("Enter weekly food expenses (NUMBERS ONLY, NO DOLLAR SIGNS):"))
transportation=float(input("Enter weekly transportation expenses (NUMBERS ONLY, NO DOLLAR SIGNS):"))
entertainemnt=float(input("Enter weekly entertainemnt expenses (NUMBERS ONLY, NO DOLLAR SIGNS):"))

total_expesnes=food+transportation+entertainemnt #Calculate total weekly expenses
remaining=income-total_expesnes #Calculate remaining balance

#Displays expenses, income, and remaining balance
print(f"Weekly income: ${income:.2f}")
print(f"Weekly food expenses: ${food:.2f}")
print(f"Weekly transportation expenses: ${transportation:.2f}")
print(f"Weekly entertainment expenses: ${entertainemnt:.2f}")
print(f"Total Weekly expenses: ${total_expesnes:.2f}")
print(f"Remaining balance: ${remaining:.2f}")