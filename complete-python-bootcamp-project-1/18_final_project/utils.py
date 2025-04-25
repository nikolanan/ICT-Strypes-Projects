from datetime import datetime
from category_class import Category
from transaction_class import *
from occurrence_class import Occurrence

def display_budgets(bugets: list[tuple]):
    """The function displays a list of budgets with their corresponding primary keys."""
    for index,(primary_key,budget) in enumerate(bugets):
        print(index+1,budget)

def get_primary_key(all_budgets: list[tuple]) -> int:
    """The function prompts the user to select a budget from a list of budgets until a valid choice is made.

    :param all_budgets: A list of tuples containing budget information.
    :type all_budgets: list[tuple]
    :return: The primary key of the selected budget.
    :rtype: int
    """    
    while True:
        try:
            budget_name_index = int(input("Choose the number coresponding to you budget: "))
            primary_key_budget = all_budgets[budget_name_index-1][0]
            return primary_key_budget
        except IndexError:
            print("There is no such number for a budget!")
        except ValueError:
            print("Only numbers are accepted!")

def choice_made() -> int:
    """The function prompts the user to select an option from a menu until a valid choice is made.

    :return: The user's choice as an integer.
    :rtype: int
    """    
    while True:
        try:
            print("\n=== Budget Menu ===")
            print("1. Add Income")
            print("2. Add Expense")
            print("3. View Total Income for a Period")
            print("4. View Total Expenses for a Period")
            print("5. View Net Budget for a Period")
            print("====================")
            choice = int(input("Enter the option you would like to proceed with: "))
            if choice in [1,2,3,4,5]:
                return choice
            else:
                print("Not a valid choice\n")
        except ValueError:
            print("You cannot enter text! Only numbers are accepted!\n")



def get_valid_amount() -> float:
    """The function prompts the user to enter a valid amount until a valid number is provided.

    :return: The amount as a float.
    :rtype: float
    """    
    while True:
        try:
            amount = input("Enter amount: ")
            if amount.replace('.', '', 1).isdigit():
                return float(amount)
            else:
                print("Only numbers are accepted!")
        except ValueError:
            print("Invalid number.")

def get_valid_date() -> datetime:
    """The function prompts the user to enter a date in the format YYYY-MM-DD until a valid date is provided.

    :return: The date as a datetime object.
    :rtype: datetime
    """    
    while True:
        try:
            date_input = input("Enter date (YYYY-MM-DD): ")
            return datetime.strptime(date_input, "%Y-%m-%d")
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD.")

def get_occurrence_id(DB_PATH: str) -> int:
    """The function prompts the user to select an occurrence type from the database.

    :param DB_PATH: Path to the database file.
    :type DB_PATH: str
    :return: The primary key of the selected occurrence type.
    :rtype: int
    """    
    o1 = Occurrence(DB_PATH)
    all_occurences = o1.show_occurences()
    primary_keys = []
    print("Select occurrence type:")
    for index,(primary_key,category) in enumerate(all_occurences):
        print(f"{index+1}",category)
        primary_keys.append(primary_key)
    while True:
        try:
            occurrence_choice = int(input(f"Enter your choice (1-{len(primary_keys)}): "))
            if 1 <= occurrence_choice <= len(primary_keys):
                return primary_keys[occurrence_choice-1]
            else:
                print(f"Please enter a number between 1 and {len(primary_keys)}.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def get_category_id(DB_PATH: str) -> int:
    """The function prompts the user to select a category from the database or add a new one.

    :param DB_PATH: Path to the database file.
    :type DB_PATH: str
    :return: The primary key of the selected or newly added category.
    :rtype: int
    """    
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

def get_date_range() -> tuple:
    """The function prompts the user to enter a start and end date in the format YYYY-MM-DD 
    until a valid date is provided.

    :return: A tuple containing the start and end date as strings.
    :rtype: tuple
    """ 
    while True:
        try:
            start_date = input("Enter start date (YYYY-MM-DD): ")
            datetime.strptime(start_date, "%Y-%m-%d")
            end_date = input("Enter end date (YYYY-MM-DD): ")
            datetime.strptime(end_date, "%Y-%m-%d")
            return start_date, end_date
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD.")