import sqlite3 as sql
import smtplib

def mail(username):
    email="garvkumar059@gmail.com"
    rec="garvkumar68@gmail.com"
    #rec="garvkumar68@gmail.com"
        
    subject="alert"
    msg="someone trying to get unauth access in account: "+username
    txt=f"subject:{subject}\n\n{msg}"
    server=smtplib.SMTP("smtp.gmail.com",587)
    server.starttls()
    server.login(email,"ummfddsecaqclwcp")
    server.sendmail(email,rec,txt)
    print("done")

def create_db():
    try:
        conn = sql.connect('database.db')
        conn.execute('CREATE TABLE IF NOT EXISTS tb_usuario (id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT UNIQUE NOT NULL, password TEXT NOT NULL)')
        print("INFO - DATABASE - Table created successfully")
        conn.close()
    except Exception as e:
        print("ERROR - DATABASE - Connection could not be established:", e)

def drop_db():
    try:
        conn = sql.connect('database.db')
        conn.execute('DROP TABLE IF EXISTS tb_usuario')
        print("INFO - DATABASE - Table deleted successfully!")
        conn.close()
    except Exception as e:
        print("ERROR - DATABASE - Connection denied or database does not exist:", e)

def add_user_and_passw(username, password):
    try:
        with sql.connect("database.db") as con:
            cur = con.cursor()
            cur.execute("SELECT * FROM tb_usuario WHERE username=?", (username,))
            rows = cur.fetchall()
            if rows:
                print("Username already exists!")
                return 0, False
            else:
                cur.execute("INSERT INTO tb_usuario (username, password) VALUES (?, ?)", (username, password))
                id = cur.lastrowid
                print("User created, ID:", id)
                return id, True
    except Exception as e:
        print("Error in registration:", e)

def check_user_and_passw(username, password):
    try:
        with sql.connect("database.db") as con:
            cur = con.cursor()
            cur.execute("SELECT * FROM tb_usuario WHERE username=?", (username,))
            row = cur.fetchone()
            if row:
                user_id, usuario, senha = row
                if senha == password:
                    print('WARNING - DATABASE - check_user_and_pass: Username and password match, user authenticated! USER_ID:', user_id, 'USERNAME:', username)
                    return 2, True, user_id
                else: 
                    print('WARNING - DATABASE - check_user_and_pass: Existing user but incorrect password! USER_ID:', user_id, 'USERNAME:', username)
                    mail(username)
                    print("email sent to user:",username," for unauth user entry try")
                                   
                    
                    return 1, False, user_id
            else:
                print("ERROR - DATABASE - check_user_and_pass: User does not exist in the database!")
                return 3, False, 0
    except Exception as e:
        print("ERROR - DATABASE - Unable to verify username and password:", e)

def get_user_and_passw(id):
    try:
        con = sql.connect("database.db")
        cur = con.cursor()
        cur.execute("SELECT * FROM tb_usuario")
        rows = cur.fetchall()
        if id < len(rows):
            username = rows[id][1]
            password = rows[id][2]
            return username, password
        else:
            print("ERROR - DATABASE - User ID out of range!")
    except Exception as e:
        print("Unable to obtain users:", e)

def get_user_id(username):
    try:
        with sql.connect("database.db") as con:
            cur = con.cursor()
            cur.execute("SELECT id FROM tb_usuario WHERE username=?", (username,))
            row = cur.fetchone()
            if row:
                user_id = row[0]
                return user_id
            else:
                print("User not found in the database!")
    except Exception as e:
        print("Unable to obtain USER_ID from the database:", e)

