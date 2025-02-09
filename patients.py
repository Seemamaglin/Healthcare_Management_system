import mysql.connector

def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Seema@2004",
        database="healthcare_db"
    )

# View All Patients
def view_all_patients():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM patients")
    patients = cursor.fetchall()
    for patient in patients:
        print(f"ID: {patient[0]}, Name: {patient[1]}, Age: {patient[2]}, Conditions: {patient[3]}")
    conn.close()

# Add New Patient
def add_patient(name, age, conditions):
    conn = connect_db()
    cursor = conn.cursor()
    query = "INSERT INTO patients (name, age, conditions) VALUES (%s, %s, %s)"
    cursor.execute(query, (name, age, conditions))
    conn.commit()
    print("Patient added successfully.")
    conn.close()

# Update Patient Details
def update_patient(patient_id, name=None, age=None, conditions=None):
    conn = connect_db()
    cursor = conn.cursor()
    if name:
        cursor.execute("UPDATE patients SET name = %s WHERE id = %s", (name, patient_id))
    if age:
        cursor.execute("UPDATE patients SET age = %s WHERE id = %s", (age, patient_id))
    if conditions:
        cursor.execute("UPDATE patients SET conditions = %s WHERE id = %s", (conditions, patient_id))
    conn.commit()
    print("Patient details updated successfully.")
    conn.close()

# Delete Patient
def delete_patient(patient_id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM patients WHERE id = %s", (patient_id,))
    conn.commit()
    print("Patient deleted successfully.")
    conn.close()

# Main Function
if __name__ == "__main__":
    while True:
        print("\nPatient Management")
        print("1. View All Patients")
        print("2. Add New Patient")
        print("3. Update Patient")
        print("4. Delete Patient")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            view_all_patients()
        elif choice == "2":
            name = input("Enter name: ")
            age = int(input("Enter age: "))
            conditions = input("Enter conditions: ")
            add_patient(name, age, conditions)
        elif choice == "3":
            patient_id = int(input("Enter patient ID to update: "))
            name = input("Enter new name (leave blank to skip): ")
            age = input("Enter new age (leave blank to skip): ")
            conditions = input("Enter new conditions (leave blank to skip): ")
            update_patient(patient_id, name or None, int(age) if age else None, conditions or None)
        elif choice == "4":
            patient_id = int(input("Enter patient ID to delete: "))
            delete_patient(patient_id)
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")
