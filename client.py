import tkinter as tk
import pickle
import socket

from tkinter import messagebox


class Client:

    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.client_socket = socket.socket()
        self.client_socket.connect((self.host, self.port))

    def login(self):
        username = username_entry.get()
        password = password_entry.get()

        data = {'action': 'login', 'username': username, 'password': password}
        self.client_socket.send(pickle.dumps(data))
        response = pickle.loads(self.client_socket.recv(1024))
        return response

    def search_student(self):
        student_name = student_name_entry.get()

        data = {'action': 'search_student', 'name': student_name}
        self.client_socket.send(pickle.dumps(data))
        response = pickle.loads(self.client_socket.recv(1024))
        return response

    def search_highest(self):
        student_name = student_name_entry.get()

        data = {'action': 'search_highest', 'name': student_name}
        self.client_socket.send(pickle.dumps(data))
        response = pickle.loads(self.client_socket.recv(1024))
        return response

    def search_average(self):
        student_name = student_name_entry.get()

        data = {'action': 'search_average', 'name': student_name}
        self.client_socket.send(pickle.dumps(data))
        response = pickle.loads(self.client_socket.recv(1024))
        return response

    def add_student_db(self):
        student_name = student_name_entry.get()
        class_ = class_entry.get()
        marks = marks_entry.get()

        data = {'action': 'add_student', 'name': student_name,
                'class': class_, 'marks': marks}
        self.client_socket.send(pickle.dumps(data))
        response = pickle.loads(self.client_socket.recv(1024))
        return response


def login():
    response = client.login()
    if response['status'] == 'success':
        messagebox.showinfo(
            "Login Success", "You have logged in successfully.")
        show_all_radiobuttons()
    else:
        messagebox.showerror("Login Error", "Invalid username or password.")


# Create a function to toggle the visibility of the student details fields and buttons
def toggle_add_student(visible):
    if visible == True:
        student_name_entry.config(state="normal")
        class_entry.config(state="normal")
        marks_entry.config(state="normal")
        add_button.config(state="normal")
        search_button.config(state="disabled")
        student_name_label.pack()
        student_name_entry.pack()
        class_label.pack()
        class_entry.pack()
        marks_label.pack()
        marks_entry.pack()
        add_button.pack()
        search_button.pack_forget()
    else:
        search_button.config(state="normal")
        student_name_entry.config(state="normal")
        student_name_label.pack()
        student_name_entry.pack()
        class_label.pack_forget()
        class_entry.pack_forget()
        marks_label.pack_forget()
        marks_entry.pack_forget()
        add_button.pack_forget()
        search_button.pack()


def toggle_search_button_visibility(visible):
    if visible == False:
        search_button.config(state="normal")
        search_button.pack_forget()
    else:
        search_button.pack()


def show_all_radiobuttons():
    add_student_option.config(state="normal")
    search_student_option.config(state="normal")
    highest_mark_option.config(state="normal")
    average_mark_option.config(state="normal")
    add_student_option.pack(side="left")
    search_student_option.pack(side="left")
    highest_mark_option.pack(side="left")
    average_mark_option.pack(side="left")
    username_entry.pack_forget()
    username_label.pack_forget()
    password_entry.pack_forget()
    password_label.pack_forget()
    login_button.pack_forget()


# Function to toggle radio buttons

def toggle_buttons():
    option = option_var.get()
    if option == "add":
        add_student_option.select()
        search_student_option.deselect()
        highest_mark_option.deselect()
        average_mark_option.deselect()
        toggle_add_student(True)
        toggle_search_button_visibility(False)
    elif option == "search":
        add_student_option.deselect()
        search_student_option.select()
        highest_mark_option.deselect()
        average_mark_option.deselect()
        toggle_add_student(False)
        toggle_search_button_visibility(True)
    elif option == "highest":
        add_student_option.deselect()
        search_student_option.deselect()
        highest_mark_option.select()
        average_mark_option.deselect()
        toggle_add_student(False)
        toggle_search_button_visibility(True)
    elif option == "average":
        add_student_option.deselect()
        search_student_option.deselect()
        highest_mark_option.deselect()
        average_mark_option.select()
        toggle_add_student(False)
        toggle_search_button_visibility(True)


