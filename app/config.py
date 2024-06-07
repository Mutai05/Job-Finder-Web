# app/config.py

import secrets

class Config:
    SECRET_KEY = secrets.token_hex(16)
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = ''
    MYSQL_HOST = 'localhost'
    MYSQL_DB = 'jobfinderweb'