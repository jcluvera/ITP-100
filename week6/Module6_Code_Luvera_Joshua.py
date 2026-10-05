#Name: Joshua Luvera
#Date: 9/24/2026
#Assignment: Module 5 Personal Budjet Planner, Part 2

#Get inputs from user
income=float(input("Enter weekly income (NUMBERS ONLY, NO DOLLAR SIGNS):"))
food=float(input("Enter weekly food expenses (NUMBERS ONLY, NO DOLLAR SIGNS):"))
transportation=float(input("Enter weekly transportation expenses (NUMBERS ONLY, NO DOLLAR SIGNS):"))
entertainemnt=float(input("Enter weekly entertainemnt expenses (NUMBERS ONLY, NO DOLLAR SIGNS):"))

total_expenses=food+transportation+entertainemnt #Calculate total weekly expenses
remaining=income-total_expenses #Calculate remaining balance
income_spent_percentage=(total_expenses/income)*100 #Calculate percentage of income spent

#Analyze the percentage of income spent and set spending status accordingly
if income_spent_percentage > 80:
    spending_status="HIGH"
elif income_spent_percentage > 50:
    spending_status="MODERATE"
else:
    spending_status="LOW"

#Displays expenses, income, and remaining balance
print(f"Weekly income: ${income:.2f}")
print(f"Weekly food expenses: ${food:.2f}")
print(f"Weekly transportation expenses: ${transportation:.2f}")
print(f"Weekly entertainment expenses: ${entertainemnt:.2f}")
print(f"Total Weekly expenses: ${total_expenses:.2f}")
print(f"Remaining balance: ${remaining:.2f}")
print(f"Percentage of Income Spent: {income_spent_percentage:.2f}%")
print(f"Spending Status: {spending_status}")

if remaining < 50 or spending_status == "HIGH":
    print("WARNING: You are over budget for this month.")