import sqlite3
class Budget:
    """The Budget class is responsible for managing the budget database."""
    def __init__(self, db_path: str):
        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()
    def add_budget(self, budget_name: str):
        """The function adds a new budget to the database."""
        self.cursor.execute(
            "INSERT INTO Budget (budget_name) VALUES(?)",
            (budget_name,)
        )
        self.conn.commit()
    def show_bugets(self) -> list[tuple]:
        """The function retrieves all budgets from the database.

        :return: A list of tuples containing budget primary keys and names.
        :rtype: list[tuple]
        """        
        self.cursor.execute(
            "SELECT budget_pk,budget_name from Budget"
        )
        return self.cursor.fetchall()
    def close(self):
        """The function closes the database connection."""
        self.conn.close()
