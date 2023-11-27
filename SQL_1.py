import sqlite3
import time

def create_table(table_name, item):
    with sqlite3.connect(db_name) as con:
        cur = con.cursor()
        time.sleep(0.5)
        print("Creating a Table...")
        command = f"CREATE TABLE IF NOT EXISTS {table_name}({item});"
        cur.execute(command)
        time.sleep(1)
        print("Done!")

def drop_table(table_name):
    with sqlite3.connect(db_name) as con:
        cur = con.cursor()
        command = f"DROP TABLE IF EXISTS {table_name};"
        time.sleep(0.5)
        print("Deleting...")
        cur.execute(command)
        time.sleep(1)
        print("Done!")

def insert_to_table(table_name, item):
    with sqlite3.connect(db_name) as con:
        cur = con.cursor()
        command = f"INSERT INTO {table_name} VALUES ('{item}');"
        time.sleep(0.5)
        print('Inserting...')
        time.sleep(1)
        cur.execute(command)
        print("Done!")

def select_show_all(table_name):
    with sqlite3.connect(db_name) as con:
        cur = con.cursor()
        command = f"SELECT * FROM {table_name};"
        cur.execute(command)
        records = cur.fetchall()
        for i in records:
            print(i[0])

# ---------------------------------------------
db_name = input("Enter DB name to start (type it with .db format): ")

time.sleep(0.5)
print("Choose Your Option:\n1.Exit\n2.Add a Table\n3.Delete a Table\n4.Insert items to Table\n5.Show Table\nChoose your options wisely")
# ----------------------------------------------
def start_app(answer):
    time.sleep(1)
    while answer != '1':
        if answer == '2':
            create_table(input("Enter your Table name: "), input("Enter your Table item name: "))
        elif answer == '3':
            drop_table(input("Enter your Table name to delete: "))
        elif answer == '4':
            insert_to_table(input("Enter your Table name to insert: "), input("Enter your item to add: "))
        elif answer == '5':
            select_show_all(input("Enter your Table name to show: "))
        answer = input("Enter Option: ")
    print("Done!")

start_app(input("Choose Ur option: "))
