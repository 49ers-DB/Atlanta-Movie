import pytest
import functools
import datetime
import dateutil.parser

import pymysql
import sys
import os
import json
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.services.DBService import get_conn
from app.services.RegisterService import RegisterService
from app.services.DBService import db_reset, get_conn

def test_register_user():
  db_reset()
  register_service = RegisterService()
  user= {'username':"andrw",
    'firstname':"andy",
    'lastname':"yang",
    'password':"googlecom"
  }
  register_service.registerUser(user)

  connection = get_conn()
  with connection.cursor() as cursor:
    cursor.execute("SELECT * FROM USER where username='andrw' ")
    data = cursor.fetchall()
  connection.commit()
  connection.close()

  assert data[0]['lastname'] == 'yang'


def test_customer_only_register():
  db_reset()
  register_service = RegisterService()
  user= {'username':"andrw",
    'firstname':"andy",
    'lastname':"yang",
    'password':"googlecom",
    'creditCardsList': [
      '3434492893921019',
      '3434492893921018'
    ]
  }
  resp = register_service.registerCustomer(user)
  print(resp)

  connection = get_conn()
  with connection.cursor() as cursor:
    cursor.execute("SELECT * FROM USER where username='andrw' ")
    data = cursor.fetchall()
  connection.commit()

  assert data[0]['lastname'] == 'yang'

  with connection.cursor() as cursor:
    cursor.execute("SELECT * FROM CUSTOMER where username='andrw' ")
    data = cursor.fetchall()
  connection.commit()

  assert data[0]['username'] == 'andrw'

  with connection.cursor() as cursor:
    cursor.execute("SELECT * FROM CustomerCreditCard where username = 'andrw'")
    data = cursor.fetchall()
  connection.commit()
  print(data)

  assert len(data) == 2

def test_manager_only_register():
  db_reset()
  register_service = RegisterService()
  
  user= {'username':"andrw",
    'firstname':"andy",
    'lastname':"yang",
    'password':"googlecom",
    'selectedCompany':{'value':'EZ Theater Company'},
    'address':"4000 so st",
    'city':"sometown",
    'selectedState':{'value':"GA"},
    'zipCode':'20202'
  }
  register_service.registerManager(user)

  connection = get_conn()
  with connection.cursor() as cursor:
    cursor.execute("SELECT * FROM USER where username='andrw' ")
    data = cursor.fetchall()
  connection.commit()

  assert data[0]['lastname'] == 'yang'

  with connection.cursor() as cursor:
    cursor.execute("SELECT * FROM Manager where username='andrw' ")
    data = cursor.fetchall()
  connection.commit()

  assert data[0]['username'] == 'andrw'


def test_manager_customer_register():
  db_reset()
  register_service = RegisterService()
  user= {'username':"andrw",
    'firstname':"andy",
    'lastname':"yang",
    'password':"googlecom",
    'creditCardsList': [
      '3434492893921019',
      '3434492893921018'
    ],
    'selectedCompany':{'value':'EZ Theater Company'},
    'address':"4000 so st",
    'city':"sometown",
    'selectedState':{'value':"GA"},
    'zipCode':'20202'
  }
  resp = register_service.registerManagerCustomer(user)

  connection = get_conn()
  with connection.cursor() as cursor:
    cursor.execute("SELECT * FROM USER where username='andrw' ")
    data = cursor.fetchall()
  connection.commit()

  assert data[0]['lastname'] == 'yang'

  with connection.cursor() as cursor:
    cursor.execute("SELECT * FROM CUSTOMER where username='andrw' ")
    data = cursor.fetchall()
  connection.commit()

  assert data[0]['username'] == 'andrw'

  with connection.cursor() as cursor:
    cursor.execute("SELECT * FROM CustomerCreditCard where username = 'andrw'")
    data = cursor.fetchall()
  connection.commit()
  print(data)

  assert len(data) == 2

  with connection.cursor() as cursor:
    cursor.execute("SELECT * FROM Manager where username='andrw' ")
    data = cursor.fetchall()
  connection.commit()

  assert data[0]['username'] == 'andrw'