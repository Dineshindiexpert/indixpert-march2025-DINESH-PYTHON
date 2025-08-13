import sys
import os
from menu import menu_management
from reservation import reservation_management
from order import order_management
from billing import billing_management
from reports import reports_management
from user import User

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
USERS_FILE = os.path.join(BASE_DIR, 'data', 'users.json')

def login():
    print("\n--- Login ---")
    role_map = {'1': 'admin', '2': 'staff'}
    while True:
        print("Login as:")
        print("1) Admin")
        print("2) Staff")
        print("0) Exit")
        role_choice = input("Select role (1, 2, or 0 to exit): ")
        if role_choice == '0':
            print("Exiting... Goodbye!")
            sys.exit()
        if role_choice in role_map:
            required_role = role_map[role_choice]
            break
        else:
            print("Invalid choice. Please select 1, 2, or 0.")
    for _ in range(3):
        username = input("Username: ")
        password = input("Password: ")
        user = User.authenticate(username, password, USERS_FILE, required_role)
        if user:
            print(f"\nWelcome, {user.username}! Role: {user.role}")
            return user
        else:
            print(f"Invalid credentials for {required_role}. Please try again.")
    print("Too many failed attempts. Exiting.")
    sys.exit()

def main_menu(user):
    while True:
        print("\n--- Restaurant Management System ---")
        print("1. Menu Management")
        print("2. Table Reservation")
        print("3. Order Management")
        print("4. Billing/Payment")
        if user.role == 'admin':
            print("6. Reports")
            print("7. Cancel Order")
        print("0. Exit")
        choice = input("Select an option: ")
        if choice == '1':
            menu_management(user)
        elif choice == '2':
            reservation_management(user)
        elif choice == '3':
            order_management(user)
        elif choice == '4':
            billing_management(user)
        elif choice == '6' and user.role == 'admin':
            reports_management(user)
        elif choice == '7' and user.role == 'admin':

            print("Cancel order feature (admin only) - TODO")
        elif choice == '0':
            print("Exiting... Goodbye!")
            sys.exit()
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    user = login()
    main_menu(user)
