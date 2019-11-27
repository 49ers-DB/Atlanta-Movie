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
        expected = [{"creditCardCount": 1, "status": "Approved", "userType": "Customer", "username": "theScienceGuy"}, {"creditCardCount": 1, "status": "Approved", "userType": "Customer", "username": "thePiGuy3.14"}, {"creditCardCount": 0, "status": "Declined", "userType": "User", "username": "texasStarKarate"}, {"creditCardCount": 0, "status": "Pending", "userType": "User", "username": "smith_j"}, {"creditCardCount": 1, "status": "Approved", "userType": "Customer", "username": "RitzLover28"}, {"creditCardCount": 0, "status": "Approved", "userType": "Manager", "username": "radioactivePoRa"}, {"creditCardCount": 1, "status": "Approved", "userType": "Customer", "username": "programerAAL"}, {"creditCardCount": 1, "status": "Approved", "userType": "Customer", "username": "notFullMetal"}, {"creditCardCount": 0, "status": "Approved", "userType": "Manager", "username": "manager4"}, {"creditCardCount": 0, "status": "Approved", "userType": "Manager", "username": "manager3"}, {"creditCardCount": 0, "status": "Approved", "userType": "Manager", "username": "manager2"}, {"creditCardCount": 0, "status": "Approved", "userType": "Manager", "username": "manager1"}, {"creditCardCount": 3, "status": "Approved", "userType": "Customer", "username": "isthisthekrustykrab"}, {"creditCardCount": 1, "status": "Approved", "userType": "Customer", "username": "imready"}, {"creditCardCount": 0, "status": "Approved", "userType": "Manager", "username": "imbatman"}, {"creditCardCount": 3, "status": "Approved", "userType": "Customer", "username": "ilikemoney$$"}, {"creditCardCount": 0, "status": "Approved", "userType": "Manager", "username": "ghcghc"}, {"creditCardCount": 5, "status": "Approved", "userType": "CustomerManager", "username": "georgep"}, {"creditCardCount": 0, "status": "Declined", "userType": "User", "username": "gdanger"}, {"creditCardCount": 1, "status": "Approved", "userType": "Customer", "username": "fullMetal"}, {"creditCardCount": 0, "status": "Approved", "userType": "Manager", "username": "fatherAI"}, {"creditCardCount": 2, "status": "Approved", "userType": "CustomerManager", "username": "entropyRox"}, {"creditCardCount": 1, "status": "Approved", "userType": "Customer", "username": "eeqmcsquare"}, {"creditCardCount": 1, "status": "Approved", "userType": "Customer", "username": "does2Much"}, {"creditCardCount": 1, "status": "Approved", "userType": "Customer", "username": "DNAhelix"}, {"creditCardCount": 1, "status": "Approved", "userType": "CustomerAdmin", "username": "cool_class4400"}, {"creditCardCount": 0, "status": "Declined", "userType": "Customer", "username": "clarinetbeast"}, {"creditCardCount": 1, "status": "Approved", "userType": "Customer", "username": "calcwizard"}, {"creditCardCount": 2, "status": "Approved", "userType": "Customer", "username": "calcultron2"}, {"creditCardCount": 1, "status": "Approved", "userType": "CustomerManager", "username": "calcultron"}]
        admin_service = AdminService()

        filterz = {"i_status": "ALL", "username": "", 'i_sortBy':"",'i_sortDirection':""}
        Actual = admin_service.FilterUser(filterz)
        assert expected == Actual 

        filterz = {"i_status": "", "username": "", 'i_sortBy':"username",'i_sortDirection':"desc"}
        Actual = admin_service.FilterUser(filterz)
        assert expected == Actual

        filterz = {"i_status": "ALL", "username": "", 'i_sortBy':"username",'i_sortDirection':"desc"}
        Actual = admin_service.FilterUser(filterz)
        assert expected == Actual

    def test_filter_theater_no_filters(self):
        db_reset()
        expected = [{"comName": "EZ Theater Company", "numCityCover": 2, "numEmployee": 2, "numTheater": 2}, {"comName": "Awesome Theater Company", "numCityCover": 1, "numEmployee": 1, "numTheater": 1}, {"comName": "AI Theater Company", "numCityCover": 1, "numEmployee": 2, "numTheater": 1}, {"comName": "4400 Theater Company", "numCityCover": 3, "numEmployee": 6, "numTheater": 3}]
        admin_service = AdminService()

        filterz = {
            "i_comName":'ALL',
            "i_minCity": None,
            "i_maxCity": None,
            "i_minTheater": None,
            "i_maxTheater": None,
            "i_minEmployee": None,
            "i_maxEmployee": None,
            "i_sortBy": '',
            "i_sortDirection": ''
        }
        
        actual = admin_service.ManageCompany(filterz)
        assert actual == expected

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
