import sqlite3
from datetime import date
from dataclasses import dataclass
import bcrypt



# sql = """
# CREATE TABLE users(
#     id INTEGER PRIMARY key AUTOINCREMENT,
#     first_name TEXT not null,
#     last_name TEXT not null,
#     email TEXT not null,
#     password TEXT not null,
#     birth TEXT not null
# )
# """

# cur.execute(sql)

@dataclass
class User:
    fname:str
    lname:str
    email:str
    password:str
    birthday:str

    db = sqlite3.connect('gestion/database/users.db')

    cur = db.cursor()

    def register(self):
        sql = """
        INSERT INTO users(first_name, last_name, email, password, birth) VALUES(?, ?, ?, ?, ?)
        """
        self.cur.execute(sql, (self.fname, self.lname, self.email, bcrypt.hashpw(self.password, bcrypt.gensalt()), self.birthday))

    def login(self):
        sql = """
        SELECT * FROM USERS WHERE email = ?
        """
        self.cur.execute(sql, (self.email))
    
    def update(self):
        pass