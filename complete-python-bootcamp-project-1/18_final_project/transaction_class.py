from datetime import datetime, timedelta
import sqlite3

class Transaction:
    """Base class for transactions (Income and Expense)."""
    def __init__(self, db_path: str, table_name: str):
        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()
        self.table_name = table_name

    def add(self, amount: float, date: datetime, budget_id: int, occurrence_id: int, category_id: int):
        """Add a new transaction to the database (income or expense).

        :param amount: how much money is added or removed from the budget
        :type amount: float
        :param date: date of the transaction
        :type date: datetime
        :param budget_id: foreign key of the budget
        :type budget_id: int
        :param occurrence_id: foreign key of the occurrence (one time, daily, weekly, monthly)
        :type occurrence_id: int
        :param category_id: foreign key of the category
        :type category_id: int
        """
        self.cursor.execute(
            f"INSERT INTO {self.table_name} (amount, date, budget_fk, occ_fk, category_fk) VALUES (?, ?, ?, ?, ?)",
            (amount, date, budget_id, occurrence_id, category_id)
        )
        self.conn.commit()

    def select_all(self) -> list[tuple]:
        """Select all transactions from the database.

        :return: A list of tuples containing all transactions.
        :rtype: list[tuple]
        """

        self.cursor.execute(
            f"""SELECT * FROM {self.table_name}"""
        )
        return self.cursor.fetchall()

    def select_by_id(self,revenue_id: int) -> list[tuple]:
        """Select a transaction by its primary key.

        :param revenue_id: The primary key of the transaction to be selected.
        :type revenue_id: int
        :return: A list of tuples containing the transaction details.
        :rtype: list[tuple]
        """
        self.cursor.execute(
            f"""
            SELECT * FROM {self.table_name}
            WHERE {self.table_name.lower()}_pk = ?
            """,
            (revenue_id,)
        )
        return self.cursor.fetchall()

    def get_total(self, budget_id: int, start_date: str, end_date: str) -> float:
        """Calculate the total transaction amount for a given budget within a date range.

        :param budget_id: The ID of the budget to filter transactions.
        :type budget_id: int
        :param start_date: The start date of the range in "YYYY-MM-DD" format.
        :type start_date: str
        :param end_date: The end date of the range in "YYYY-MM-DD" format.
        :type end_date: str
        :return: The total transaction amount within the specified date range.
        :rtype: float
        """
        self.cursor.execute(
            f"""
            SELECT amount, date, occ_fk 
            FROM {self.table_name}
            WHERE budget_fk = ?
            """,
            (budget_id,)
        )
        rows = self.cursor.fetchall()

        total = 0.0
        start = datetime.strptime(start_date, "%Y-%m-%d")
        end = datetime.strptime(end_date, "%Y-%m-%d")

        for amount, date_str, occurrence_id in rows:
            txn_date = datetime.strptime(date_str.strip(), "%Y-%m-%d %H:%M:%S")

            if txn_date > end:
                continue

            current_date = max(txn_date, start)

            if occurrence_id == 2:  # Daily
                while current_date <= end:
                    total += amount
                    current_date += timedelta(days=1)

            elif occurrence_id == 3:  # Weekly
                while current_date <= end:
                    total += amount
                    current_date += timedelta(weeks=1)

            elif occurrence_id == 4:  # Monthly
                while current_date <= end:
                    total += amount
                    # Increment month
                    year = current_date.year + (current_date.month // 12)
                    month = (current_date.month % 12) + 1
                    try:
                        current_date = current_date.replace(year=year, month=month)
                    except ValueError:
                        current_date = current_date.replace(day=1, year=year, month=month) + timedelta(days=30)

            else:  # One-time
                if start <= txn_date <= end:
                    total += amount

        return total

    def delete_revenue(self,revenue_id: int):
        """Deletes a selected income or expense from the database

        :param revenue_id: id of the revenue (income or expense)
        :type revenue_id: int
        """
        self.cursor.execute(
            f"""
            DELETE FROM {self.table_name}
            WHERE {self.table_name.lower()}_pk = ?
            """,
            (revenue_id,)
        )
        self.conn.commit()

    def close(self):
        """Close the database connection."""
        self.conn.close()


class Income(Transaction):
    """Class for handling income transactions."""
    def __init__(self, db_path: str):
        super().__init__(db_path, "Income")

class Expense(Transaction):
    """Class for handling expense transactions."""
    def __init__(self, db_path: str):
        super().__init__(db_path, "Expense")
