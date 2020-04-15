import sqlite3

class Database:
    
    def __init__(self, db):
        self.con = sqlite3.connect(db)
        self.cur = self.con.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS books (ID INTEGER PRIMARY KEY, TITLE TEXT, AUTHOR TEXT, YEAR INTEGER, ISBN INTEGER)")
        self.con.commit()
        
    def insert(self, title, author, year, isbn):
        self.cur.execute("INSERT INTO BOOKS VALUES (NULL,?,?,?,?)",(title, author, year, isbn))
        self.con.commit()
    
    def view(self):
        self.cur.execute("SELECT * FROM BOOKS")
        rows = self.cur.fetchall()
        return rows
    
    def search(self, title="", author="", year="", isbn=""):
        self.cur.execute("SELECT * FROM BOOKS WHERE TITLE=? OR AUTHOR=? OR YEAR=? OR ISBN=?", (title, author, year, isbn))
        rows = self.cur.fetchall()
        return rows
    
    def delete(self, id):
        self.cur.execute("DELETE FROM BOOKS WHERE ID=?", (id,))
        self.con.commit()
    
    def update(self, id, title, author, year, isbn):
        self.cur.execute("UPDATE BOOKS SET TITLE=?, AUTHOR=?, YEAR=?, ISBN=? WHERE ID=?", (title, author, year, isbn, id))
        self.con.commit()

    def __del__(self):
        self.con.close()