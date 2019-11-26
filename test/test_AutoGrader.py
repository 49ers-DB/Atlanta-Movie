import pytest
import functools
import datetime
import pymysql
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from app.services.DBService import get_conn, db_reset
from app.services.AdminService import AdminService


class TestAutoGrader(object):


  def test_AutoGrading_TA(self):

    db_reset()



