# fees_management/gui/dashboard.py

import customtkinter as ctk
from tkinter import messagebox

class Dashboard(ctk.CTkToplevel):
    def __init__(self, user_email):
        super().__init__()
        self.title("Dashboard")
        self.geometry("700x500")
        self.user_email = user_email

        ctk.CTkLabel(self, text=f"Welcome, {self.user_email}", font=("Arial", 20)).pack(pady=20)

        ctk.CTkButton(self, text="➕ Add Student", command=self.add_student).pack(pady=10)
        ctk.CTkButton(self, text="📋 View Students", command=self.view_students).pack(pady=10)
        ctk.CTkButton(self, text="📊 View Analytics", command=self.view_analytics).pack(pady=10)
        ctk.CTkButton(self, text="📤 Export to Excel", command=self.export_excel).pack(pady=10)
        ctk.CTkButton(self, text="🚪 Logout", fg_color="red", command=self.logout).pack(pady=20)

    def add_student(self):
        messagebox.showinfo("Add", "Add Student UI Coming Soon...")

    def view_students(self):
        messagebox.showinfo("View", "View Student Records Coming Soon...")

    def view_analytics(self):
        messagebox.showinfo("Analytics", "Graphs Coming Soon...")

    def export_excel(self):
        messagebox.showinfo("Export", "Export Feature Coming Soon...")

    def logout(self):
        self.destroy()
from gui.add_student import AddStudent

def add_student(self):
    AddStudent()
