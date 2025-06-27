def show_main_menu():
    print("\n===== STUDENT MANAGEMENT MENU =====")
    print("1. Register Students")
    print("2. Display Students")
    print("3. Search Students")
    print("4. Exit")
    print("====================================")

def get_user_choice():
    while True:
        try:
            choice = int(input("Enter your choice (1-4): "))
            if 1 <= choice <= 4:
                return choice
            else:
                print("Please enter a number between 1 and 4.")
        except ValueError:
            print("Invalid input! Please enter a number.")
