import pytest
import functools
import datetime
import pymysql
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from app.services.DBService import get_conn, db_reset
from app.services.AdminService import AdminService


class TestAdminService(object):


    def test_Approve_User(self):
        connection = get_conn()
        filters={'i_username':'smith_j'}
        admin_service = AdminService()
        admin_service.ApproveUser(filters)
        with connection.cursor() as cursor:
            query = "select * from user where username = 'smith_j'"
            cursor.execute(query)
            Actual = cursor.fetchall()
            connection.commit()
        connection.close()
        assert Actual[0]['status']=="Approved"


    def test_Decline_User(self):
        db_reset()
        connection = get_conn()
        filters = {'i_username':'smith_j'}
        admin_service = AdminService()
        admin_service.DeclineUser(filters)
        with connection.cursor() as cursor:
            query = "select * from user where username = 'smith_j'"
            cursor.execute(query)
            Actual = cursor.fetchall()
            connection.commit()
        connection.close()
        assert Actual[0]['status']=="Declined"

    def test_Decline_already_approved_User(self):
        connection = get_conn()
        filters = {'i_username':'manager1'}
        admin_service = AdminService()
        admin_service.DeclineUser(filters)
        with connection.cursor() as cursor:
            query = "select * from user where username = 'manager1'"
            cursor.execute(query)
            Actual = cursor.fetchall()
            connection.commit()
        connection.close()
        assert Actual[0]['status']=="Approved"


    def test_filter_user(self):
        connection = get_conn()
        filterz = {'i_status':"Declined",'i_sortBy':"username",'i_sortDirection':"desc"}
        
        admin_service = AdminService()
        Actual = admin_service.FilterUser(filterz)
        Expected = [
        {'username':'clarinetbeast','creditCardNum':0,'status':'Declined','userType':'Customer'},
        {'username':'gdanger','creditCardNum':0,'status':'Declined','userType':'User'},
        {'username':'smith_j','creditCardNum':0,'status':'Declined','userType':'User'},
        {'username':'texasStarKarate','creditCardNum':0,'status':'Declined','userType':'User'}]
        print(Actual)
        assert Actual==Expected

    def test_filter_user_no_filters(self):
        db_reset()

        filterz = {"i_status": None, "username": "", 'i_sortBy':"username",'i_sortDirection':"desc"}
        
        admin_service = AdminService()
        Actual = admin_service.FilterUser(filterz)
        Expected = [
            {'username':'clarinetbeast','creditCardNum':0,'status':'Declined','userType':'Customer'},
            {'username':'gdanger','creditCardNum':0,'status':'Declined','userType':'User'},
            {'username':'smith_j','creditCardNum':0,'status':'Declined','userType':'User'},
            {'username':'texasStarKarate','creditCardNum':0,'status':'Declined','userType':'User'},

        ]
        print(Actual)
        assert len(Actual) == 30


    def test_CreateMovie(self):

        connection = get_conn()
        with connection.cursor() as cursor:
            sql_del = """delete from Movie where movName = "4400 The Movie" and movReleaseDate = '20190812' """
            cursor.execute(sql_del)
            connection.commit()

            admin_service = AdminService()
            admin_service.CreateMovie('cool_class4400')

            cursor.execute("insert into Movie (movName,movReleaseDate,duration) values (('4400 The Movie', '20190812', 130)")
            data = cursor.fetchall()
            connection.commit()

            sql_del = """delete from Movie where movName = "4400 The Movie" and movReleaseDate = '20190812' """
            cursor.execute(sql_del)
            connection.commit()

        connection.close()

        assert len(data) == 1
