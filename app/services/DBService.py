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
  os.system("mysql < schema_and_initialdata.sql -u flask --password=1234 > output.txt")
  os.system("mysql < procedures.sql -u flask --password=1234")

def run_s22_script():

  os.system("mysql < 'CS4400 Fall2019 s22 Self_Testing_Script_v2.sql' -u flask --password=1234 > output.txt")

