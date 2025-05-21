import mysql.connector

# Connect to MariaDB
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Dipj@15072006"  # Set this if you use a password
)
cursor = conn.cursor()

# Create DB
cursor.execute("CREATE DATABASE IF NOT EXISTS ecommerce")
cursor.execute("USE ecommerce")

# Users Input Table
cursor.execute("""
CREATE TABLE chatbox (
    id INT AUTO_INCREMENT PRIMARY KEY,
    category VARCHAR(100),
    description VARCHAR(5000) ,
    minRange INT ,
    maxRange INT,
    image_data LONGBLOB
)
""")
print("E-commerce database and tables created successfully!")

cursor.close()
conn.close()