# Create a window
gui = tk.Tk()
gui.geometry("640x860")
gui.title("Login")

# Create labels and entries for username and password
username_label = tk.Label(text="Username:")
username_label.pack()
username_entry = tk.Entry()
username_entry.pack()

password_label = tk.Label(text="Password:")
password_label.pack()
password_entry = tk.Entry(show="*")  # Use '*' to hide the password text
password_entry.pack()

# Create labels and entries for student name, class, and marks, but keep them invisible
student_name_label = tk.Label(text="Student Name:")
student_name_label.pack()
student_name_entry = tk.Entry()
student_name_entry.pack()
student_name_label.pack_forget()
student_name_entry.pack_forget()

class_label = tk.Label(text="Class:")
class_label.pack()
class_entry = tk.Entry()
class_entry.pack()
class_label.pack_forget()
class_entry.pack_forget()

marks_label = tk.Label(text="Marks:")
marks_label.pack()
marks_entry = tk.Entry()
marks_entry.pack()
marks_label.pack_forget()
marks_entry.pack_forget()


# Create a login button
login_button = tk.Button(text="Login", command=login)
login_button.pack()


# Create radio buttons
option_frame = tk.Frame(gui)
option_frame.pack()

option_var = tk.StringVar()

add_student_option = tk.Radiobutton(
    option_frame, text="Add Student", variable=option_var, value="add", state=tk.DISABLED, command=toggle_buttons)
add_student_option.deselect()
add_student_option.pack(side="left")
add_student_option.pack_forget()

search_student_option = tk.Radiobutton(
    option_frame, text="Search Student", variable=option_var, value="search", state=tk.DISABLED, command=toggle_buttons)
search_student_option.deselect()
search_student_option.pack(side="left")
search_student_option.pack_forget()

highest_mark_option = tk.Radiobutton(
    option_frame, text="Search Highest Mark", variable=option_var, value="highest", state=tk.DISABLED, command=toggle_buttons)
highest_mark_option.deselect()
highest_mark_option.pack(side="left")
highest_mark_option.pack_forget()

average_mark_option = tk.Radiobutton(
    option_frame, text="Search Average Mark", variable=option_var, value="average", state=tk.DISABLED, command=toggle_buttons)
average_mark_option.deselect()
average_mark_option.pack(side="left")
average_mark_option.pack_forget()


def search():
    option = option_var.get()
    if option == 'search':
        response = client.search_student()
        if response['status'] == 'success':
            messagebox.showinfo(
                "Student Found", response['student'])
        else:
            messagebox.showerror("No Student Found",
                                 "There is no such student in the database")
    elif option == 'highest':
        response = client.search_highest()
        if response['status'] == 'success':
            messagebox.showinfo(
                "Highest mark found", response['student'])
        else:
            messagebox.showerror("No Student Found",
                                 "There is no such student in the database")
    elif option == 'average':
        response = client.search_average()
        if response['status'] == 'success':
            messagebox.showinfo(
                "Average mark found", response['student'])
        else:
            messagebox.showerror("No Student Found",
                                 "There is no such student in the database")


def add():
    response = client.add_student_db()
    if response['status'] == 'success':
        messagebox.showinfo(
            "Student Added", response['status'])
    else:
        messagebox.showerror("Error", "Student Couldnt be added")


# Create buttons for adding a student and searching (hidden by default)
add_button = tk.Button(text="Add Student")
add_button.pack()
add_button.config(state=tk.DISABLED, command=add)
add_button.pack_forget()

search_button = tk.Button(text="Search")
search_button.pack()
search_button.config(state=tk.DISABLED, command=search)
search_button_visible = False
search_button.pack_forget()


def main():
    # Create the singleton instance
    global client
    client = Client('127.0.0.1', 5000)


if __name__ == '__main__':
    main()

# Start the window's main loop
gui.mainloop()
