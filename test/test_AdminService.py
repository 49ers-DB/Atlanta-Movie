import pytest
import functools
import datetime
import pymysql
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from app.services.DBService import get_conn
from app.services.AdminService import AdminService


class TestAdminService(object):


    def test_Approve_User(self):
        connection = get_conn()
        i_username = 'smith_j'
        admin_service = AdminService()
        admin_service.ApproveUser(i_username)
        with connection.cursor() as cursor:
            query = "select * from user where username = 'smith_j'"
            cursor.execute(query)
            Actual = cursor.fetchall()
            connection.commit()
        connection.close()
        assert Actual[0]['status']=="Approved"


    def test_Decline_User(self):
        connection = get_conn()
        i_username = 'smith_j'
        admin_service = AdminService()
        admin_service.DeclineUser(i_username)
        with connection.cursor() as cursor:
            query = "select * from user where username = 'smith_j'"
            cursor.execute(query)
            Actual = cursor.fetchall()
            connection.commit()
        connection.close()
        assert Actual[0]['status']=="Declined"
