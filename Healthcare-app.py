from patients import view_all_patients, add_patient, update_patient, delete_patient
from Medications import view_all_medications, add_medication, update_medication_stock, delete_medication
from Reminder import view_all_reminders, add_reminder, update_reminder,delete_reminder

def main():
    while True:
        print("\n Healthcare Management System")
        print("1. Manage Patients")
        print("2. Manage Medications")
        print("3. Manage Reminders")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            print("\n1 View Patients\n2 Add Patient\n3 Update Patient\n4 Delete Patient")
            patient_choice = input("Choose an option: ")
            if patient_choice == '1':
                view_all_patients()
            elif patient_choice == '2':
                name = input("Enter Name: ")
                age = int(input("Enter Age: "))
                conditions = input("Enter Conditions: ")
                add_patient(name, age, conditions)
            elif patient_choice == '3':
                patient_id = int(input("Enter Patient ID: "))
                name = input("Enter New Name: ")
                age = int(input("Enter New Age: "))
                conditions = input("Enter New Conditions: ")
                update_patient(patient_id, name, age, conditions)
            elif patient_choice == '4':
                patient_id = int(input("Enter Patient ID to Delete: "))
                delete_patient(patient_id)

        elif choice == '2':
            print("\n1 View Medications\n2 Add Medication\n3 Update Stock\n4 Delete Medication")
            med_choice = input("Choose an option: ")
            if med_choice == '1':
                view_all_medications()
            elif med_choice == '2':
                patient_id = int(input("Enter Patient ID: "))
                name = input("Enter Medication Name: ")
                stock = int(input("Enter Stock Quantity: "))
                add_medication(patient_id, name, stock)
            elif med_choice == '3':
                medication_id = int(input("Enter Medication ID: "))
                new_stock = int(input("Enter New Stock: "))
                update_medication_stock(medication_id, new_stock)
            elif med_choice == '4':
                medication_id = int(input("Enter Medication ID to Delete: "))
                delete_medication(medication_id)

        elif choice == '3':
            print("\n1 View Reminders\n2 Set Reminder\n3 Delete Reminder")
            reminder_choice = input("Choose an option: ")
            if reminder_choice == '1':
                view_all_reminders()
            elif reminder_choice == '2':
                medication_id = int(input("Enter Medication ID: "))
                reminder_time = input("Enter Reminder Time (HH:MM:SS): ")
                update_reminder(medication_id, reminder_time)
            elif reminder_choice == '3':
                reminder_id = int(input("Enter Reminder ID to Delete: "))
                delete_reminder(reminder_id)

        elif choice == '4':
            print("Exiting the system. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
