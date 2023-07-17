import mysql.connector

con = mysql.connector.connect(
    host = "localhost" ,
    user = "root",
    passwd = "",
    database = "carobar"
    )
cursor = con.cursor()
print("Database Connected")

def add_car_and_seller_details(sell_car_data):
    print(sell_car_data)
    try:
         cursor.execute("INSERT INTO `sell_car_data` (car_brand,car_registration_year,car_model,car_variant,car_ownership,car_km_driven,seller_name,seller_contact,seller_address) values(%s,%s,%s,%s,%s,%s,%s,%s,%s)",sell_car_data)
         con.commit()
         return True
    except:
         return False
