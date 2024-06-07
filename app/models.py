# app/models.py

import mysql.connector
from mysql.connector import errorcode
from flask import current_app

def get_db_connection():
    config = {
        'user': current_app.config['MYSQL_USER'],
        'password': current_app.config['MYSQL_PASSWORD'],
        'host': current_app.config['MYSQL_HOST'],
        'database': current_app.config['MYSQL_DB'],
    }

    try:
        cnx = mysql.connector.connect(**config)
        print("Database connection successful")
        return cnx
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
    return None