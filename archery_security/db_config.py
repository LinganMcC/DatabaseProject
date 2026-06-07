import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="archer_user",
        password="StrongPassword1!",
        database="archer_database"
    )
