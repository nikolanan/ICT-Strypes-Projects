from datetime import datetime
from category_class import Category
from transaction_class import *

def display_budgets(bugets: list[tuple]):
    for index,(primary_key,budget) in enumerate(bugets):
        print(index+1,budget)

def choice_made() -> int:
    while True:
        try:
            print("1 Add income"
                    "\n2 Add expense"
                    "\n3 Calculate income for a period of time"
                    "\n4 Calculate expenses for a period of time"
                    "\n5 Calculate budget for a period of time")
            choice = int(input("Enter the option you would like to proceed with: "))
            if choice in [1,2,3,4,5]:
                return choice
        except ValueError:
            print("You cannot enter text! Only numbers are accepted! ")



def get_valid_amount():
    while True:
        try:
            amount = input("Enter amount: ")
            if amount.replace('.', '', 1).isdigit():
                return float(amount)
            else:
                print("Only numbers are accepted!")
        except ValueError:
            print("Invalid number.")

def get_valid_date():
    while True:
        try:
            date_input = input("Enter date (YYYY-MM-DD): ")
            return datetime.strptime(date_input, "%Y-%m-%d")
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD.")

def get_occurrence_id():
    while True:
        print("Select occurrence type:")
        print("1. Daily")
        print("2. Weekly")
        print("3. Monthly")
        try:
            occurrence_choice = int(input("Enter your choice (1-3): "))
            if occurrence_choice in [1, 2, 3]:
                return occurrence_choice  # Assuming 1 = Daily, 2 = Weekly, 3 = Monthly
            else:
                print("Please enter a number between 1 and 3.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def get_category_id(DB_PATH):
    c1 = Category(DB_PATH)
    
    while True:
        all_categories = c1.show_categories()
        primary_keys = []

        print("\nCategories:")
        for index, (primary_key, category) in enumerate(all_categories):
            print(f"{index + 1}. {category}")
            primary_keys.append(primary_key)

        print(f"{len(primary_keys) + 1}. Add new category")

        try:
            choice = int(input("Choose a category number: "))
            
            if 1 <= choice <= len(primary_keys):
                return primary_keys[choice - 1]

            elif choice == len(primary_keys) + 1:
                new_cat = input("Enter name for new category: ").strip()
                if new_cat:
                    existing_names = [cat[1].lower() for cat in all_categories]
                    if new_cat.lower() not in existing_names:
                        c1.add_category(new_cat)
                        print(f"Category '{new_cat}' added successfully.")
                    else:
                        print("Category already exists.")
                else:
                    print("Category name cannot be empty.")
            else:
                print("Choice out of range.")

        except ValueError:
            print("Only numbers are accepted.")

def get_date_range():
    while True:
        try:
            start_date = input("Enter start date (YYYY-MM-DD): ")
            datetime.strptime(start_date, "%Y-%m-%d")
            end_date = input("Enter end date (YYYY-MM-DD): ")
            datetime.strptime(end_date, "%Y-%m-%d")
            return start_date, end_date
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD.")