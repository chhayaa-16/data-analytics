import os
import sqlite3
import pandas as pd
import numpy as np

pd.set_option('display.width', 1000)
base_directory = os.path.dirname(os.path.abspath(__file__))
db_file = os.path.join( base_directory, "Sales_Analytical_Report.db")
xl_file = os.path.join( base_directory, "Sales_Analytical_Report.xlsx")

for i in db_file, xl_file:
    if os.path.exists(i):
        os.remove(i)
print("Database Initialized...")

conn = sqlite3.connect(db_file)
cursor = conn.cursor()
cursor.execute("PRAGMA foreign_keys= ON; " )

cursor.execute("""
    CREATE TABLE IF NOT EXISTS Customers
    (
        Customer_ID INTEGER PRIMARY KEY AUTOINCREMENT, 
        Customer_Name TEXT NOT NULL,
        Email TEXT UNIQUE NOT NULL,
        City TEXT NOT NULL,
        Tier TEXT CHECK(Tier IN ('Bronze', 'Silver', 'Gold', 'Platinum')) DEFAULT 'Bronze'
    );
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS Products
    (
        Product_ID INTEGER PRIMARY KEY AUTOINCREMENT,
        Product_Name TEXT NOT NULL,
        Category TEXT NOT NULL,
        Unit_Price REAL CHECK(Unit_Price >= 0) NOT NULL
    );
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS Orders
    (
        Order_ID INTEGER PRIMARY KEY AUTOINCREMENT, 
        Quantity INTEGER CHECK(Quantity >= 30) NOT NULL,
        Order_Date TEXT NOT NULL,
        Customer_ID INTEGER NOT NULL,
        Product_ID INTEGER NOT NULL,
        FOREIGN KEY (Customer_ID) REFERENCES Customers (Customer_ID) ON DELETE CASCADE,
        FOREIGN KEY (Product_ID) REFERENCES Products (Product_ID) ON DELETE CASCADE
    );
""")




conn.commit()
print("Tables Created Successfully...")



cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name NOT LIKE 'sqlite_%';")


tables_in_db = [row[0] for row in cursor.fetchall()]

for i in tables_in_db :
    print(f"we found {i}")




customer_details = [
    ("abc", "abc@gmail.com", "NSK", "Gold"),
    ("xyz", "xyz@gmail.com", "PUNE", "Platinum"),
    ("pre", "pre@gmail.com", "DELHI", "Platinum"),
    ("nit", "nit@gmail.com", "pune", "Silver"),
    ("cma", "cma@gmail.com", "thane", "Silver")
]

                

customer_sql ="""


    INSERT INTO customers (Customer_name,Email,City,Tier)
      VALUES (?,?,?,?);

      

  """

cursor.executemany(customer_sql,customer_details)
conn.commit()
