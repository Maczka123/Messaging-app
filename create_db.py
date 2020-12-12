from psycopg2 import connect, OperationalError
from psycopg2.errors import DuplicateDatabase, DuplicateTable


CREATE_DATABASE = f"CREATE DATABASE project_db"

CREATE_TABLE_USERS = f"""CREATE TABLE users(
                    id serial PRIMARY KEY,
                    username varchar(255) UNIQUE NOT NULL,
                    hashed_password varchar(80) NOT NULL)"""

CREATE_TABLE_MESSAGES = f"""CREATE TABLE messages(
                       id serial PRIMARY KEY,
                       from_id int,
                       to_id int,
                       creation_date timestamp DEFAULT now(),
                       FOREIGN KEY (from_id) REFERENCES users(id) ON DELETE CASCADE, 
                       FOREIGN KEY (to_id) REFERENCES users(id) ON DELETE CASCADE )"""

USER = "postgres"
HOST = "localhost"
PASSWORD = "coderslab"

try:
    cnx = connect(user=USER, password=PASSWORD, host=HOST)
    cnx.autocommit = True
    cursor = cnx.cursor()
    try:
        cursor.execute(CREATE_DATABASE)
        print("Database created successfully.")
    except DuplicateDatabase as ex:
        print("Chosen database name exists.", ex)
    cnx.close()
except OperationalError as ex:
    print(ex)

try:
    cnx = connect(user=USER, password=PASSWORD, host=HOST, database="project_db")
    cnx.autocommit = True
    cursor = cnx.cursor()
    try:
        cursor.execute(CREATE_TABLE_USERS)
        print("Table users created successfully.")
    except DuplicateDatabase as ex:
        print(ex)
    try:
        cursor.execute(CREATE_TABLE_MESSAGES)
        print("Table messages created successfully.")
    except DuplicateDatabase as ex:
        print(ex)
except OperationalError as ex:
    print(ex)