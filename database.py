import mysql.connector

con = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "",
    database = "carObar"
)

cursor = con.cursor()

print("Database Connected")




#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! Treeview for brand new cars !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!11

def add_brand_new_cars(new_car_data):
    
    try:
        cursor.execute("INSERT INTO `brand_new_cars_data` (car_brand,car_model,car_variant,car_mileage,car_price) values(%s,%s,%s,%s,%s)",new_car_data)
        con.commit()
        return True
    except:
        return False


def update_new_cars(car_id):
    print()
    try:
        cursor.execute("UPDATE `brand_new_cars_data` SET car_brand=%s,car_model=%s,car_variant=%s,car_mileage=%s,car_price=%s WHERE id=%s",car_id)  #?????????????????????????? for updating 
        con.commit()
        return True
    except:
        return False


def delete_new_cars(car_id):
    print("Database: car id ", car_id)
    cursor.execute("DELETE FROM `brand_new_cars_data` WHERE id=%s",car_id)
    con.commit()
    return True


#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! CAR SERVICES !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

def add_car_services_details(car_service_data):
    try:
        cursor.execute("INSERT INTO `car_services` (service_type,service_time,service_date,customer_name,customer_contact) values(%s,%s,%s,%s,%s)",car_service_data)
        con.commit()
        return True
    except:

        return False        

def get_car_services_details():
    cursor.execute("SELECT *FROM `car_services`")
    return cursor.fetchall()

def delete_car_services_data(service_id):
    cursor.execute("DELETE FROM `car_services` WHERE id=%s", service_id)
    con.commit()
    return True

def update_car_services_details(updated_services_data):
    print("Database: updated student data - ", updated_services_data)
    try:
        cursor.execute("UPDATE `car_services` SET `service_type`=%s,`service_time`=%s,`service_date`=%s,`customer_name`=%s,`customer_contact`=%s WHERE `id`=%s",updated_services_data)
        con.commit()
        return True
    except:
        return False
    

#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! SECOND HAND CARS BOUGHT (SELL CAR) !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

def add_car_and_seller_details(sell_car_data):
    print(sell_car_data)
    try:
        cursor.execute("INSERT INTO `secondhand_cars_bought_data` (car_brand,car_registration_year,car_model,car_variant,car_ownership,car_km_driven,car_price,seller_name,seller_contact,seller_address) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",sell_car_data)
        con.commit()
        return True
    except:
        return False

def update_car_and_seller_details(update_car_data):
    try:
        cursor.execute("UPDATE `secondhand_cars_bought_data` (car_brand,car_registration_year,car_model,car_variant,car_ownership,car_km_driven,car_price,seller_name,seller_contact,seller_address,car_price) values(%s,%s,%s,%s,%s,%s,%s,%s,%s)",update_car_data)
        con.commit()
        return True
    except:
        return False    
    
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! ADMIN LOGIN !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!    
    
def register_data(admin):
        try:
        
            cursor.execute("SELECT * FROM `admin` WHERE `username`=%s AND `password`=%s",admin)
            return cursor.fetchone()
        
        
        except:
            return False    
        
        
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! UPDATE PASSWORD !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        
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

#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! BRAND NEW CAR !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!


def manage_brand_new_cars():
    cursor.execute("SELECT *FROM `brand_new_cars_data`")
    return cursor.fetchall()

def delete_cars(car_id):
    print("Database: car id ", car_id)
    cursor.execute("DELETE FROM `brand_new_cars_data` WHERE id=%s",car_id)
    con.commit()
    return True













def manage_new_cars():
    cursor.execute("SELECT *FROM `new_cars_data`")
    return cursor.fetchall()

def manage_used_cars():
    cursor.execute("SELECT *FROM `used_cars_data`")
    return cursor.fetchall()



def manage_cars_stock():
    cursor.execute("SELECT *FROM `instock_cars_data`")
    return cursor.fetchall()

def delete_cars_stock(car_id):
    print("Database: car id ", car_id)
    cursor.execute("DELETE FROM `cars_data` WHERE id=%s",car_id)
    con.commit()
    return True

def delete_new_cars(car_id):
    print("Database: car id ", car_id)
    cursor.execute("DELETE FROM `new_cars_data` WHERE id=%s",car_id)
    con.commit()
    return True

def delete_used_cars(car_id):
    print("Database: car id ", car_id)
    cursor.execute("DELETE FROM `used_cars_data` WHERE id=%s",car_id)
    con.commit()
    return True



def get_cars(car_id):
    cursor.execute("SELECT * From `instock_cars_data`")
    return cursor.fetchall()



    # (car_brand,car_registration_year,car_model,car_variant,car_ownership,car_km_driven,seller_name,seller_contact,seller_address) values(%s,%s,%s,%s,%s,%s,%s,%s,%s)",sell_car_data)