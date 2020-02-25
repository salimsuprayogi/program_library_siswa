# Mentor = Muhammad Nasrullah
# Author = Salim Suprayogi

# import mysql.connector
import pymysql


def connect_db():
    # fungsi connect database
    # open database connection
    db = pymysql.connect("127.0.0.1", "root", "admin", "angket")
    return db
