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

def add_car_and_seller_details(sell_car_data):
    print(sell_car_data)
    try:
         cursor.execute("INSERT INTO `sell_car_data` (car_brand,car_registration_year,car_model,car_variant,car_ownership,car_km_driven,seller_name,seller_contact,seller_address) values(%s,%s,%s,%s,%s,%s,%s,%s,%s)",sell_car_data)
         con.commit()
         return True
    except:
         return False
    
def register_data(admin):
        try:
           
           cursor.execute("SELECT * FROM `admin` WHERE `username`=%s AND `password`=%s",admin)
           return cursor.fetchone()
           
          
        except:
             return False    
def update_passwords(previous_data, updated_data):
    try:
        cursor.execute("SELECT * FROM `admin` WHERE `username`=%s AND `password`=%s",previous_data)
        if cursor.fetchone():
            cursor.execute("UPDATE `admin` SET `password`=%s WHERE `username`=%s",updated_data)
            con.commit()
            return True
        else:
            return False
    except:
        return False