from patient import add_patient , view_patient

from doctor import view_doctor

from appointment import book_appointment , view_appointment

while True:
    print("\nHOSPITAL MANAGEMENT SYSTEM")
    print("1. Add Patient")
    print("2. View Patients")
    print("3. View Doctors")
    print("4. Book Appointment")
    print("5. View Appointments")
    print("6. Exit")

    choice = int(input("Enter Choice: "))

    if choice == 1:
        add_patient()

    elif choice == 2:
        view_patient()

    elif choice == 3:
        view_doctor()

    elif choice == 4:
        book_appointment()

    elif choice == 5:
        view_appointment()

    elif choice == 6:
        print("\n Thank You!\n")
        break
    else:
        print("Invalid Choice Try Again!\n")
        
