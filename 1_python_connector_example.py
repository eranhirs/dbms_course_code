import os
import mysql.connector

# Create a connection
cnx = mysql.connector.connect(
    user='root',
    password=os.getenv('MYSQL_ROOT_PASSWORD', 'your_password'),
    host='127.0.0.1',
    database='sakila'
)

# Create a cursor
cursor = cnx.cursor()


# Example #1 - fetchall()
cursor.execute("SELECT * FROM customer;")
result = cursor.fetchall()

print()
print("Example #1 - Here are the \"fetchall()\" results:")
print(result)


# Example #2 - fetchone()
cursor.execute("SELECT * FROM customer LIMIT 4;")
result = cursor.fetchone()

print()
print("Example #2 - Here are the \"fetchone()\" results:")
while result is not None:
    print(result)
    result = cursor.fetchone()


# Example #3 - fetchmany(5)
cursor.execute("SELECT * FROM customer;")
result = cursor.fetchmany(5)

print()
print("Example #3 - Here are the \"fetchmany(5)\" results:")
print(result)


# Close the connection
cnx.close()
