import sqlite3
conn = sqlite3.connect("Hospital.db")
cur = conn.cursor()
#cur.execute("Drop table if exists Doctor")
cur.execute(
    """CREATE TABLE IF NOT EXISTS Doctor
    (id int primary key, Name varchar(10), Specialization VARCHAR(100),Phone VARCHAR(15),Fees DECIMAL(10,2)
    )"""
)
conn.commit()

cur.execute(
    """
    CREATE TABLE IF NOT EXISTS Patient
    (id int primary key , Patient_name varchar(20), age int , phone varchar(15) ,
    Doctor_id int , Foreign key (Doctor_id) references Doctor(id)
    )"""
)
conn.commit()
conn.execute("PRAGMA foreign_keys = ON")

def add_doctor():
    print("adding dr function is called")
    add_id = int(input("enter id :  "))
    add_name = input("enter name : ")
    add_speciliazation = input("enter specilization : ")
    add_phone = input("enter contact number : ")
    add_fees = int(input("enter consultancy fees : "))

    cur.execute(
        f"INSERT INTO Doctor values({add_id},'{add_name}', '{add_speciliazation}', '{add_phone}', {add_fees});"
        
    )
    conn.commit()
    print(f"{add_name} with {add_id}, has been added.")

def alter_details_doctor():
    print("What do you want to update?")
    print("1 - name")

    choice = int(input("enter your choice : "))
    doc_id = int(input("enter doctor's id : "))

    if choice == 1:
        new_name = input("enter updated name : ")
        cur.execute(f"UPDATE Doctor SET Name = '{new_name}' WHERE id = {doc_id}")
        conn.commit()

def delete_doctor():

    doc_id = int(input("enter id of doctor to be deleted : "))

    cur.execute(f"DELETE FROM Doctor WHERE id = '{doc_id}'")
    conn.commit()

def display_doctor():

    doc_id = int(input("enter doctor id that you want to see : "))

    cur.execute(f"select * from Doctor WHERE id = {doc_id}")
    print(cur.fetchone())

def add_patient():
    print("add patient")
    add_id = int(input("enter patient id : "))
    add_name = input("enter patient name : ")
    add_age = int(input("enter patient's age : "))
    add_phone = input("enter patient phone number : ")
    doc_id = int(input("Enter doctor id to assign: "))

    cur.execute(f"INSERT INTO Patient values({add_id} , '{add_name}' , {add_age}, '{add_phone}', {doc_id})")
    conn.commit()
    print("Patient details are added successfully")

def alter_patient_details():
    print("what do you want to update ? ")
    print("01 - name")
    print("02 - age")
    print("03 - phone")

    choice = int(input("enter your choice : "))
    p_id = int(input("enter patient id : "))

    if choice == 1:
        new_name = input("enter updated name : ")
        cur.execute(f"update Patient SET Patient_name = '{new_name}' WHERE id = {p_id}")

    elif choice == 2:
        updated_age = input("enter updated age : ")
        cur.execute(f"update Patient SET age = {updated_age} WHERE id = {p_id}")

    elif choice == 3:
        updated_phone = input("enter updated phone : ")
        cur.execute(f"update Patient SET phone = '{updated_phone}' WHERE id = {p_id}")

    else:
        print("invalid choice")
        return

    conn.commit()
    print("patient details are updated successfully")

def delete_patient():

    p_id = int(input("enter patient id to be deleted : "))

    cur.execute(f"DELETE FROM Patient where id = {p_id}")

    conn.commit()
    print("Patient is removed successfully")

while True:
    print("Welcome to my Hospital")
    print("0 - exit")
    print("01 - Add doctor")
    print("02 - alter doctor's details")
    print("03 - Delete doctor name")
    print("04 - Display doctor detail")
    print("05 - Add patient detail and Assign doctor to patient")
    print("06 - Update patient detail")
    print("07 - Remove patient")

    choice = int(input("Select one of these : "))

    if choice == 0:
        break
    elif choice == 1:
        add_doctor()
    elif choice == 2:
        alter_details_doctor()
    elif choice == 3:
        delete_doctor()
    elif choice == 4:
        display_doctor()
    elif choice == 5:
        add_patient()
    elif choice == 6:
        alter_patient_details()
    elif choice == 7:
        delete_patient()
    else :
        print("invalid choice")
