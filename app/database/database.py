import os
import mysql.connector
from loguru import logger

from dotenv import load_dotenv
load_dotenv()

con = mysql.connector.connect(
    port=os.getenv("DB_PORT"),
    host=os.getenv("DB_HOST"),
    user=os.getenv("DB_USER"),
    passwd=os.getenv("DB_PASSWORD"),
    database=os.getenv("DB_NAME")
)

cursor = con.cursor()
logger.info("Database Connected")

# ADMIN LOGIN   
def register_data(admin):
    try:
        cursor.execute("SELECT * FROM `admin` WHERE `username`=%s AND `password`=%s LIMIT 1", admin)
        return cursor.fetchone()
    except Exception as e:
        logger.error(f"Error in register_data: {e}")
        return False

# ADMIN PASSWORD UPDATE   
def update_passwords(previous_data, updated_data):
    try:
        cursor.execute("UPDATE `admin` SET `password`=%s WHERE `username`=%s AND `password`=%s", (updated_data[0], previous_data[0], previous_data[1]))
        con.commit()
        return cursor.rowcount > 0
    except Exception as e:
        logger.error(f"Error in update_passwords: {e}")
        return False

# BUY CAR PAGE   
def get_cars():
    cursor.execute("SELECT * FROM `instock_cars_data`")
    return cursor.fetchall()

# BRAND NEW CARS TREEVIEW  
def add_brand_new_cars(new_car_data):
    try:
        cursor.execute("INSERT INTO `brand_new_cars_data` VALUES (NULL, %s, %s, %s, %s, %s, %s)", new_car_data)
        con.commit()
        return True
    except Exception as e:
        logger.error(f"Error in add_brand_new_cars: {e}")
        return False

def get_brand_new_cars():
    try:
        cursor.execute("SELECT * FROM `brand_new_cars_data`")
        return cursor.fetchall()
    except Exception as e:
        logger.error(f"Error in get_brand_new_cars: {e}")
        return []

def delete_brand_new_cars(car_id):
    try:
        cursor.execute("DELETE FROM `brand_new_cars_data` WHERE `id`=%s", (car_id,))
        con.commit()
        return cursor.rowcount > 0
    except Exception as e:
        logger.error(f"Error in delete_brand_new_cars: {e}")
        return False

def update_new_cars(car_data):
    try:
        cursor.execute("UPDATE `brand_new_cars_data` SET car_type=%s, car_brand=%s, car_model=%s, car_variant=%s, car_mileage=%s, car_price=%s WHERE id=%s", car_data)
        con.commit()
        return cursor.rowcount > 0
    except Exception as e:
        logger.error(f"Error in update_new_cars: {e}")
        return False

def add_in_stock(car_details):
    try:
        cursor.execute("INSERT INTO `instock_cars_data` VALUES (NULL, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", car_details)
        con.commit()
        return True
    except Exception as e:
        logger.error(f"Error in add_in_stock: {e}")
        return False

# SECOND HAND CARS BOUGHT (SELL CAR)  
def add_car_and_seller_details(sell_car_data):
    try:
        cursor.execute("INSERT INTO `secondhand_cars_bought_data` VALUES (NULL, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", sell_car_data)
        con.commit()
        return True
    except Exception as e:
        logger.error(f"Error in add_car_and_seller_details: {e}")
        return False

def get_car_and_seller_details():
    try:
        cursor.execute("SELECT * FROM `secondhand_cars_bought_data`")
        return cursor.fetchall()
    except Exception as e:
        logger.error(f"Error in get_car_and_seller_details: {e}")
        return []

def delete_car_and_seller_details(car_id):
    try:
        cursor.execute("DELETE FROM `secondhand_cars_bought_data` WHERE id=%s", (car_id,))
        con.commit()
        return cursor.rowcount > 0
    except Exception as e:
        logger.error(f"Error in delete_car_and_seller_details: {e}")
        return False

def update_car_and_seller_details(update_car_data):
    try:
        cursor.execute("UPDATE `secondhand_cars_bought_data` SET car_type=%s, car_brand=%s, car_model=%s, car_variant=%s, car_km_driven=%s, car_registration_year=%s, car_ownership=%s, seller_name=%s, seller_contact=%s, seller_address=%s, car_price=%s WHERE id=%s", update_car_data)
        con.commit()
        return cursor.rowcount > 0
    except Exception as e:
        logger.error(f"Error in update_car_and_seller_details: {e}")
        return False

def manage_cars_stock():
    cursor.execute("SELECT * FROM `instock_cars_data` WHERE `is_sold`='NO'")
    return cursor.fetchall()

def sold_car(sold_car_details):
    try:
        cursor.execute("UPDATE `instock_cars_data` SET `is_sold`=%s WHERE `id`=%s", sold_car_details)
        con.commit()
        return cursor.rowcount > 0
    except Exception as e:
        logger.error(f"Error in sold_car: {e}")
        return False

def show_all_sold_cars_details():
    try:
        cursor.execute("SELECT * FROM `instock_cars_data` WHERE `is_sold`='YES'")
        return cursor.fetchall()
    except Exception as e:
        logger.error(f"Error in show_all_sold_cars_details: {e}")
        return []

# CAR SERVICES  
def add_car_services_details(car_service_data):
    try:
        cursor.execute("INSERT INTO `car_services` VALUES (NULL, %s, %s, %s, %s, %s)", car_service_data)
        con.commit()
        return True
    except Exception as e:
        logger.error(f"Error in add_car_services_details: {e}")
        return False

def get_car_services_details():
    try:
        cursor.execute("SELECT * FROM `car_services`")
        return cursor.fetchall()
    except Exception as e:
        logger.error(f"Error in get_car_services_details: {e}")
        return []

def delete_car_services_data(service_id):
    try:
        cursor.execute("DELETE FROM `car_services` WHERE id=%s", (service_id,))
        con.commit()
        return cursor.rowcount > 0
    except Exception as e:
        logger.error(f"Error in delete_car_services_data: {e}")
        return False

def update_car_services_details(updated_services_data):
    try:
        cursor.execute("UPDATE `car_services` SET service_type=%s, service_time=%s, service_date=%s, customer_name=%s, customer_contact=%s WHERE id=%s", updated_services_data)
        con.commit()
        return cursor.rowcount > 0
    except Exception as e:
        logger.error(f"Error in update_car_services_details: {e}")
        return False







# def delete_cars(car_id):
#     logger("Database: car id ", car_id)
#     cursor.execute("DELETE FROM `brand_new_cars_data` WHERE id=%s",car_id)
#     con.commit()
#     return True

# def manage_new_cars():
#     cursor.execute("SELECT *FROM `new_cars_data`")
#     return cursor.fetchall()

# def manage_used_cars():
#     cursor.execute("SELECT *FROM `used_cars_data`")
#     return cursor.fetchall()

# def delete_cars_stock(car_id):
#     logger("Database: car id ", car_id)
#     cursor.execute("DELETE FROM `cars_data` WHERE id=%s",car_id)
#     con.commit()
#     return True

# def delete_new_cars(car_id):
#     logger("Database: car id ", car_id)
#     cursor.execute("DELETE FROM `new_cars_data` WHERE id=%s",car_id)
#     con.commit()
#     return True

# def delete_used_cars(car_id):
#     logger("Database: car id ", car_id)
#     cursor.execute("DELETE FROM `used_cars_data` WHERE id=%s",car_id)
#     con.commit()
#     return True