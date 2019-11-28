import pytest
import functools
import datetime
import pymysql
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from app.services.DBService import get_conn, db_reset
from app.services.LoginService import LoginService



def test_Login():
  db_reset()
  login_service = LoginService()
  username = 'calcwizard'
  password =  '222222222'
  user = {"username":username, "password":password}
  result = login_service.login(user)

  expected = [{"isAdmin": 0, "isCustomer": 1, "isManager": 0, "status": "Approved", "username": "calcwizard"}]

  assert result == expected






