# Budget Tracker

## Overview

This is a simple budget management system that allows users to manage their income and expenses
using a command-line interface. Users can create budgets, add income and expenses, view totals for specific periods, and remove entries.

## Features

- Create new budgets or use existing ones
- Add income and expenses with categories
- View total income and expenses for specific periods
- View net budget for specific periods
- Remove income and expenses

## Requirements

- Python 3.x, nothing else in needed

## How to Run
run
```text
    python main.py
```
in the terminal (in the directory of the project). The program will prompt you to choose between creating a new budget or using an existing one. Follow the on-screen instructions to manage your budget.

## Project Structure

**main.py** # Main script to run the budget tracker
budget_class.py

**budget_class.py** # Contains the Budget class and its methods

**category_class.py** # Contains the Category class and its methods. It is used to manage the categories of income and expenses, basically the categories are food, water bill, electricity bill, salary, scholarship and anyrhing else could be added by the user.

**occurrence_class.py** # Contains the Occurrence class. The occurrence class is used to manage the occurrence of income and expenses (one-time, daily, weekly, monthly).

**transaction_class.py** # Contains the Transaction class. The transaction class is used to manage the transactions (income and expenses). It is an abstract class and is inherited by the Income and Expense classes locatated in the same file.

**utils.py** # Contains utility functions for that are used in main.py.

**budget.txt** # It is a SQlite database file that is used to store the inforamation. To see the database, you can use any SQLite viewer. Suggested: [DB Browser for SQLite](https://sqlitebrowser.org/).

## Code Documentation and Data Structure
The code is well documented with docstrings and comments. Functions and classes are named appropriately to reflect their purpose. The code is organized into separate files for better readability and maintainability. Refer to the project structure for breif description of each file.

![structure of database](images/database_structure.png)

## Sample Usage of the Budget Tracker

