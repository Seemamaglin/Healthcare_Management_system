import mysql.connector

# Database Connection Function
def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Seema@2004",  # Replace with your MySQL password
        database="healthcare_db"
    )

# View All Medications
def view_all_medications():
    conn = connect_db()
    cursor = conn.cursor()
    query = "SELECT * FROM medications"
    cursor.execute(query)
    medications = cursor.fetchall()
    if medications:
        for med in medications:
            print(f"ID: {med[0]}, Patient ID: {med[1]}, Name: {med[2]}, Stock: {med[3]}")
    else:
        print("No medications found.")
    conn.close()

#  Add New Medication
def add_medication():
    patient_id = int(input("Enter Patient ID: "))
    name = input("Enter Medication Name: ")
    stock = int(input("Enter Stock Quantity: "))

    conn = connect_db()
    cursor = conn.cursor()
    query = "INSERT INTO medications (patient_id, name, stock) VALUES (%s, %s, %s)"
    cursor.execute(query, (patient_id, name, stock))
    conn.commit()
    print("✅ Medication added successfully.")
    conn.close()

# Update Medication Stock
def update_medication_stock():
    medication_id = int(input("Enter Medication ID to update: "))
    new_stock = int(input("Enter New Stock Quantity: "))

    conn = connect_db()
    cursor = conn.cursor()
    query = "UPDATE medications SET stock = %s WHERE id = %s"
    cursor.execute(query, (new_stock, medication_id))
    conn.commit()
    print("✅ Medication stock updated successfully.")
    conn.close()

# Delete Medication
def delete_medication():
    medication_id = int(input("Enter Medication ID to delete: "))

    conn = connect_db()
    cursor = conn.cursor()
    query = "DELETE FROM medications WHERE id = %s"
    cursor.execute(query, (medication_id,))
    conn.commit()
    print("Medication deleted successfully.")
    conn.close()

# Main Function for Console Menu
def main():
    while True:
        print("\nMedication Management System")
        print("1 View All Medications")
        print("2 Add New Medication")
        print("3 Update Medication Stock")
        print("4 Delete Medication")
        print("5 Exit")

        choice = input("Choose an option (1-5): ")

        if choice == '1':
            view_all_medications()
        elif choice == '2':
            add_medication()
        elif choice == '3':
            update_medication_stock()
        elif choice == '4':
            delete_medication()
        elif choice == '5':
            print("Exiting Medication Management System.")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 5.")

if __name__ == "__main__":
    main()
