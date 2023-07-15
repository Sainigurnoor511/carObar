import mysql.connector

con = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "",
    database = "carObar"
)

cursor = con.cursor()

print("Database Connected")

def display_new_car():
    cursor.execute("SELECT *FROM `new_cars`")
    return cursor.fetchall()

def display_used_car():
    cursor.execute("SELECT *FROM `used_cars`")
    return cursor.fetchall()
