#Name: Joshua Luvera
#Date: 10/11/2026
#Assignment: Module 6 Personal Budjet Planner, Part 2

#Get inputs from user
income=float(input("Enter weekly income (NUMBERS ONLY, NO DOLLAR SIGNS):"))
#food=float(input("Enter weekly food expenses (NUMBERS ONLY, NO DOLLAR SIGNS):"))
#transportation=float(input("Enter weekly transportation expenses (NUMBERS ONLY, NO DOLLAR SIGNS):"))
#entertainemnt=float(input("Enter weekly entertainemnt expenses (NUMBERS ONLY, NO DOLLAR SIGNS):"))
#total_expenses=food+transportation+entertainemnt #Calculate total weekly expenses

#initialize variables
total_expenses = 0
day = 1

#starts a loop that asks the user for their expenses for each of the seven days of the week and adds it to the total expenses
while day <= 7:
    daily_expenses=float(input(f"Please enter how much money you spent on day {day} (NUMBERS ONLY NO DOLLAR SIGNS):"))

    #Detects if the given input is negative, if it is, then retry the previous step, if not then it continues to the next day
    if daily_expenses < 0:
        print("The value of money cannot be negative, please try again.")
        continue
    else:
        total_expenses += daily_expenses
        day += 1

average_daily_expenses = total_expenses/7 #calculates the average daily expenses
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
#print(f"Weekly food expenses: ${food:.2f}")
#print(f"Weekly transportation expenses: ${transportation:.2f}")
#print(f"Weekly entertainment expenses: ${entertainemnt:.2f}")
print(f"Total Weekly expenses: ${total_expenses:.2f}")
print(f"Average daily expenses: ${average_daily_expenses:.2f}")
print(f"Remaining balance: ${remaining:.2f}")
print(f"Percentage of Income Spent: {income_spent_percentage:.2f}%")
print(f"Spending Status: {spending_status}")

if remaining < 50 or spending_status == "HIGH":
    print("WARNING: You are over budget for this month.")