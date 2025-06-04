import customtkinter as ctk
from tkinter import messagebox
from user_manager import UserManager

class SignupWindow(ctk.CTk):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.title("Sign Up")
        self.geometry("400x350")
        self.resizable(False, False)

        self.user_manager = UserManager()

        ctk.CTkLabel(self, text="Email:").pack(pady=(40, 5))
        self.email_entry = ctk.CTkEntry(self, placeholder_text="Enter your email")
        self.email_entry.pack(pady=5, ipadx=50)

        ctk.CTkLabel(self, text="Password:").pack(pady=(20, 5))
        self.password_entry = ctk.CTkEntry(self, placeholder_text="Enter your password", show="*")
        self.password_entry.pack(pady=5, ipadx=50)

        ctk.CTkLabel(self, text="Confirm Password:").pack(pady=(20, 5))
        self.confirm_entry = ctk.CTkEntry(self, placeholder_text="Confirm your password", show="*")
        self.confirm_entry.pack(pady=5, ipadx=50)

        signup_btn = ctk.CTkButton(self, text="Sign Up", command=self.signup_user)
        signup_btn.pack(pady=30, ipadx=20)

    def signup_user(self):
        email = self.email_entry.get().strip()
        password = self.password_entry.get()
        confirm = self.confirm_entry.get()

        if not email or not password or not confirm:
            messagebox.showwarning("Input Error", "Please fill all fields.")
            return

        if password != confirm:
            messagebox.showerror("Error", "Passwords do not match.")
            return

        if self.user_manager.add_user(email, password):
            messagebox.showinfo("Success", "Account created successfully!")
            self.destroy()
            self.parent.deiconify()
        else:
            messagebox.showerror("Error", "Email already registered.")
