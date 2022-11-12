import os
import mysql.connector

# Create a connection
cnx = mysql.connector.connect(
    user='root',
    password=os.getenv('MYSQL_ROOT_PASSWORD', 'your_password'),
    host='127.0.0.1',
    database='sakila'
)

# Create a cursor with prepared=True, necessary to run prepared statements
cursor = cnx.cursor(prepared=True)

# Create the table
cursor.execute("""
    CREATE TABLE movies (
      movieID smallint AUTO_INCREMENT NOT NULL PRIMARY KEY,
      title varchar(45) DEFAULT NULL,
      duration smallint DEFAULT NULL
    );
""")

# Insert values into the table, using prepared statements
insert_stmnt = "INSERT INTO movies (title, duration) VALUES (%s, %s)"
values = [
    ('ACADEMY DINOSAUR ', 86),
    ('ACE GOLDFINGER', 48),
    ('ADAPTION HOLES', 48),
]

for value in values:
    cursor.execute(insert_stmnt, value)

# Query our new table
cursor.execute("SELECT * FROM movies")
result = cursor.fetchall()
print(result)

# Close the connection
cnx.close()
