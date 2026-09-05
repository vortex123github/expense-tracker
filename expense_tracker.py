expense_count = int(input("How many items do you want to buy? "))
budget = int(input("What is your budget? "))
expense_list = []
cost_list = []

def calculate_total(costs):
    return sum(costs)

def check_budget(total_cost, budget):
    if total_cost > budget:
        print(f"You have exceeded your budget by ${total_cost - budget}")
    elif total_cost < budget:
        print(f"You have ${budget - total_cost} left in your budget")
    else:
        print("You have spent your entire budget.")


for i in range(expense_count):
    expense = input("What did you spend money on? ")
    cost = int(input("How much did it cost? "))
    expense_list.append(expense)
    cost_list.append(cost)

total_cost = calculate_total(cost_list)
budget_percent = total_cost / budget * 100
remaining_percent = 100 - budget_percent
check_budget(total_cost, budget)
print(f"You have spent {budget_percent:.1f}% of your budget.")
print(f"Remaining budget: {remaining_percent:.1f}%")

for i in range (expense_count):
    print(f"{expense_list[i]}: ${cost_list[i]}")
largest_cost = max(cost_list)
largest_index = cost_list.index(largest_cost)
print(f"Biggest expense: {expense_list[largest_index]}: ${largest_cost}")
print("--------------------------------")
print(f"Total spent: ${total_cost}")





    
