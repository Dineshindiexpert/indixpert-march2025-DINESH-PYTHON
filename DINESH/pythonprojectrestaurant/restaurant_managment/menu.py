import os
from utils import load_json, save_json, center_text, center_block
from tabulate import tabulate
import shutil

MENU_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data', 'menu.json')

class MenuItem:
    def __init__(self, item_id, name, price, category):
        self.item_id = item_id
        self.name = name
        self.price = price
        self.category = category

    def to_dict(self):
        return {
            "item_id": self.item_id,
            "name": self.name,
            "price": self.price,
            "category": self.category
        }

    @staticmethod
    def from_dict(data):
        return MenuItem(data["item_id"], data["name"], data["price"], data["category"])

def display_menu(menu_items):
    print("\n" + center_text("--- MENU ---"))
    if not menu_items:
        print(center_text("No menu items found."))
        return
    table = [[item.item_id, item.name, f"Rs.{item.price}", item.category.capitalize()] for item in menu_items]
    table_str = tabulate(table, headers=["ID", "Name", "Price", "Category"], tablefmt="fancy_grid")
    print(center_block(table_str))

def get_menu_items():
    data = load_json(MENU_FILE, default=[])
    return [MenuItem.from_dict(d) for d in data]

def save_menu_items(menu_items):
    save_json(MENU_FILE, [item.to_dict() for item in menu_items])

def add_menu_item(menu_items):
    name = input(center_text("Enter dish name: ")).strip()
    if not name:
        print(center_text("Dish name cannot be empty."))
        return
    if any(item.name.lower() == name.lower() for item in menu_items):
        print(center_text("Dish name already exists."))
        return
    try:
        price = float(input(center_text("Enter price: ")))
        if price <= 0:
            print(center_text("Price must be positive."))
            return
    except ValueError:
        print(center_text("Invalid price. Please enter a number."))
        return
    print(center_text("Select category:"))
    categories = ["breakfast", "lunch", "dinner", "snacks", "special", "other"]
    for idx, cat in enumerate(categories, 1):
        print(center_text(f"{idx}. {cat.capitalize()}"))
    try:
        cat_choice = int(input(center_text("Enter category number: ")))
        if not (1 <= cat_choice <= len(categories)):
            print(center_text("Invalid category selection."))
            return
    except ValueError:
        print(center_text("Invalid input. Please enter a number."))
        return
    category = categories[cat_choice-1]
    item_id = max([item.item_id for item in menu_items], default=0) + 1
    menu_items.append(MenuItem(item_id, name, price, category))
    save_menu_items(menu_items)
    print(center_text("Item added!"))

def edit_menu_item(menu_items):
    try:
        item_id = int(input(center_text("Enter item ID to edit: ")))
    except ValueError:
        print(center_text("Invalid input. Please enter a number."))
        return
    for item in menu_items:
        if item.item_id == item_id:
            new_name = input(center_text(f"Enter new name ({item.name}): ")).strip()
            if new_name:
                if any(i.name.lower() == new_name.lower() and i.item_id != item_id for i in menu_items):
                    print(center_text("Dish name already exists."))
                    return
                item.name = new_name
            try:
                new_price = input(center_text(f"Enter new price ({item.price}): "))
                if new_price:
                    new_price = float(new_price)
                    if new_price <= 0:
                        print(center_text("Price must be positive."))
                        return
                    item.price = new_price
            except ValueError:
                print(center_text("Invalid price. Please enter a number."))
                return
            print(center_text("Select new category or press Enter to keep current:"))
            categories = ["breakfast", "lunch", "dinner", "snacks", "special", "other"]
            for idx, cat in enumerate(categories, 1):
                print(center_text(f"{idx}. {cat.capitalize()}"))
            cat_input = input(center_text(f"Enter category number ({item.category}): "))
            if cat_input:
                try:
                    cat_choice = int(cat_input)
                    if not (1 <= cat_choice <= len(categories)):
                        print(center_text("Invalid category selection."))
                        return
                    item.category = categories[cat_choice-1]
                except ValueError:
                    print(center_text("Invalid input. Please enter a number."))
                    return
            save_menu_items(menu_items)
            print(center_text("Item updated!"))
            return
    print(center_text("Item not found."))

def delete_menu_item(menu_items):
    try:
        item_id = int(input(center_text("Enter item ID to delete: ")))
    except ValueError:
        print(center_text("Invalid input. Please enter a number."))
        return
    for i, item in enumerate(menu_items):
        if item.item_id == item_id:
            del menu_items[i]
            save_menu_items(menu_items)
            print(center_text("Item deleted!"))
            return
    print(center_text("Item not found."))

def menu_management(user):
    while True:
        menu_items = get_menu_items()
        print("\n" + center_text("--- Menu Management ---"))
        print(center_text("1. View Menu"))
        if user.role == 'admin':
            print(center_text("2. Add Menu Item"))
            print(center_text("3. Edit Menu Item"))
            print(center_text("4. Delete Menu Item"))
        print(center_text("0. Back to Main Menu"))
        choice = input(center_text("Select an option: "))
        if choice == '1':
            display_menu(menu_items)
            input(center_text("(Press Enter to continue)"))
        elif choice == '2' and user.role == 'admin':
            add_menu_item(menu_items)
        elif choice == '3' and user.role == 'admin':
            edit_menu_item(menu_items)
        elif choice == '4' and user.role == 'admin':
            delete_menu_item(menu_items)
        elif choice == '0':
            break
        else:
            print(center_text("Invalid choice. Please try again."))
