import json
import requests
import mysql.connector
import config
from mysql.connector import errorcode

DB_NAME = 'yelp_tea'

cnx = mysql.connector .connect(
    host = config.host,
    user = config.user,
    passwd = config.password,
    database = DB_NAME,
    use_pure=True
)

cursor = cnx.cursor()


def create_database(cursor, database):
    try:
        cursor.execute(
            "CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(database))
    except mysql.connector.Error as err:
        print("Failed creating database: {}".format(err))
        exit(1)

#create_database(cursor, DB_NAME)


TABLES = {}
TABLES['yelp_businesses'] = ("""
     CREATE TABLE yelp_businesses (
      business_id varchar(22) NOT NULL,
      name varchar(50) NOT NULL,
      price varchar(4),
      rating decimal(3,2),
      review_count int(22),
      PRIMARY KEY (business_id)
    ) ENGINE=InnoDB""")

TABLES['yelp_reviews'] = ("""
     CREATE TABLE yelp_reviews (
     review_id varchar(22) NOT NULL,
     business_id varchar(22) NOT NULL,
     reviews text(1000),
     time_created varchar(20),
     PRIMARY KEY (review_id),
     FOREIGN KEY (business_id) REFERENCES yelp_businesses(business_id)
    ) ENGINE=InnoDB""")

for table_name in TABLES:
    table_description = TABLES[table_name]
    try:
        print("Creating table {}: ".format(table_name), end='')
        cursor.execute(table_description)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
            print("already exists.")
        else:
            print(err.msg)
    else:
        print("OK")

cursor.close()
cnx.close()
