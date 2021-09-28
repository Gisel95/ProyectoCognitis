import sqlite3

connection = sqlite3.connect('proyect.db', check_same_thread=False)
cursor = connection.cursor()

cursor.execute(
    """INSERT INTO users(
        usuario,
        contraseña,
        email
        )VALUES(
        'Gisel',
        'gigimor95',
        'ale_g_30@hotmail.com'
    );"""
)

cursor.execute(
    """INSERT INTO users(
        usuario,
        contrseña,
        email
        )VALUES(
        'Ana',
        '123456',
        'analopez@gmail.com'
    );"""
)

connection.commit()
cursor.close()
connection.close()