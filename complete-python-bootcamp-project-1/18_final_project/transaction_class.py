from datetime import datetime, timedelta
import sqlite3

class Transaction:
    def __init__(self, db_path: str, table_name: str):
        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()
        self.table_name = table_name

    def add(self, amount: float, date: datetime, budget_id: int, occurrence_id: int, category_id: int):
        self.cursor.execute(
            f"INSERT INTO {self.table_name} (amount, date, budget_id, occurrence_id, category_id) VALUES (?, ?, ?, ?, ?)",
            (amount, date, budget_id, occurrence_id, category_id)
        )
        self.conn.commit()

    def get_total(self, budget_id: int, start_date: str, end_date: str) -> float:
        self.cursor.execute(
            f"""
            SELECT amount, date, occurrence_id 
            FROM {self.table_name}
            WHERE budget_id = ?
            """,
            (budget_id,)
        )
        rows = self.cursor.fetchall()

        total = 0.0
        start = datetime.strptime(start_date, "%Y-%m-%d")
        end = datetime.strptime(end_date, "%Y-%m-%d")

        for amount, date_str, occurrence_id in rows:
            txn_date = datetime.strptime(date_str, "%Y-%m-%d")

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

    def close(self):
        self.conn.close()


class Income(Transaction):
    def __init__(self, db_path: str):
        super().__init__(db_path, "Income")

class Expense(Transaction):
    def __init__(self, db_path: str):
        super().__init__(db_path, "Expense")
