import sqlite3
class Budget:
    def __init__(self, db_path: str):
        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()
    def add_budget(self, budget_name: str):
        self.cursor.execute(
            "INSERT INTO Budget (budget_name) VALUES(?)",
            (budget_name,)
        )
        self.conn.commit()
    def show_bugets(self):
        self.cursor.execute(
            "SELECT budget_pk,budget_name from Budget"
        )
        return self.cursor.fetchall()
    def close(self):
        self.conn.close()
