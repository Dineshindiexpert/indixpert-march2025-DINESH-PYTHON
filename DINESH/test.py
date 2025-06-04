try:
    import traceback
    import sys
    import tkinter as tk
    from tkinter import ttk, messagebox
    import mysql.connector

    print("Starting Fees Management System...")

    # ------------------ Database Setup ------------------
    def create_database():
        try:
            conn = mysql.connector.connect(host='localhost', user='root', password='1234')
            cursor = conn.cursor()
            cursor.execute("CREATE DATABASE IF NOT EXISTS fees_management")
            cursor.execute("USE fees_management")
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS students (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    name VARCHAR(100),
                    course VARCHAR(100),
                    fees_paid FLOAT
                )
            """)
            conn.commit()
            conn.close()
            print("✅ Database and table are ready.")
        except Exception as e:
            print("❌ Error in create_database:", e)
            traceback.print_exc()
            sys.exit()

    create_database()

    # ------------------ Main Application ------------------
    class FeesManagementSystem:
        def __init__(self, root):
            self.root = root
            self.root.title("Fees Management System")
            self.root.geometry("800x600")
            self.root.configure(bg="#f0f4f7")

            title = tk.Label(root, text="Fees Management System", font=("Arial", 24, "bold"), bg="#007acc", fg="white")
            title.pack(side=tk.TOP, fill=tk.X)

            # Frames
            self.frame1 = tk.Frame(root, bd=2, relief=tk.RIDGE, bg="white")
            self.frame1.place(x=20, y=60, width=350, height=500)

            self.frame2 = tk.Frame(root, bd=2, relief=tk.RIDGE, bg="white")
            self.frame2.place(x=390, y=60, width=380, height=500)

            # Variables
            self.name_var = tk.StringVar()
            self.course_var = tk.StringVar()
            self.fees_paid_var = tk.DoubleVar()

            # Frame 1 - Input
            tk.Label(self.frame1, text="Student Name", font=("Arial", 12)).pack(pady=10)
            tk.Entry(self.frame1, textvariable=self.name_var, font=("Arial", 12)).pack()

            tk.Label(self.frame1, text="Course", font=("Arial", 12)).pack(pady=10)
            tk.Entry(self.frame1, textvariable=self.course_var, font=("Arial", 12)).pack()

            tk.Label(self.frame1, text="Fees Paid", font=("Arial", 12)).pack(pady=10)
            tk.Entry(self.frame1, textvariable=self.fees_paid_var, font=("Arial", 12)).pack()

            tk.Button(self.frame1, text="Add Record", font=("Arial", 12, "bold"), bg="#28a745", fg="white", command=self.add_record).pack(pady=20)

            # Frame 2 - Table
            self.tree = ttk.Treeview(self.frame2, columns=("ID", "Name", "Course", "Fees"), show='headings')
            self.tree.heading("ID", text="ID")
            self.tree.heading("Name", text="Name")
            self.tree.heading("Course", text="Course")
            self.tree.heading("Fees", text="Fees Paid")
            self.tree.pack(fill=tk.BOTH, expand=True)

            self.load_data()

        def add_record(self):
            name = self.name_var.get()
            course = self.course_var.get()
            fees = self.fees_paid_var.get()

            if name.strip() == "" or course.strip() == "" or fees <= 0:
                messagebox.showerror("Error", "Please fill all fields correctly")
                return

            try:
                conn = mysql.connector.connect(host='localhost', user='root', password='1234', database='fees_management')
                cursor = conn.cursor()
                cursor.execute("INSERT INTO students (name, course, fees_paid) VALUES (%s, %s, %s)", (name, course, fees))
                conn.commit()
                conn.close()
                messagebox.showinfo("Success", "Record added successfully")
                self.load_data()
                self.clear_inputs()
            except Exception as e:
                messagebox.showerror("Database Error", f"Failed to add record:\n{e}")

        def load_data(self):
            try:
                for row in self.tree.get_children():
                    self.tree.delete(row)

                conn = mysql.connector.connect(host='localhost', user='root', password='1234', database='fees_management')
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM students")
                rows = cursor.fetchall()
                conn.close()

                for row in rows:
                    self.tree.insert('', tk.END, values=row)
            except Exception as e:
                messagebox.showerror("Database Error", f"Failed to load data:\n{e}")

        def clear_inputs(self):
            self.name_var.set("")
            self.course_var.set("")
            self.fees_paid_var.set(0.0)

    # ------------------ Run App ------------------
    if __name__ == "__main__":
        print("Launching GUI...")
        root = tk.Tk()
        app = FeesManagementSystem(root)
        root.mainloop()

except Exception as e:
    print("Fatal error:", e)
    traceback.print_exc()
    input("Press Enter to exit...")
