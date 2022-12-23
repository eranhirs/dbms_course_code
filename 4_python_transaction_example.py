import mysql.connector

### ATTENTION! Running this code will make changes on your Sakila dataset. Please be careful ###

# Create a connection
cnx = mysql.connector.connect(
    user='username',
    password='password',
    host='127.0.0.1',
    database='sakila'
)

# Create a cursor
cursor = cnx.cursor()

try:
    # Start transaction
    cnx.start_transaction()
    
    # Execute the SQL command
    cursor.execute('UPDATE film SET rental_rate = rental_rate + rental_rate*0.2')
    cnx.commit()

except:
    # Rollback in case there is any error
    cnx.rollback()

# Disconnect from server
cnx.close()
