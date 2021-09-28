import sqlite3
from sqlite3.dbapi2 import Cursor

def check_pw(usuario):
    connection = sqlite3.connect('proyect.db', check_same_thread=False)
    cursor = connection.cursor()
    cursor.execute(""" SELECT contraseña FROM users WHERE usuario='{usuario}' ORDER BY pk DESC;""".format(usuario=usuario))
    contraseña = cursor.fetchone()[0]

    connection.commit()
    cursor.close()
    connection.close()
    return contraseña

def check_users():
    connection = sqlite3.connect('proyect.db', check_same_thread=False)
    cursor = connection.cursor()
    cursor.execute(""" SELECT usuario FROM users ORDER BY pk DESC;""")
    db_users = cursor.fetchall()
    usuario = []

    for i in range(len(db_users)):
        person = db_users[i][0]
        usuario.append(person)

    connection.commit()
    cursor.close()
    connection.close()
    
    return usuario

def registro(usuario, contraseña, email):
    connection = sqlite3.connect('proyect.db', check_same_thread=False)
    cursor = connection.cursor()
    cursor.execute("""SELECT contraseña FROM users WHERE usuario='{usuario}';""".format(usuario=usuario))
    exist = cursor.fetchone()

    if exist is None:
        cursor.execute("""INSERT INTO users(usuario, contraseña, email)VALUES('{usuario}', '{contraseña}', '{email}');""".format(usuario=usuario, contraseña=contraseña, email=email))
        connection.commit()
        cursor.close()
        connection.close()


    else:
        return ('El usuario ya existe')

    return 'Registro exitoso'