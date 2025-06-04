import customtkinter as ctk
from tkinter import messagebox
from user_manager import UserManager
from gui.signup import SignupWindow
from gui.dashboard import Dashboard

class LoginWindow(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Login Window")
        self.geometry("400x300")
        self.resizable(False, False)

        self.user_manager = UserManager()

        ctk.CTkLabel(self, text="Email:").pack(pady=(40, 5))
        self.email_entry = ctk.CTkEntry(self, placeholder_text="Enter your email")
        self.email_entry.pack(pady=5, ipadx=50)

        ctk.CTkLabel(self, text="Password:").pack(pady=(20, 5))
        self.password_entry = ctk.CTkEntry(self, placeholder_text="Enter your password", show="*")
        self.password_entry.pack(pady=5, ipadx=50)

        login_btn = ctk.CTkButton(self, text="Login", command=self.login_user)
        login_btn.pack(pady=(30, 10), ipadx=20)

        signup_btn = ctk.CTkButton(self, text="Sign Up", command=self.open_signup)
        signup_btn.pack(ipadx=20)

    def login_user(self):
        email = self.email_entry.get().strip()
        password = self.password_entry.get()

        if not email or not password:
            messagebox.showwarning("Input Error", "Please enter both email and password.")
            return

        if self.user_manager.verify_user(email, password):
            messagebox.showinfo("Success", "Login successful!")
            self.destroy()
            dash = Dashboard(email)
            dash.mainloop()
        else:
            messagebox.showerror("Error", "Invalid email or password.")

    def open_signup(self):
        self.withdraw()
        signup_window = SignupWindow(self)
        signup_window.mainloop()
        self.deiconify()

if __name__ == "__main__":
    app = LoginWindow()
    app.mainloop()
