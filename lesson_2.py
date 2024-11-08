"""БД - База данных"""
"""СУБД - Система управления базой данных"""
"""CRUD - CREATE, RETRIVE, UPDATE, DELETE"""

import sqlite3

connect = sqlite3.connect("itppark.db")
cursor = connect.cursor()

cursor.execute("""
    CREATE TABLE IF BOT EXITS itpark.db(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        full_name VARCHER (30) NOT NULL,
        age INT DEFAULT NULL,
        direction TEXT,
        is_have BOOLEAN NOT NULL DEFAULT FALSE,
        rating DOUBLE (4,2) DEFAULT (0,0),
        birth_date DATE
    )
""")