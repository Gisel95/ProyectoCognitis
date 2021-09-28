import sqlite3

connection = sqlite3.connect('proyect.db', check_same_thread = False)
cursor = connection.cursor()

cursor.execute(
   """CREATE TABLE users(
       pk INTEGER PRIMARY KEY AUTOINCREMENT,
       usuario VARCHAR(16),
       contraseña VARCHAR(32),
       email VARCHAR(32) 
   ); """
)

connection.commit()
cursor.close()
connection.close()