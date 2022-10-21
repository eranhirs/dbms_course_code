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


# Example #1: Valid input from user
input_from_user = "2"
query = "SELECT * FROM customer WHERE customer_id = " + input_from_user
cursor.execute(query)
result = cursor.fetchall()

print()
print("Example #1")
print(f"The user input was \"{input_from_user}\", here are the results:")
print(result)


# Example #2: SQL Injection attempt by user
input_from_user = "2 OR 1=1"
query = "SELECT * FROM customer WHERE customer_id = " + input_from_user
cursor.execute(query)
result = cursor.fetchall()

print()
print("Example #2")
print(f"The user input was \"{input_from_user}\", here are the results:")
print(result)


# Example #3: Blocking the SQL Injection attempt by user
input_from_user = "2 OR 1=1"
query = "SELECT * FROM customer WHERE customer_id = %s"
cursor.execute(query, [input_from_user])
result = cursor.fetchall()

print()
print("Example #3")
print(f"The user input was \"{input_from_user}\", here are the results:")
print(result)


# Close the connection
cnx.close()
