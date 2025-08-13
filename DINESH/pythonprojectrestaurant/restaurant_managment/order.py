import os
from utils import load_json, save_json, center_text, center_block
from menu import get_menu_items
from tabulate import tabulate

ORDERS_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data', 'orders.json')
RESERVATIONS_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data', 'reservations.json')

# Helper to get all orders
def get_orders():
    return load_json(ORDERS_FILE, default=[])

def save_orders(orders):
    save_json(ORDERS_FILE, orders)

# Helper to get menu items as dict for name lookup
def get_menu_dict():
    return {item.item_id: item for item in get_menu_items()}

def display_order_details(order):
    menu_dict = get_menu_dict()
    print("\n" + center_text(f"Order ID: {order['order_id']}"))
    print(center_text(f"Table Number: {order['table_number']}"))
    # Prepare items table
    item_rows = []
    for item_id in order['items']:
        item = menu_dict.get(item_id)
        if item:
            item_rows.append([item_id, item.name, f"Rs.{item.price}"])
        else:
            item_rows.append([item_id, "(not found)", "-"])
    if item_rows:
        table_str = tabulate(item_rows, headers=["Item ID", "Name", "Price"], tablefmt="fancy_grid")
        print(center_block(table_str))
    print(center_text(f"Total: Rs.{order['total']}"))
    print(center_text(f"Status: {order['status'].capitalize()}"))
    if order.get('paid'):
        print(center_text(f"Payment: Paid ({order.get('payment_method', 'N/A').capitalize()})"))
    else:
        print(center_text("Payment: Not Paid"))

def search_order_by_id():
    orders = get_orders()
    try:
        order_id = int(input("Enter Order ID to search: "))
    except ValueError:
        print("Invalid input.")
        return
    for order in orders:
        if order['order_id'] == order_id:
            display_order_details(order)
            return
    print("Order not found.")

def take_new_order():
    # Validate table number
    try:
        table_number = int(input("Enter table number: "))
        if table_number <= 0:
            print("Invalid table number.")
            return
    except ValueError:
        print("Invalid input. Table number must be a number.")
        return
    # Show menu
    menu_items = get_menu_items()
    menu_dict = {item.item_id: item for item in menu_items}
    print("\nMenu:")
    for item in menu_items:
        print(f"{item.item_id}. {item.name} (Rs.{item.price}) [{item.category}]")
    # Take items
    order_items = []
    while True:
        item_input = input("Enter item ID to add (or 0 to finish): ")
        if item_input == '0':
            break
        try:
            item_id = int(item_input)
            if item_id not in menu_dict:
                print("Invalid item ID.")
                continue
            qty = int(input(f"Enter quantity for {menu_dict[item_id].name}: "))
            if qty <= 0:
                print("Quantity must be positive.")
                continue
            order_items.extend([item_id] * qty)
        except ValueError:
            print("Invalid input. Please enter numbers only.")
    if not order_items:
        print("No items added. Order cancelled.")
        return
    # Calculate total
    total = sum(menu_dict[item_id].price for item_id in order_items)
    # Save order
    orders = get_orders()
    order_id = max([o['order_id'] for o in orders], default=0) + 1
    new_order = {
        'order_id': order_id,
        'table_number': table_number,
        'items': order_items,
        'total': total,
        'status': 'pending',
        'paid': False
    }
    orders.append(new_order)
    save_orders(orders)
    print(f"Order placed! Order ID: {order_id}")

def generate_bill():
    orders = get_orders()
    try:
        order_id = int(input(center_text("Enter Order ID to generate bill: ")))
    except ValueError:
        print(center_text("Invalid input."))
        return
    for order in orders:
        if order['order_id'] == order_id:
            print("\n" + center_text("--- BILL ---"))
            display_order_details(order)
            if order.get('paid'):
                print(center_text("This order is already paid."))
                return
            print(center_text("Select payment method:"))
            print(center_text("1. UPI"))
            print(center_text("2. Credit Card"))
            print(center_text("3. Cash"))
            method_choice = input(center_text("Enter option (1/2/3): ")).strip()
            payment_method = ""
            if method_choice == '1':
                payment_method = "UPI"
            elif method_choice == '2':
                payment_method = "Credit Card"
            elif method_choice == '3':
                payment_method = "Cash"
            else:
                print(center_text("Invalid payment method. Payment not recorded."))
                return
            order['paid'] = True
            order['payment_method'] = payment_method
            save_orders(orders)
            print(center_text(f"Order marked as paid via {payment_method}."))
            return
    print(center_text("Order not found."))

def order_management(user):
    while True:
        print("\n" + center_text("--- Order Management ---"))
        print(center_text("1. View All Orders"))
        if user.role == 'admin':
            print(center_text("2. Search Order by ID"))
            print(center_text("3. Take New Order (Customer)"))
            print(center_text("4. Generate Bill / Payment"))
        else:
            print(center_text("2. Take New Order (Customer)"))
            print(center_text("3. Generate Bill / Payment"))
        print(center_text("0. Back to Main Menu"))
        choice = input(center_text("Select an option: "))
        if choice == '1':
            orders = get_orders()
            for order in orders:
                display_order_details(order)
            input(center_text("(Press Enter to continue)"))
        elif (choice == '2' and user.role == 'admin'):
            search_order_by_id()
            input(center_text("(Press Enter to continue)"))
        elif (choice == '2' and user.role == 'staff') or (choice == '3' and user.role == 'admin'):
            take_new_order()
            input(center_text("(Press Enter to continue)"))
        elif (choice == '3' and user.role == 'staff') or (choice == '4' and user.role == 'admin'):
            generate_bill()
            input(center_text("(Press Enter to continue)"))
        elif choice == '0':
            break
        else:
            print(center_text("Invalid choice. Please try again."))