```text
Would you like to choose new or existing budget? Choose n or e: e



=== Available Budgets ===
No.  Budget
------------------------------
1    household1
------------------------------
Choose the number coresponding to you budget: 1

=== Budget Menu ===
1. Add Income
2. Add Expense
3. View Total Income for a Period
4. View Total Expenses for a Period
5. View Net Budget for a Period
6. Remove Income
7. Remove Expense
0. Exit
====================
Enter the option you would like to proceed with: 1
Enter amount: 100
Enter date (YYYY-MM-DD): 2025-04-0555
Invalid date format. Please use YYYY-MM-DD.
Enter date (YYYY-MM-DD): 2025-04-05  
Select occurrence type:
1 One time
2 Daily
3 Weekly
4 Monthly
Enter your choice (1-4): 1

Categories:
1. food
2. water bill
3. Electricity bill
4. Salary
5. Scholarship
6. Add new category
Choose a category number: 55
Choice out of range.

Categories:
1. food
2. water bill
3. Electricity bill
4. Salary
5. Scholarship
6. Add new category
Choose a category number: 5
New income added successfully.

=== Budget Menu ===
1. Add Income
2. Add Expense
3. View Total Income for a Period
4. View Total Expenses for a Period
5. View Net Budget for a Period
6. Remove Income
7. Remove Expense
0. Exit
====================
Enter the option you would like to proceed with: 2
Enter amount: 134.56
Enter date (YYYY-MM-DD): 32322323
Invalid date format. Please use YYYY-MM-DD.
Enter date (YYYY-MM-DD): 2024-04-25
Select occurrence type:
1 One time
2 Daily
3 Weekly
4 Monthly
Enter your choice (1-4): 323223
Please enter a number between 1 and 4.
Enter your choice (1-4): 4

Categories:
1. food
2. water bill
3. Electricity bill
4. Salary
5. Scholarship
6. Add new category
Choose a category number: 3
New expense added successfully.

=== Budget Menu ===
1. Add Income
2. Add Expense
3. View Total Income for a Period
4. View Total Expenses for a Period
5. View Net Budget for a Period
6. Remove Income
7. Remove Expense
0. Exit
====================
Enter the option you would like to proceed with: 3
Enter start date (YYYY-MM-DD): 2024-01-01
Enter end date (YYYY-MM-DD): 20244-04-01
Invalid date format. Please use YYYY-MM-DD.
Enter start date (YYYY-MM-DD): 2024-04-01  
Enter end date (YYYY-MM-DD): ew
Invalid date format. Please use YYYY-MM-DD.
Enter start date (YYYY-MM-DD): 2024-01-01
Enter end date (YYYY-MM-DD): 2024-04-01

 Total income from 2024-01-01 to 2024-04-01: 0.00

=== Budget Menu ===
1. Add Income
2. Add Expense
3. View Total Income for a Period
4. View Total Expenses for a Period
5. View Net Budget for a Period
6. Remove Income
7. Remove Expense
0. Exit
====================
Enter the option you would like to proceed with: 3
Enter start date (YYYY-MM-DD): 2025-01-01
Enter end date (YYYY-MM-DD): 2025-04-01

 Total income from 2025-01-01 to 2025-04-01: 2500.00

=== Budget Menu ===
1. Add Income
2. Add Expense
3. View Total Income for a Period
4. View Total Expenses for a Period
5. View Net Budget for a Period
6. Remove Income
7. Remove Expense
0. Exit
====================
Enter the option you would like to proceed with: 4
Enter start date (YYYY-MM-DD): 2025-02-01
Enter end date (YYYY-MM-DD): 2025-04-25

 Total expenses from 2025-02-01 to 2025-04-25: 703.68

=== Budget Menu ===
1. Add Income
2. Add Expense
3. View Total Income for a Period
4. View Total Expenses for a Period
5. View Net Budget for a Period
6. Remove Income
7. Remove Expense
0. Exit
====================
Enter the option you would like to proceed with: 5
Enter start date (YYYY-MM-DD): 2023-12-01
Enter end date (YYYY-MM-DD): 2025-04-26

 Total net budget from 2023-12-01 to 2025-04-26: 1150.72

=== Budget Menu ===
1. Add Income
2. Add Expense
3. View Total Income for a Period
4. View Total Expenses for a Period
5. View Net Budget for a Period
6. Remove Income
7. Remove Expense
0. Exit
====================
Enter the option you would like to proceed with: 6

Available Revenues to Delete:

No.   Amount     Date         Occurrence           Category
---------------------------------------------------------------------------
1     300.0      2024-12-08   Monthly              Salary
2     100.0      2025-01-01   Weekly               Scholarship
3     100.0      2025-04-05   One time             Scholarship

Enter the number of the revenue you want to delete (0 to cancel):
Number: 3
Income deleted successfully.

=== Budget Menu ===
1. Add Income
2. Add Expense
3. View Total Income for a Period
4. View Total Expenses for a Period
5. View Net Budget for a Period
6. Remove Income
7. Remove Expense
0. Exit
====================
Enter the option you would like to proceed with: 6

Available Revenues to Delete:

No.   Amount     Date         Occurrence           Category
---------------------------------------------------------------------------
1     300.0      2024-12-08   Monthly              Salary
2     100.0      2025-01-01   Weekly               Scholarship

Enter the number of the revenue you want to delete (0 to cancel):
Number: 0
Operation canceled.

=== Budget Menu ===
1. Add Income
2. Add Expense
3. View Total Income for a Period
4. View Total Expenses for a Period
5. View Net Budget for a Period
6. Remove Income
7. Remove Expense
0. Exit
====================
Enter the option you would like to proceed with: 7

Available Revenues to Delete:

No.   Amount     Date         Occurrence           Category
---------------------------------------------------------------------------
1     100.0      2025-01-01   Monthly              Electricity bill
2     134.56     2024-04-25   Monthly              Electricity bill

Enter the number of the revenue you want to delete (0 to cancel):
Number: 2
Expense deleted successfully.

=== Budget Menu ===
1. Add Income
2. Add Expense
3. View Total Income for a Period
4. View Total Expenses for a Period
5. View Net Budget for a Period
6. Remove Income
7. Remove Expense
0. Exit
====================
Enter the option you would like to proceed with: 7

Available Revenues to Delete:

No.   Amount     Date         Occurrence           Category
---------------------------------------------------------------------------
1     100.0      2025-01-01   Monthly              Electricity bill

Enter the number of the revenue you want to delete (0 to cancel):
Number: 0
Operation canceled.

=== Budget Menu ===
1. Add Income
2. Add Expense
3. View Total Income for a Period
4. View Total Expenses for a Period
5. View Net Budget for a Period
6. Remove Income
7. Remove Expense
0. Exit
====================
Enter the option you would like to proceed with: 0
See you again!
```