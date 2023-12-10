import mysql.connector

# Establish a connection to the database


def create_connection():
    connection = mysql.connector.connect(
        host="ecommerce.ch0s2ra5njdh.us-east-2.rds.amazonaws.com",
        user="admin",
        password="admin123",
        database="ecommerce"
    )
    return connection


connection = create_connection()
print(connection)

# Select records


cursor = connection.cursor()
cursor.execute("SELECT * FROM predictions limit 10")
rows = cursor.fetchall()
for row in rows:
    print(row)
