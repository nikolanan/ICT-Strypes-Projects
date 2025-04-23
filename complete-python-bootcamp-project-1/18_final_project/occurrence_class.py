import sqlite3
class Occurrence:
    def __init__(self, db_path: str):
        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()
    def show_occurences(self):
        self.cursor.execute(
            "SELECT * from Occurrences"
        )
        return self.cursor.fetchall()
    def close(self):
        self.conn.close()
