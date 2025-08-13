import os
from utils import load_json, save_json, center_text, center_block
from menu import get_menu_items, display_menu
from tabulate import tabulate
from datetime import datetime

RESERVATIONS_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data', 'reservations.json')

EXTRA_CHARGE_PER_HOUR = 100  # Rs. 100 per extra hour


def get_reservations():
    return load_json(RESERVATIONS_FILE, default=[])

def save_reservations(reservations):
    save_json(RESERVATIONS_FILE, reservations)

def display_reservations(reservations):
    print("\n" + center_text("--- Reservations ---"))
    if not reservations:
        print(center_text("No reservations found."))
        return
    table = [[
        r.get('reservation_id', ''),
        r.get('customer_name', ''),
        r.get('table_number', ''),
        r.get('start_time', r.get('time', '')),
        r.get('end_time', ''),
        r.get('status', ''),
        r.get('extra_charges', 0),
        'Paid' if r.get('paid') else 'Not Paid'
    ] for r in reservations]
    table_str = tabulate(table, headers=["ID", "Customer", "Table", "Start", "End", "Status", "Extra Charges", "Payment"], tablefmt="fancy_grid")
    print(center_block(table_str))

def book_reservation(user):
    if user.role != 'staff':
        print(center_text("Only staff can book reservations."))
        return
    reservations = get_reservations()
    reservation_id = max([r.get('reservation_id', 0) for r in reservations], default=0) + 1
    customer_name = input(center_text("Enter customer name: "))
    try:
        table_number = int(input(center_text("Enter table number: ")))
        if table_number <= 0:
            print(center_text("Invalid table number."))
            return
    except ValueError:
        print(center_text("Invalid input. Table number must be a number."))
        return
    start_time_str = input(center_text("Enter reservation start time (YYYY-MM-DD HH:MM): "))
    end_time_str = input(center_text("Enter reservation end time (YYYY-MM-DD HH:MM): "))
    try:
        start_time = datetime.strptime(start_time_str, "%Y-%m-%d %H:%M")
        end_time = datetime.strptime(end_time_str, "%Y-%m-%d %H:%M")
        duration = (end_time - start_time).total_seconds() / 3600
        if duration <= 0:
            print(center_text("End time must be after start time."))
            return
    except Exception:
        print(center_text("Invalid date/time format."))
        return
    extra_charges = 0
    if duration > 3:
        extra_hours = duration - 3
        extra_charges = int(extra_hours) * EXTRA_CHARGE_PER_HOUR
        print(center_text(f"Extra charges for {int(extra_hours)} hour(s): Rs.{extra_charges}"))
    # Show menu to staff as a single centered table
    print(center_text("Show menu to customer:"))
    from menu import get_menu_items, display_menu
    display_menu(get_menu_items())
    status = "booked"
    reservations.append({
        'reservation_id': reservation_id,
        'customer_name': customer_name,
        'table_number': table_number,
        'start_time': start_time_str,
        'end_time': end_time_str,
        'status': status,
        'extra_charges': extra_charges,
        'paid': False
    })
    save_reservations(reservations)
    print(center_text(f"Reservation booked! ID: {reservation_id}"))

def cancel_reservation():
    reservations = get_reservations()
    try:
        reservation_id = int(input(center_text("Enter reservation ID to cancel: ")))
    except ValueError:
        print(center_text("Invalid input."))
        return
    for r in reservations:
        if r['reservation_id'] == reservation_id:
            r['status'] = 'cancelled'
            save_reservations(reservations)
            print(center_text("Reservation cancelled."))
            return
    print(center_text("Reservation not found."))

def generate_reservation_bill():
    reservations = get_reservations()
    try:
        reservation_id = int(input(center_text("Enter reservation ID to generate bill: ")))
    except ValueError:
        print(center_text("Invalid input."))
        return
    for r in reservations:
        if r.get('reservation_id') == reservation_id:
            print("\n" + center_text("--- RESERVATION BILL ---"))
            table = [["Reservation ID", r.get('reservation_id', '')],
                     ["Customer", r.get('customer_name', '')],
                     ["Table", r.get('table_number', '')],
                     ["Start Time", r.get('start_time', r.get('time', ''))],
                     ["End Time", r.get('end_time', '')],
                     ["Status", r.get('status', '')],
                     ["Extra Charges", f"Rs.{r.get('extra_charges', 0)}"]]
            table_str = tabulate(table, tablefmt="fancy_grid")
            print(center_block(table_str))
            if r.get('paid'):
                print(center_text("This reservation is already paid."))
                return
            pay = input(center_text("Mark as paid? (y/n): ")).strip().lower()
            if pay == 'y':
                r['paid'] = True
                # Ask to update status
                print(center_text("Select new status for reservation:"))
                print(center_text("1. Completed"))
                print(center_text("2. Booked (keep as is)"))
                status_choice = input(center_text("Enter option (1/2): ")).strip()
                if status_choice == '1':
                    r['status'] = 'completed'
                else:
                    r['status'] = r.get('status', 'booked')
                save_reservations(reservations)
                print(center_text("Reservation marked as paid and status updated."))
            else:
                print(center_text("Reservation not marked as paid."))
            return
    print(center_text("Reservation not found."))

def reservation_management(user):
    while True:
        print("\n" + center_text("--- Table Reservation ---"))
        print(center_text("1. View Reservations"))
        if user.role == 'staff':
            print(center_text("2. Book Reservation"))
            print(center_text("3. Generate Bill / Payment"))
        if user.role == 'admin':
            print(center_text("2. Cancel Reservation"))
            print(center_text("3. Generate Bill / Payment"))
        print(center_text("0. Back to Main Menu"))
        choice = input(center_text("Select an option: "))
        if choice == '1':
            display_reservations(get_reservations())
            input(center_text("(Press Enter to continue)"))
        elif choice == '2' and user.role == 'staff':
            book_reservation(user)
            input(center_text("(Press Enter to continue)"))
        elif choice == '2' and user.role == 'admin':
            cancel_reservation()
            input(center_text("(Press Enter to continue)"))
        elif choice == '3':
            generate_reservation_bill()
            input(center_text("(Press Enter to continue)"))
        elif choice == '0':
            break
        else:
            print(center_text("Invalid choice. Please try again."))
