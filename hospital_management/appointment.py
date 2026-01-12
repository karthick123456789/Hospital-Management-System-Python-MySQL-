from db import get_connection

def book_appointment():

    patient_id = int(input("Enter Patient_id: "))
    doctor_id = int(input("Enter Doctor_id: "))
    date = input("Enter Appointment Date (YYYY-MM-DD): ")

    con = get_connection()
    cur = con.cursor()
    cur.execute(
        'insert into appointments (patient_id,doctor_id,date) values (%s,%s,%s)',
        (patient_id,doctor_id,date)
    )
    print("\nSuccessfully Book Appointment")

    con.commit()
    con.close()

def view_appointment():

    con = get_connection()
    cur = con.cursor()
    cur.execute(
        """select a.id, p.name, d.name, a.date
        from appointments a
        JOIN patients p ON a.patient_id = p.id
        JOIN doctors d ON a.doctor_id = d.id
    """)

    print("\nID | Patient_Name | Doctor_Name |           Date         ")
    print("-"*60)

    for row in cur.fetchall():
        print(row)

    con.close()
    
