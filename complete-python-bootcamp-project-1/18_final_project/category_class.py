import sqlite3
class Category():
    def __init__(self, db_path: str):
        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()
    def add_category(self, category_name: str):
        self.cursor.execute(
            "INSERT INTO Categories (category_name) VALUES (?)",
            (category_name,)
        )
        self.conn.commit()
    def show_categories(self):
        self.cursor.execute(
            "SELECT * from categories"
        )
        return self.cursor.fetchall()
    def close(self):
        self.conn.close()

