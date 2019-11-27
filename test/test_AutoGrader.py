import pytest
import functools
import datetime
import pymysql
import sys
import os
import json
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from app.services.DBService import get_conn, db_reset, run_s22_script
from app.services.AdminService import AdminService


class AutoGrader(object):


  def db_reset(self):

    # db_reset()
    print(True)


  def get_AutoGrading_Python_objects(self):
    # db_reset()
    # run_s22_script()
    # run_s22_script()
    # run_s22_script()

    # now the tables will be in the database.
    table_name = "magic44_table"

    table_dne_list = [31,32,33,34,36, 37, 39, 41, 43, 45, 47, 49, 50, 51, 53, 55, 57, 58, 59, 60, 61]
    with open("magic44_tables", 'w') as file:
      connection = get_conn()
      with connection.cursor() as cursor:

        for i in range(63):
          i = i + 1
          table_name_str = table_name + str(i)


          if (i not in table_dne_list):
            sql = "SELECT * FROM {}".format(table_name_str)
            cursor.execute(sql)
            data = cursor.fetchall()
            connection.commit()

            json.dump({table_name_str:data}, file, sort_keys=True, default=str)
            file.write("\n")

      connection.close()

    file.close()
