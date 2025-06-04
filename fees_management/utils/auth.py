import customtkinter as ctk
from tkinter import messagebox
from utils.otp_sender import send_otp

class Auth:
    def __init__(self):
        self.users = {}

    def login(self, email, password):
        return email in self.users and self.users[email] == password

    def signup_popup(self):
        win = ctk.CTkToplevel()
        win.title("Sign Up")
        win.geometry("400x300")

        ctk.CTkLabel(win, text="Email").pack(pady=5)
        email_entry = ctk.CTkEntry(win, placeholder_text="Email")
        email_entry.pack(pady=5)

        ctk.CTkLabel(win, text="Password").pack(pady=5)
        password_entry = ctk.CTkEntry(win, placeholder_text="Password", show="*")
        password_entry.pack(pady=5)

        ctk.CTkLabel(win, text="Enter OTP").pack(pady=5)
        otp_entry = ctk.CTkEntry(win, placeholder_text="Enter OTP")
        otp_entry.pack(pady=5)

        def send_otp_and_store():
            email_value = email_entry.get()
            if email_value:
                try:
                    win.generated_otp = send_otp(email_value)
                    messagebox.showinfo("OTP Sent", f"OTP sent to {email_value}")
                except Exception as e:
                    messagebox.showerror("Error", f"Failed to send OTP:\n{e}")
            else:
                messagebox.showwarning("Missing Email", "Please enter your email before requesting OTP")

        def verify():
            email_value = email_entry.get()
            password_value = password_entry.get()
            entered_otp = otp_entry.get()

            if not email_value or not password_value or not entered_otp:
                messagebox.showwarning("Missing Fields", "Fill all fields before verifying")
                return

            if entered_otp == getattr(win, 'generated_otp', ''):
                self.users[email_value] = password_value
                messagebox.showinfo("Success", "Account created successfully")
                win.destroy()
            else:
                messagebox.showerror("Invalid OTP", "The OTP entered is incorrect")

        ctk.CTkButton(win, text="Send OTP", command=send_otp_and_store).pack(pady=10)
        ctk.CTkButton(win, text="Verify & Sign Up", command=verify).pack(pady=10)
