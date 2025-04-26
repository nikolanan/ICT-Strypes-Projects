from budget_class import Budget
from datetime import datetime
from transaction_class import *
import utils

DB_PATH = "budget.db"

is_new_budget = input("Would you like to choose new or existing budget? Choose n or e: ")
while is_new_budget.lower() not in ["n","e"]:
    is_new_budget = input("Choose n or e (n for new, e for existing): ")
print("\n")
budget = Budget(DB_PATH)
if is_new_budget.lower() == "n":
    budget_name = input("Type the name of the new budget: ")
    budget.add_budget(budget_name)

all_budgets = budget.show_bugets()
utils.display_budgets(all_budgets)

primary_key_budget = utils.get_primary_key(all_budgets)


while True:
    choice = utils.choice_made()
    if choice == 0:
        print("See you again!")
        break

    if choice == 1:
        i1 = Income(DB_PATH)
        amount = utils.get_valid_amount()
        date = utils.get_valid_date()
        occurrence_id = utils.get_occurrence_id(DB_PATH)
        category_id = utils.get_category_id(DB_PATH)
        i1.add(amount,date,primary_key_budget,occurrence_id,category_id)
        i1.close()
        print("New income added successfully.")
    elif choice == 2:
        e1 = Expense(DB_PATH)
        amount = utils.get_valid_amount()
        date = utils.get_valid_date()
        occurrence_id = utils.get_occurrence_id(DB_PATH)
        category_id = utils.get_category_id(DB_PATH)
        e1.add(amount, date, primary_key_budget, occurrence_id, category_id)
        print("New expense added successfully.")
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
        print(f"\n Total net budget from {start_date} to {end_date}: {total:.2f}")

    elif choice == 6:
        income_obj = Income(DB_PATH)
        primary_key_revenue = utils.choose_revenue_to_delete(income_obj.select_all(),DB_PATH)
        if primary_key_revenue is not None:
            income_obj.delete_revenue(primary_key_revenue)
            print("Income deleted successfully.")
        income_obj.close()

    elif choice == 7:
        expense_obj = Expense(DB_PATH)
        primary_key_revenue = utils.choose_revenue_to_delete(expense_obj.select_all(),DB_PATH)
        if primary_key_revenue is not None:
            expense_obj.delete_revenue(primary_key_revenue)
            print("Expense deleted successfully.")
        expense_obj.close()