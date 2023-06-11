import sqlite3 as sql
import random
import string
con = sql.connect("finalTask.db")
cur = con.cursor()


def createTables():
    cur.execute("""DROP TABLE IF EXISTS users;""")
    print("Dropped users table")
    cur.execute("""DROP TABLE IF EXISTS student;""")
    print("Dropped student table")
    cur.execute("""CREATE TABLE IF NOT EXISTS student (
    ID INTEGER PRIMARY KEY,
    name VARCHAR(255),
    class VARCHAR(255),
    marks VARCHAR(255)
    );""")
    print("Created student table")
    cur.execute("""CREATE TABLE IF NOT EXISTS users (
    username VARCHAR(255) PRIMARY KEY,
    password VARCHAR(255)
    );""")
    print("Created users table")

    # Generate a random username and password
    username = ''.join(random.choices(
        string.ascii_letters + string.digits, k=8))
    password = ''.join(random.choices(
        string.ascii_letters + string.digits, k=12))

    # Construct the query string
    cur.execute("""INSERT INTO users (username, password) VALUES ('{}', '{}');""".format(
        username, password))
    con.commit()

    cur.execute("""SELECT * FROM users""")
    result = cur.execute("""SELECT * FROM users""").fetchall()
    print(result)

    print(username)
    print(password)

    import os

    # Get the current working directory
    current_dir = os.getcwd()

    # Search for the file in the current directory and its subdirectories
    for root, dirs, files in os.walk(current_dir):
        if 'finalTask.db' in files:
            file_path = os.path.join(root, 'finalTask.db')
            print('Found file:', file_path)
            break
    else:
        print('File not found.')


def main():
    createTables()
    con.close()


if __name__ == "__main__":
    main()
