import mysql.connector

try:
    print("Testing MySQL connection...")
    conn = mysql.connector.connect(host='localhost', user='root', password='1234')
    print("MySQL connection successful.")
    conn.close()
except Exception as e:
    print("MySQL connection failed:", e)

input("Press Enter to exit...")  # <-- This keeps window open
