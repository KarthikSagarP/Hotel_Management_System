from tkinter import *
from tkinter import messagebox

class LoginPage:
    def __init__(self, master, on_login_success):
        self.master = master
        self.master.title("Login Page")
        self.master.geometry("400x400")
        self.on_login_success = on_login_success  # Store the callback function

        # Create and place the username label and entry
        Label(self.master, text="Username").pack(pady=10)
        self.username_entry = Entry(self.master)
        self.username_entry.pack(pady=5)

        # Create and place the password label and entry
        Label(self.master, text="Password").pack(pady=10)
        self.password_entry = Entry(self.master, show="*")
        self.password_entry.pack(pady=5)

        # Create and place the login button
        login_button = Button(self.master, text="Login", command=self.login)
        login_button.pack(pady=20)

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        # Predefined credentials (for demonstration purposes)
        if username == "admin" and password == "password":
            messagebox.showinfo("Login Successful", "Welcome!")
            self.on_login_success()  # Call the success callback
            self.master.destroy()  # Close the login window
        else:
            messagebox.showerror("Login Failed", "Invalid username or password.")