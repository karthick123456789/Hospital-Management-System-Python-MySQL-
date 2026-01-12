from db import get_connection

def add_patient():

    name = input("Enter Name: ")
    age = int(input("Enter age: "))
    disease = input("Enter Disease: ")

    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        "Insert Into patients (name,age,disease) values (%s,%s,%s)",
        (name,age,disease)
    )

    conn.commit()
    conn.close()

    print("\nPatient Add Successfully")

def view_patient():

    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        "select * from Patients",
    )

    print("\nId | Name      | Age  | Disease ")
    print("-"*30)

    for row in cur.fetchall():
        print(row)

    conn.close()
