import sqlite3
class Occurrence:
    """A class to manage occurrences (one time, daily weekly, monthly) in a SQLite database."""
    def __init__(self, db_path: str):
        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()
    def show_occurences(self) -> tuple:
        """Fetch all occurrences from the database."""
        self.cursor.execute(
            "SELECT * from Occurrences"
        )
        return self.cursor.fetchall()
    def show_occurence_by_id(self,occ_pk: int) -> str:
        """Gives the name of the rarity according to the id

        :param occ_pk: primary key of the database
        :type occ_pk: int
        :return: returs the needed rarity as a string
        :rtype: str
        """        
        self.cursor.execute(
            """Select rarity from Occurrences
            where occ_pk = ?
            """,
            (occ_pk,)
        )
        return self.cursor.fetchall()[0][0]
    def close(self):
        """Close the database connection."""
        self.conn.close()
