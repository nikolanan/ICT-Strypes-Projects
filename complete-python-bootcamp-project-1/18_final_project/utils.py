from datetime import datetime
from category_class import Category
from transaction_class import *
from occurrence_class import Occurrence

def display_budgets(budgets: list[tuple]):
    """The function displays a list of budgets with their corresponding primary keys.

    :param bugets: A list of tuples containing budget information.
    :type bugets: list[tuple]
    """
    print("\n=== Available Budgets ===")
    print(f"{'No.':<5}{'Budget':<20}")
    print("-" * 30)

    for index, (primary_key, budget) in enumerate(budgets):
        print(f"{index + 1:<5}{budget:<20}")

    print("-" * 30)

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
            print("6. Remove Income")
            print("7. Remove Expense")
            print("0. Exit")
            print("====================")
            choice = int(input("Enter the option you would like to proceed with: "))
            if choice in [0,1,2,3,4,5,6,7]:
                return choice
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

def get_occurrence_id(db_path: str) -> int:
    """The function prompts the user to select an occurrence type from the database.

    :param DB_PATH: Path to the database file.
    :type DB_PATH: str
    :return: The primary key of the selected occurrence type.
    :rtype: int
    """
    o1 = Occurrence(db_path)
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

def get_category_id(db_path: str) -> int:
    """The function prompts the user to select a category from the database or add a new one.

    :param DB_PATH: Path to the database file.
    :type DB_PATH: str
    :return: The primary key of the selected or newly added category.
    :rtype: int
    """
    c1 = Category(db_path)

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

def choose_revenue_to_delete(select_result: list[tuple], db_path: str) -> int | None:
    """The function displays a list of revenues and prompts the user to select one for deletion.

    :param select_result: A list of tuples containing revenue information.
    :type select_result: list[tuple]
    :param db_path: Path to the database file.
    :type db_path: str
    :return: The primary key of the selected revenue.
    :rtype: int
    :return: If the user cancels, returns None.
    :rtype: None
    """    
    primary_keys_revenue = []
    print("\nAvailable Revenues to Delete:\n")
    print("{:<5} {:<10} {:<12} {:<20} {:<20}".format("No.", "Amount", "Date", "Occurrence", "Category"))
    print("-" * 75)

    for index, result_tuple in enumerate(select_result, start=1):
        primary_keys_revenue.append(result_tuple[0])
        amount = result_tuple[1]
        date = result_tuple[2].split(' ')[0]
        oc1 = Occurrence(db_path)
        occ_fk = result_tuple[4]
        occ_name = oc1.show_occurence_by_id(occ_fk)
        oc1.close()
        cat1 = Category(db_path)
        category_fk = result_tuple[5]
        category_name = cat1.show_categories_by_id(category_fk)
        cat1.close()

        print("{:<5} {:<10} {:<12} {:<20} {:<20}".format(index, amount, date, occ_name, category_name))

    print("\nEnter the number of the revenue you want to delete (0 to cancel):")
    while True:
        try:
            choice = int(input("Number: "))
            if choice == 0:
                print("Operation canceled.")
                return None
            elif 1 <= choice <= len(primary_keys_revenue):
                return primary_keys_revenue[choice - 1]
            else:
                print("Invalid number. Please enter one of the numbers shown above.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")