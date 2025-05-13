import sqlite3
class Category():
    """The class is used to manage categories of trasactions in the database."""
    def __init__(self, db_path: str):
        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()
    def add_category(self, category_name: str):
        """The function adds a new category to the database.

        :param category_name: The name of the category to be added.
        :type category_name: str
        """
        self.cursor.execute(
            "INSERT INTO Categories (category_name) VALUES (?)",
            (category_name,)
        )
        self.conn.commit()
    def show_categories(self) -> list[tuple]:
        """The function retrieves all categories from the database.

        :return: A list of tuples containing all categories.
        :rtype: list[tuple]
        """
        self.cursor.execute(
            "SELECT * FROM categories"
        )
        return self.cursor.fetchall()

    def show_categories_by_id(self,cat_id: int) -> str:
        """The function retrieves a category name by its primary key.

        :param cat_id: The primary key of the category to be retrieved.
        :type cat_id: int
        :return: The name of the category.
        :rtype: str
        """        
        self.cursor.execute(
            """
            SELECT category_name FROM Categories
            WHERE category_pk = ?
            """,
            (cat_id,)
        )
        return self.cursor.fetchall()[0][0]
    def close(self):
        """The function closes the database connection."""
        self.conn.close()