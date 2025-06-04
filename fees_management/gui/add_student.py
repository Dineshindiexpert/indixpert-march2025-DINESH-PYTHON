# fees_management/gui/add_student.py

import customtkinter as ctk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import os

class AddStudent(ctk.CTkToplevel):
    def __init__(self):
        super().__init__()
        self.title("Add Student")
        self.geometry("600x500")
        self.photo_path = ""

        ctk.CTkLabel(self, text="Add Student Details", font=("Arial", 22)).pack(pady=10)

        self.name_var = ctk.StringVar()
        self.email_var = ctk.StringVar()
        self.course_var = ctk.StringVar()
        self.fees_var = ctk.StringVar()
        self.date_var = ctk.StringVar()

        form_frame = ctk.CTkFrame(self)
        form_frame.pack(pady=10, padx=20, fill="both", expand=True)

        # Form layout
        ctk.CTkLabel(form_frame, text="Full Name").grid(row=0, column=0, padx=10, pady=5, sticky="w")
        ctk.CTkEntry(form_frame, textvariable=self.name_var).grid(row=0, column=1, padx=10, pady=5)

        ctk.CTkLabel(form_frame, text="Email").grid(row=1, column=0, padx=10, pady=5, sticky="w")
        ctk.CTkEntry(form_frame, textvariable=self.email_var).grid(row=1, column=1, padx=10, pady=5)

        ctk.CTkLabel(form_frame, text="Course").grid(row=2, column=0, padx=10, pady=5, sticky="w")
        ctk.CTkComboBox(form_frame, values=["Python", "Java", "Web Dev", "Data Science"],
                        variable=self.course_var).grid(row=2, column=1, padx=10, pady=5)

        ctk.CTkLabel(form_frame, text="Fees Paid").grid(row=3, column=0, padx=10, pady=5, sticky="w")
        ctk.CTkEntry(form_frame, textvariable=self.fees_var).grid(row=3, column=1, padx=10, pady=5)

        ctk.CTkLabel(form_frame, text="Join Date (YYYY-MM-DD)").grid(row=4, column=0, padx=10, pady=5, sticky="w")
        ctk.CTkEntry(form_frame, textvariable=self.date_var).grid(row=4, column=1, padx=10, pady=5)

        ctk.CTkButton(form_frame, text="Upload Photo", command=self.upload_photo).grid(row=5, column=0, columnspan=2, pady=10)

        self.photo_label = ctk.CTkLabel(form_frame, text="No Image", width=100, height=100, corner_radius=10)
        self.photo_label.grid(row=6, column=0, columnspan=2)

        ctk.CTkButton(self, text="Save Student", command=self.save_student).pack(pady=15)

    def upload_photo(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
        if file_path:
            self.photo_path = file_path
            img = Image.open(file_path)
            img = img.resize((100, 100))
            img = ImageTk.PhotoImage(img)
            self.photo_label.configure(image=img, text="")
            self.photo_label.image = img

    def save_student(self):
        # Save data (in memory or local file for now)
        if not self.name_var.get() or not self.email_var.get():
            messagebox.showerror("Error", "Please fill all fields")
            return

        messagebox.showinfo("Saved", f"{self.name_var.get()} saved successfully!")
        self.destroy()
