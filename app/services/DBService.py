import pymysql
import os


def get_conn():
  connection = pymysql.connect(host='localhost',
                            user='flask',
                            password='1234',
                            db='moviez',
                            charset='utf8mb4',
                            port=3306,
                            cursorclass=pymysql.cursors.DictCursor)
  return connection

def db_reset():
  os.system("mysql < schema_and_initialdata.sql -u flask --password=1234")
