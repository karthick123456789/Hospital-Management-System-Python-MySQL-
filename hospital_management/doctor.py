from db import get_connection

def view_doctor():

    conn = get_connection()

    cur = conn.cursor()

    cur.execute(
        'select * from doctors'
    )

    print("\nID | Name       | Specialization")
    print("-"*30)

    for row in cur.fetchall():
        print(row)

    conn.close()
    
