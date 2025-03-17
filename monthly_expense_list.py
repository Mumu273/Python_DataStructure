monthly_expense = [2200, 2350, 2600, 2130, 2190]

extra = monthly_expense[1] - monthly_expense[0]

print(f"In February, I spent extra {extra} dollars compared to january.")
total = monthly_expense[0] + monthly_expense[1] + monthly_expense[2]

print(f"total expense is {total} in first quarter (first three months) of the year")

for exp in monthly_expense:
    if exp == 2000:
        print("Yes")

monthly_expense.append(1980)

monthly_expense[3] = monthly_expense[3] - 200

print(monthly_expense)
