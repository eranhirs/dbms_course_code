import os
import mysql.connector
import time
import random

# Create a connection
cnx = mysql.connector.connect(
    user='root',
    password=os.getenv('MYSQL_ROOT_PASSWORD', 'your_password'),
    host='127.0.0.1',
    database='sakila'
)

# Set autocommit to true (this is circumstantial, think twice if you want to use this)
cnx.autocommit = True

# Create a cursor with prepared=True, necessary to run prepared statements
cursor = cnx.cursor(prepared=True)


# Create the table
cursor.execute("""
    DROP TABLE movies;
""")
cursor.execute("""
    CREATE TABLE movies (
      movieID int AUTO_INCREMENT NOT NULL PRIMARY KEY,
      title varchar(45),
      duration smallint
    );
""")

MOVIE_TITLES = ["DOWNHILL ENOUGH", "HALLOWEEN NUTS", "HANOVER GALAXY", "HAWK CHILL", "SHANGHAI TYCOON",
                "SUSPECTS QUILLS", "ACE GOLDFINGER", "HEAVEN FREEDOM", "MIDSUMMER GROUNDHOG", "NOTTING SPEAKEASY",
                "ODDS BOOGIE", "PARADISE SABRINA", "PELICAN COMFORTS", "RUSH GOODFELLAS", "STEPMOM DREAM",
                "SUNSET RACER", "VALENTINE VANISHING", "DOORS PRESIDENT", "GROSSE WONDERFUL", "HEAVENLY GUN",
                "HOOK CHARIOTS", "HURRICANE AFFAIR", "ADAPTATION HOLES", "BLUES INSTINCT", "CROSSING DIVORCE",
                "LION UNCUT", "MUPPET MILE", "NATURAL STOCK", "PILOT HOOSIERS", "SMOKING BARBARELLA", "ZORRO ARK",
                "ZORRO ARK", "CHAMPION FLATLINERS", "DEEP CRUSADE", "ENGLISH BULWORTH", "EXCITEMENT EVE",
                "FRISCO FORREST", "HALL CASSIDY", "SIMON NORTH", "CADDYSHACK JEDI", "HARPER DYING", "LUST LOCK",
                "SIDE ARK", "SPARTACUS CHEAPER", "TROJAN TOMORROW", "WESTWARD SEABISCUIT", "BENEATH RUSH",
                "CABIN FLASH", "GUMP DATE", "MAGNIFICENT CHITTY", "MOVIE SHAKESPEARE", "PRIMARY GLASS",
                "SUMMER SCARFACE", "TEQUILA PAST", "THIN SAGEBRUSH", "AIRPORT POLLOCK", "GO PURPLE", "JUGGLER HARDLY",
                "KILL BROTHERHOOD", "OCTOBER SUBMARINE", "SENSE GREEK", "COAST RAINBOW", "WOLVES DESIRE",
                "BRIDE INTRIGUE", "CUPBOARD SINNERS", "DESTINY SATURDAY", "GOODFELLAS SALUTE", "MATRIX SNOWMAN",
                "ALTER VICTORY", "CRANES RESERVOIR", "DAWN POND", "DOCTOR GRAIL", "MOSQUITO ARMAGEDDON", "NOON PAPI",
                "STORM HAPPINESS", "CLOSER BANG", "DANCES NONE", "FANTASY TROOPERS", "JEKYLL FROGMEN",
                "OKLAHOMA JUMANJI", "RINGS HEARTBREAKERS", "SUPER WYOMING", "COMMANDMENTS EXPRESS", "DAUGHTER MADIGAN",
                "HEARTBREAKERS BRIGHT"]


def get_random_movie_title_and_duration():
    """
    Returns a random movie title and duration
    """

    title = random.choice(MOVIE_TITLES)
    duration = random.choice(list(range(3000)))
    return title, duration


def insert_movies():
    start = time.time()

    for i in range(50000):
        title, duration = get_random_movie_title_and_duration()

        # Insert values into the table, using prepared statements
        insert_stmnt = "INSERT INTO movies (title, duration) VALUES (%s, %s)"
        values = (title, duration)
        cursor.execute(insert_stmnt, values)

    end = time.time()
    print(f"Time took for insert: {end - start}")


def query_movies():
    start = time.time()

    cursor.execute("SELECT * FROM movies WHERE duration BETWEEN 50 AND 100 AND title = 'HALLOWEEN NUTS' ORDER BY duration")
    result = list(cursor.fetchall())

    end = time.time()
    print(f"Time took for query: {end - start}")


# 1. Insert movies without index
print("Before index")
insert_movies()

# 2. Query movies without index
print("Before index")
query_movies()

# Truncate table
cursor.execute("""
    TRUNCATE TABLE movies; 
""")

# Add index
cursor.execute("""
    CREATE INDEX duration_index ON movies (duration); 
""")
cursor.execute("""
    CREATE INDEX title_index ON movies (title); 
""")

# 3. Insert movies with index
print("After index")
insert_movies()

# 4. Query movies without index
print("After index")
query_movies()

# Close the connection
cnx.close()
