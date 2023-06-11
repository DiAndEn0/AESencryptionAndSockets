from os import name
import socket
import struct
import pickle
import sqlite3 as sql
import threading


def create_listening_socket(addr, port):
    # Creating a new socket object
    s = socket.socket()
    # Binding the socket to a specific address and port
    s.bind((addr, port))
    # Configure the socket backlog to 5
    s.listen(5)
    return s


def wait_for_connection(s):
    print('Waiting for connection...')
    conn, addr = s.accept()
    print('Got a new connection from: {0}'.format(addr))
    return conn


def run_server():
    server_socket = create_listening_socket('127.0.0.1', 5000)
    db = DBHandler("finalTask.db")
    db.post_all_users()
    finished = False
    while not finished:
        conn = wait_for_connection(server_socket)
        connection_on = True
        while connection_on:
            data = handle_connection(conn, db)
            if data in (b'q', b'terminate'):
                connection_on = False
                if data == b'terminate':
                    finished = True
        print('Closing connection')
        conn.close()
    print('Shutting down server')
    server_socket.close()


def handle_connection(client_socket, db):
    try:
        request = client_socket.recv(1024)
        if not request:
            return b'terminate'
        data = pickle.loads(request)
        if data['action'] == 'login':
            if db.check_user(data['username'], data['password']):
                response = {'status': 'success'}
            else:
                response = {'status': 'failure'}
            client_socket.send(pickle.dumps(response))

        elif data['action'] == 'search_student':
            if db.check_student(data['name']):
                response = {'status': 'success',
                            'student': db.check_student(data['name'])}
            else:
                response = {'status': 'failure'}
            client_socket.send(pickle.dumps(response))

        elif data['action'] == 'search_highest':
            if db.check_highest(data['name']):
                response = {'status': 'success',
                            'student': db.check_highest(data['name'])}
            else:
                response = {'status': 'failure'}
            client_socket.send(pickle.dumps(response))

        elif data['action'] == 'search_average':
            if db.check_average(data['name']):
                response = {'status': 'success',
                            'student': db.check_average(data['name'])}
            else:
                response = {'status': 'failure'}
            client_socket.send(pickle.dumps(response))

        elif data['action'] == 'add_student':
            db.add_stud(data['name'], data['class'], data['marks'])
            response = {'status': 'success'}
            client_socket.send(pickle.dumps(response))

    except Exception as e:
        print(f"Error occurred while handling connection: {e}")
        response = {'status': 'error', 'message': str(e)}
        client_socket.send(pickle.dumps(response))

    return request


class DBHandler:

    def __init__(self, db_path):
        self.conn = sql.connect(db_path)
        self.cursor = self.conn.cursor()

    def check_user(self, username, password):
        query = "SELECT * FROM users WHERE username=? AND password=?"
        result = self.cursor.execute(query, (username, password)).fetchone()
        return result is not None

    def post_all_users(self):
        query = """SELECT * FROM users"""
        result = self.cursor.execute(query).fetchall()
        print(result)

    def check_student(self, name):
        result = self.cursor.execute(
            """SELECT * FROM student WHERE name = ? ;""", (name,)).fetchone()
        return result

    def check_highest(self, name):
        result = self.cursor.execute("""SELECT marks from student
        WHERE NAME = ?;
        """, (name,))
        res = result.fetchone()[0]
        marks_list = [int(mark) for mark in res.split(',')]
        max_number = max(marks_list)
        return max_number

    def check_average(self, name):
        result = self.cursor.execute("""SELECT marks from student 
        WHERE NAME = ?;
        """, (name,))
        res = result.fetchone()[0]
        marks_list = [int(mark) for mark in res.split(',')]
        avg_mark = sum(marks_list) / len(marks_list)
        return avg_mark

    def add_stud(self, name, class_, marks):
        query = """SELECT MAX(ID) FROM student;"""
        self.cursor.execute(query)
        res = self.cursor.fetchone()
        if res[0] is not None:
            id = int(res[0]) + 1
        else:
            id = 1
        self.cursor.execute("""INSERT INTO student (ID, name, class, marks)
        VALUES (?, ?, ?, ?);
        """, (id, name, class_, marks))
        self.conn.commit()

    def __del__(self):
        self.cursor.close()
        self.conn.close()


if __name__ == '__main__':
    run_server()
