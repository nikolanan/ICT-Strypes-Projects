from budget_class import Budget
from datetime import datetime
from transaction_class import *
import utils

DB_PATH = "budget.db"

is_new_budget = input("Would you like to choose new or existing budget? Choose n or e: ")
while is_new_budget.lower() not in ["n","e"]:
    is_new_budget = input("Choose n or e (n for new, e for existing): ")

budget = Budget(DB_PATH)
if is_new_budget.lower() == "n":
    budget_name = input("Type the name of the new budget: ")
    budget.add_budget(budget_name)

all_budgets = budget.show_bugets()
utils.display_budgets(all_budgets)
budget_name_index = int(input("Choose the number coresponding to you budget: "))
primary_key_budget = all_budgets[budget_name_index-1][0]
print('\n')
    ##gives the int from the data displayed


choice = utils.choice_made()
print(choice)
if choice == 1:
    i1 = Income(DB_PATH)
    amount = utils.get_valid_amount()
    date = utils.get_valid_date()
    occurrence_id = utils.get_occurrence_id()
    category_id = utils.get_category_id(DB_PATH)
    i1.add(amount,date,primary_key_budget,occurrence_id,category_id)
    i1.close()
elif choice == 2:
    e1 = Expense(DB_PATH)
    amount = utils.get_valid_amount()
    date = utils.get_valid_date()
    occurrence_id = utils.get_occurrence_id()
    category_id = utils.get_category_id(DB_PATH)
    e1.add(amount, date, primary_key_budget, occurrence_id, category_id)
    print("Expense added successfully.")
    e1.close()
elif choice == 3:
    income_obj = Income(DB_PATH)
    start_date, end_date = utils.get_date_range()
    total = income_obj.get_total(primary_key_budget, start_date, end_date)
    print(f"\n Total income from {start_date} to {end_date}: {total:.2f}")
    income_obj.close()

elif choice == 4:
    expense_obj = Expense(DB_PATH)
    start_date, end_date = utils.get_date_range()
    total = expense_obj.get_total(primary_key_budget, start_date, end_date)
    print(f"\n Total expenses from {start_date} to {end_date}: {total:.2f}")
    expense_obj.close()
    
elif choice == 5:
    income_obj = Income(DB_PATH)
    expense_obj = Expense(DB_PATH)
    start_date, end_date = utils.get_date_range()
    total = income_obj.get_total(primary_key_budget,start_date,end_date) - expense_obj.get_total(primary_key_budget,start_date,end_date)
    income_obj.close()
    expense_obj.close()
    print(f"\n Total expenses from {start_date} to {end_date}: {total:.2f}")





###
#what would you like to do.
###1 Add income (category)
###2 Add expense (category)
###3 Calculate income for a period of time
###4 Calculate expenses for a period of time
###5 Calculate budget for a period of time
