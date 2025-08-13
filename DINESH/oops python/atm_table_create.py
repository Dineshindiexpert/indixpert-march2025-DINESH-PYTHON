import mysql.connector as sql

print("DEBUG: Running updated script")

try:
    host_value = '127.0.0.1'  # Use IP, no spaces
    print(f"DEBUG: Host used for connection: '{host_value}'")

    conn = sql.connect(
        host=host_value,
        port=3306,
        user='root',
        password='1234',
        database='ATM_MACHINE',
        connection_timeout=5
    )
    print("Successfully connected")

except Exception as e:
    print("❌ Error occurred:", e)

input("Press Enter to exit...")

try:
    print(happy.")
except Exception as e:
    print(e)