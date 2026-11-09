import sqlite3
conn = sqlite3.connect("Hospital.db")
cur = conn.cursor()
cur.execute(
    """CREATE TABLE IF NOT EXISTS Doctor
    (id int primary key, Name varchar(10)
    )"""
)
conn.commit()

def add_doctor():
    print("adding dr function is called")
    add_id = int(input("enter id :  "))
    add_name = input("enter name : ")
    cur.execute(
        f"INSERT INTO Doctor values({add_id},'{add_name}');"
        
    )
    conn.commit()
    print(f"{add_name} with {add_id}, has been added.")

while True:
    print("Welcome to my Hospital")
    print("0 - exit")
    print("01 - Add doctor")
    print("02 - display doctor")

    choice = int(input("Select one of these : "))

    if choice == 0:
        break
    elif choice == 1:
        add_doctor()
