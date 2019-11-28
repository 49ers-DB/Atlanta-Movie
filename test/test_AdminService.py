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
        db_reset()
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

        assert Actual[0]['status']=="Declined"

        filters = {'i_username':'georgep'}
        admin_service.DeclineUser(filters)
        with connection.cursor() as cursor:
            query = "select * from user where username = 'georgep'"
            cursor.execute(query)
            Actual = cursor.fetchall()
            connection.commit()
        connection.close()

        assert Actual[0]['status']=="Approved"

    def test_filter_user(self):
        db_reset()
        connection = get_conn()
        filterz = {'i_status':"Declined",'i_sortBy':"username",'i_sortDirection':"asc","username":""}
        
        admin_service = AdminService()
        Actual = admin_service.FilterUser(filterz)
        Expected = [
        {'username':'clarinetbeast','creditCardCount':0,'status':'Declined','userType':'Customer'},
        {'username':'gdanger','creditCardCount':0,'status':'Declined','userType':'User'},
        {'username':'texasStarKarate','creditCardCount':0,'status':'Declined','userType':'User'}]
        print(Actual)
        assert Actual==Expected

    def test_filter_user_no_filters(self):
        db_reset()
        expected = [{"creditCardCount": 1, "status": "Approved", "userType": "Customer", "username": "theScienceGuy"}, {"creditCardCount": 1, "status": "Approved", "userType": "Customer", "username": "thePiGuy3.14"}, {"creditCardCount": 0, "status": "Declined", "userType": "User", "username": "texasStarKarate"}, {"creditCardCount": 0, "status": "Pending", "userType": "User", "username": "smith_j"}, {"creditCardCount": 1, "status": "Approved", "userType": "Customer", "username": "RitzLover28"}, {"creditCardCount": 0, "status": "Approved", "userType": "Manager", "username": "radioactivePoRa"}, {"creditCardCount": 1, "status": "Approved", "userType": "Customer", "username": "programerAAL"}, {"creditCardCount": 1, "status": "Approved", "userType": "Customer", "username": "notFullMetal"}, {"creditCardCount": 0, "status": "Approved", "userType": "Manager", "username": "manager4"}, {"creditCardCount": 0, "status": "Approved", "userType": "Manager", "username": "manager3"}, {"creditCardCount": 0, "status": "Approved", "userType": "Manager", "username": "manager2"}, {"creditCardCount": 0, "status": "Approved", "userType": "Manager", "username": "manager1"}, {"creditCardCount": 3, "status": "Approved", "userType": "Customer", "username": "isthisthekrustykrab"}, {"creditCardCount": 1, "status": "Approved", "userType": "Customer", "username": "imready"}, {"creditCardCount": 0, "status": "Approved", "userType": "Manager", "username": "imbatman"}, {"creditCardCount": 3, "status": "Approved", "userType": "Customer", "username": "ilikemoney$$"}, {"creditCardCount": 0, "status": "Approved", "userType": "Manager", "username": "ghcghc"}, {"creditCardCount": 5, "status": "Approved", "userType": "CustomerManager", "username": "georgep"}, {"creditCardCount": 0, "status": "Declined", "userType": "User", "username": "gdanger"}, {"creditCardCount": 1, "status": "Approved", "userType": "Customer", "username": "fullMetal"}, {"creditCardCount": 0, "status": "Approved", "userType": "Manager", "username": "fatherAI"}, {"creditCardCount": 2, "status": "Approved", "userType": "CustomerManager", "username": "entropyRox"}, {"creditCardCount": 1, "status": "Approved", "userType": "Customer", "username": "eeqmcsquare"}, {"creditCardCount": 1, "status": "Approved", "userType": "Customer", "username": "does2Much"}, {"creditCardCount": 1, "status": "Approved", "userType": "Customer", "username": "DNAhelix"}, {"creditCardCount": 1, "status": "Approved", "userType": "CustomerAdmin", "username": "cool_class4400"}, {"creditCardCount": 0, "status": "Declined", "userType": "Customer", "username": "clarinetbeast"}, {"creditCardCount": 1, "status": "Approved", "userType": "Customer", "username": "calcwizard"}, {"creditCardCount": 2, "status": "Approved", "userType": "Customer", "username": "calcultron2"}, {"creditCardCount": 1, "status": "Approved", "userType": "CustomerManager", "username": "calcultron"}]
        admin_service = AdminService()

        filterz = {"i_status": "ALL", "username": "", 'i_sortBy':"",'i_sortDirection':""}
        Actual = admin_service.FilterUser(filterz)
        assert expected == Actual 

        filterz = {"i_status": "ALL", "username": "", 'i_sortBy':"username",'i_sortDirection':"desc"}
        Actual = admin_service.FilterUser(filterz)
        assert expected == Actual

    def test_filter_company_no_filters(self):
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

        filterz = {
            "i_comName":'ALL',
            "i_minCity": None,
            "i_maxCity": None,
            "i_minTheater": None,
            "i_maxTheater": None,
            "i_minEmployee": None,
            "i_maxEmployee": None,
            "i_sortBy": '',
            "i_sortDirection": 'DESC'
        }

        actual = admin_service.ManageCompany(filterz)
        assert actual == expected


        filterz = {
            "i_comName":'ALL',
            "i_minCity": None,
            "i_maxCity": None,
            "i_minTheater": None,
            "i_maxTheater": None,
            "i_minEmployee": None,
            "i_maxEmployee": None,
            "i_sortBy": 'comName',
            "i_sortDirection": 'DESC'
        }

        actual = admin_service.ManageCompany(filterz)
        assert actual == expected

    def test_admin_create_theater(self):
        db_reset()
        
        admin_service = AdminService()
        filters = {"i_thName":'Perimeter Cinema', 'i_comName':'4400 Theater Company', 'i_thStreet':'1 Roundabout Circle','i_thCity': 'Waco', 'i_thState':'TX','i_thZipcode': 90467,'i_capacity': 2,'i_managerUsername': 'manager1'}
        admin_service.CreateTheater(filters)

        connection = get_conn()
        with connection.cursor() as cursor:
            sql = "SELECT * FROM Theater where thName='Perimeter Cinema'"
            cursor.execute(sql)
            data = cursor.fetchall()
            connection.commit()

        connection.close()

        print(data)
        assert len(data) == 1
        assert data[0]['comName'] == '4400 Theater Company'


    def test_admin_view_comDetail_emp(self):
        db_reset()

        admin_service = AdminService()
        filters = {'i_comName': 'EZ Theater Company'}
        data = admin_service.admin_view_comDetail_emp(filters)

        expected = [{"empFirstname": "Dwight", "empLastname": "Schrute"}, {"empFirstname": "Alan", "empLastname": "Turing"}]

        assert expected == data


    def test_admin_view_comDetail_th(self):
        db_reset()

        admin_service = AdminService()
        filters = {'i_comName': '4400 Theater Company'}
        data = admin_service.admin_view_comDetail_th(filters)

        expected = [{"thCapacity": 4, "thCity": "San Francisco", "thManagerUsername": "entropyRox", "thName": "Cinema Star", "thState": "CA"}, {"thCapacity": 2, "thCity": "Seattle", "thManagerUsername": "georgep", "thName": "Jonathan's Movies", "thState": "WA"}, {"thCapacity": 5, "thCity": "Boulder", "thManagerUsername": "radioactivePoRa", "thName": "Star Movies", "thState": "CA"}]

        assert expected == data


    def test_CreateMovie(self):
        db_reset()
        connection = get_conn()
       
        data = {
            'movieName':'4400 The Movie',
            'releaseDate':'2019-08-12',
            'duration':130,
        }
        admin_service = AdminService()
        admin_service.CreateMovie(data)

        sql_del = """Select * from Movie where movName = "4400 The Movie" and movReleaseDate = '2019-08-12' """
        connection = get_conn()
        with connection.cursor() as cursor:
            cursor.execute(sql_del)
            row = cursor.fetchall()
            connection.commit()

        connection.close()

        expected = {
            'movName':'4400 The Movie',
            'movReleaseDate':datetime.date.fromisoformat('2019-08-12'),
            'duration':130,
        }

        print(row)
        assert row == [expected]
