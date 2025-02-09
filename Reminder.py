import mysql.connector

# Database Connection Function
def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Seema@2004",
        database="healthcare_db"
    )

# View All Reminders
def view_all_reminders():
    conn = connect_db()
    cursor = conn.cursor()
    query = "SELECT * FROM reminders"
    cursor.execute(query)
    reminders = cursor.fetchall()
    for reminder in reminders:
        print(f"ID: {reminder[0]}, Medication ID: {reminder[1]}, Time: {reminder[2]}")
    conn.close()

# Add New Reminder
def add_reminder(medication_id, reminder_time):
    conn = connect_db()
    cursor = conn.cursor()
    query = "INSERT INTO reminders (medication_id, reminder_time) VALUES (%s, %s)"
    cursor.execute(query, (medication_id, reminder_time))
    conn.commit()
    print("Reminder added successfully.")
    conn.close()

# Update Reminder Time
def update_reminder(reminder_id, new_time):
    conn = connect_db()
    cursor = conn.cursor()
    query = "UPDATE reminders SET reminder_time = %s WHERE id = %s"
    cursor.execute(query, (new_time, reminder_id))
    conn.commit()
    print("Reminder updated successfully.")
    conn.close()

#  Delete Reminder
def delete_reminder(reminder_id):
    conn = connect_db()
    cursor = conn.cursor()
    query = "DELETE FROM reminders WHERE id = %s"
    cursor.execute(query, (reminder_id,))
    conn.commit()
    print("Reminder deleted successfully.")
    conn.close()

# Main Function
def main():
    while True:
        print("\n--- Reminder Management ---")
        print("1. View All Reminders")
        print("2. Add New Reminder")
        print("3. Update Reminder")
        print("4. Delete Reminder")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            view_all_reminders()
        elif choice == '2':
            med_id = int(input("Enter Medication ID: "))
            time = input("Enter Reminder Time (HH:MM:SS): ")
            add_reminder(med_id, time)
        elif choice == '3':
            reminder_id = int(input("Enter Reminder ID to update: "))
            new_time = input("Enter new Reminder Time (HH:MM:SS): ")
            update_reminder(reminder_id, new_time)
        elif choice == '4':
            reminder_id = int(input("Enter Reminder ID to delete: "))
            delete_reminder(reminder_id)
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
