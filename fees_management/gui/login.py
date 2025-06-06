import tkinter as tk
from tkinter import messagebox
from signup_window import SignupWindow
from dashboard import Dashboard
from user_manager import UserManager

class LoginWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Login")
        self.geometry("400x300")

        tk.Label(self, text="Email").pack(pady=5)
        self.email_entry = tk.Entry(self)
        self.email_entry.pack(pady=5)

        tk.Label(self, text="Password").pack(pady=5)
        self.password_entry = tk.Entry(self, show="*")
        self.password_entry.pack(pady=5)

        tk.Button(self, text="Login", command=self.login_user).pack(pady=10)
        tk.Button(self, text="Sign Up", command=self.open_signup).pack()

    def login_user(self):
        email = self.email_entry.get()
        password = self.password_entry.get()
        manager = UserManager()

        if manager.verify_user(email, password):
            messagebox.showinfo("Success", "Login successful")
            self.destroy()
            Dashboard(email).mainloop()
        else:
            messagebox.showerror("Error", "Invalid credentials")

    def open_signup(self):
        self.withdraw()
        signup = SignupWindow(self)
        signup.mainloop()


