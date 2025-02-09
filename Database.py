import mysql.connector

# Connect to MySQL
conn = mysql.connector.connect(
    host='localhost',
    user='root',       
    password='Seema@2004',  
    database='healthcare_db'
)
cursor = conn.cursor()

print("Database connected successfully!")
