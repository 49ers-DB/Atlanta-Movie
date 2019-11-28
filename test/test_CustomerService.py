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
from app.services.CustomerService import CustomerService
from app.services.DBService import db_reset, get_conn


class TestCustomerService(object):


    def test_ExploreMovie(self):
        #MoviePlay.movName,
        # MoviePlay.'comName':,
        #  Theater.thStreet,
        # Theater.thCity,
        #  Theater.thState,
        #   Theater.thZipcode,
        #thName
        #  MoviePlay.movPlayDate\

        expected = [
        {'movName':"4400 The Movie",'movPlayDate':datetime.date(2019,10,12),'thName':"ABC Theater",'comName':"Awesome Theater Company",'thStreet':'880 Color Dr','thCity':'Austin','thState':'TX','thZipcode':'73301'},
        {'movName':"The First Pokemon Movie",'movPlayDate':datetime.date(2018,7,19),'thName':"ABC Theater",'comName':"Awesome Theater Company",'thStreet':'880 Color Dr','thCity':'Austin','thState':'TX','thZipcode':'73301'},
        {'movName':'Georgia Tech The Movie','movPlayDate':datetime.date(1985,8,13),'thName':'ABC Theater','comName':'Awesome Theater Company','thStreet':'880 Color Dr','thCity':'Austin','thState':'TX','thZipcode':'73301'},
        {'movName':'How to Train Your Dragon','movPlayDate':datetime.date(2010,4,2),'thName':'Cinema Star','comName':'4400 Theater Company','thStreet':'100 Cool Place','thCity':'San Francisco','thState':'CA','thZipcode':'94016'},
        {'movName':"4400 The Movie",'movPlayDate':datetime.date(2019,9,12),'thName':'Cinema Star','comName':'4400 Theater Company','thStreet':'100 Cool Place','thCity':'San Francisco','thState':'CA','thZipcode':'94016'},
        {'movName':"The King's Speech",'movPlayDate':datetime.date(2019,12,20),'thName':'Cinema Star','comName':'4400 Theater Company','thStreet':'100 Cool Place','thCity':'San Francisco','thState':'CA','thZipcode':'94016'},
        {'movName':'Spaceballs','movPlayDate':datetime.date(2000,2,2),'thName':'Cinema Star','comName':'4400 Theater Company','thStreet':'100 Cool Place','thCity':'San Francisco','thState':'CA','thZipcode':'94016'},
        {'movName':'Georgia Tech The Movie','movPlayDate':datetime.date(2019,9,30),'thName':'Cinema Star','comName':'4400 Theater Company','thStreet':'100 Cool Place','thCity':'San Francisco','thState':'CA','thZipcode':'94016'},
        {'movName':"George P Burdell's Life Story",'movPlayDate':datetime.date(2010,5,20),'thName':'Cinema Star','comName':'4400 Theater Company','thStreet':'100 Cool Place','thCity':'San Francisco','thState':'CA','thZipcode':'94016'},
        {'movName':'How to Train Your Dragon','movPlayDate':datetime.date(2010,3,22),'thName':'Main Movies','comName':'EZ Theater Company',"thStreet":"123 Main St",'thCity':"New York",'thState':'NY','thZipcode':'10001'},
        {'movName':'How to Train Your Dragon','movPlayDate':datetime.date(2010,3,23),'thName':'Main Movies','comName':'EZ Theater Company',"thStreet":"123 Main St",'thCity':"New York",'thState':'NY','thZipcode':'10001'},
        {'movName':'Spaceballs','movPlayDate':datetime.date(1999,6,24),'thName':'Main Movies','comName':'EZ Theater Company',"thStreet":"123 Main St",'thCity':"New York",'thState':'NY','thZipcode':'10001'},
        {'movName':"George P Burdell's Life Story",'movPlayDate':datetime.date(2019,10,22),'thName':'Main Movies','comName':'EZ Theater Company',"thStreet":"123 Main St",'thCity':"New York",'thState':'NY','thZipcode':'10001'},
        {'movName':"George P Burdell's Life Story",'movPlayDate':datetime.date(2019,7,14),'thName':'Main Movies','comName':'EZ Theater Company',"thStreet":"123 Main St",'thCity':"New York",'thState':'NY','thZipcode':'10001'},
        {'movName':"The King's Speech",'movPlayDate':datetime.date(2019,12,20),'thName':'Main Movies','comName':'EZ Theater Company',"thStreet":"123 Main St",'thCity':"New York",'thState':'NY','thZipcode':'10001'},
        {'movName':'Spaceballs','movPlayDate':datetime.date(2010,4,2),'thName':'ML Movies','comName':'AI Theater Company','thStreet':'314 Pi St','thCity':'Pallet Town','thState':'KS','thZipcode':'31415'},
        {'movName':'Spaceballs','movPlayDate':datetime.date(2023,1,23),'thName':'ML Movies','comName':'AI Theater Company','thStreet':'314 Pi St','thCity':'Pallet Town','thState':'KS','thZipcode':'31415'},
        {'movName':'Calculus Returns: A ML Story','movPlayDate':datetime.date(2019,10,10),'thName':'ML Movies','comName':'AI Theater Company','thStreet':'314 Pi St','thCity':'Pallet Town','thState':'KS','thZipcode':'31415'},
        {'movName':'Calculus Returns: A ML Story','movPlayDate':datetime.date(2019,12,30),'thName':'ML Movies','comName':'AI Theater Company','thStreet':'314 Pi St','thCity':'Pallet Town','thState':'KS','thZipcode':'31415'},
        {'movName':'Spider-Man: Into the Spider-Verse','movPlayDate':datetime.date(2019,9,30),'thName':'ML Movies','comName':'AI Theater Company','thStreet':'314 Pi St','thCity':'Pallet Town','thState':'KS','thZipcode':'31415'},
        {'movName':'How to Train Your Dragon','movPlayDate':datetime.date(2010,3,25),'thName':'Star Movies','comName':'EZ Theater Company','thStreet':'745 GT St','thCity':'Atlanta','thState':'GA','thZipcode':'30332'},
        {'movName':"4400 The Movie",'movPlayDate':datetime.date(2019,8,12),'thName':'Star Movies','comName':'EZ Theater Company','thStreet':'745 GT St','thCity':'Atlanta','thState':'GA','thZipcode':'30332'}
        ]

        customer_service = CustomerService()
            # i_movName = filters.get("i_movName")
            # i_comName = filters.get("i_comName")
            # i_city = filters.get("i_city")
            # i_state = filters.get("i_state")
            # i_minMovPlayDate = filters.get("i_minMovPlayDate")
            # i_maxMovPlayDate = filters.get("i_maxMovPlayDate")

        # filters = {
        #   'i_movName':
        #   'i_comName':
        #   'i_city':
        #   'i_state':
        #   'i_minMovPlayDate':
        #   'i_maxMovPlayDate':
        # }
        filters = {
        'i_city':"",
        'i_state':"",
        'i_movName':'','i_comName': '',
        }

        actual = customer_service.ExploreMovie(filters)

        assert len(expected) == len(actual)
        assert sorted(actual, key=functools.cmp_to_key(compare_movie)) == sorted(expected, key=functools.cmp_to_key(compare_movie))


    def test_ViewMovie(self):
        db_reset()

        customer_service = CustomerService()

        filters = {
            'i_thName':"ML Movies",
            'i_comName':"AI Theater Company",
            'i_movName':'Spider-Man: Into the Spider-Verse',
            'i_movPlayDate': 'Mon Sep 30 2019',
            'i_creditCardNum': "1111111111110000"
        }

        date = dateutil.parser.parse(filters['i_movPlayDate']).date()
        print(date)

        user_name = 'georgep'

        length = 0

        customer_service.ViewMovie( filters)

        connection = get_conn()
        #   with connection.cursor() as cursor:
        #     info = """select visitID, username, thName, comName, visitDate from UserVisitTheater where
        #       visitID=(%s) and username=(%s)
        #       and thName=(%s)
        #       and comName=(%s)
        #       and visitDate=(%s)"""
        #     cursor.execute(info, (new_id, user_name, filters['i_thname'], filters['i_coname'], date))
        #     data=cursor.fetchall()
        #     connection.commit()
            # connection = get_conn()
        with connection.cursor() as cursor:
            leng="""select creditCardNum from CustomerViewMovie where creditCardNum='1111111111110000'"""
            cursor.execute(leng)
            length = cursor.fetchall()
            connection.commit()
        connection.close()


        assert len(length) == 1
        assert length[0]['creditCardNum'] == '1111111111110000'








    def test_ViewHistory(self):

        connection = get_conn()
        with connection.cursor() as cursor:

            customer_service = CustomerService()

            customer_service.ViewHistory('georgep')

            cursor.execute("select movName, thName, comName, creditCardNum, movPlayDate from CustomerViewMovie where CustomerViewMovie.creditCardNum in (select creditCardNum from CustomerCreditCard where CustomerCreditCard.username = 'calcwizard')")
            data=cursor.fetchall()
            connection.commit()

        connection.close()

        assert len(data)==0





    def test_customer_filter_mov(self):
        db_reset()

        customer_service = CustomerService()
        filters = {'i_movName':'ALL','i_comName': 'ALL','i_city': '','i_state': '','i_minMovPlayDate': None,'i_maxMovPlayDate': None}
        data = customer_service.ExploreMovie(filters)

        expected = [{"comName": "4400 Theater Company", "movName": "4400 The Movie", "movPlayDate": "2019-09-12", "movReleaseDate": "2019-08-12", "thCity": "San Francisco", "thName": "Cinema Star", "thState": "CA", "thStreet": "100 Cool Place", "thZipcode": "94016"}, {"comName": "4400 Theater Company", "movName": "George P Burdell's Life Story", "movPlayDate": "2010-05-20", "movReleaseDate": "1927-08-12", "thCity": "San Francisco", "thName": "Cinema Star", "thState": "CA", "thStreet": "100 Cool Place", "thZipcode": "94016"}, {"comName": "4400 Theater Company", "movName": "Georgia Tech The Movie", "movPlayDate": "2019-09-30", "movReleaseDate": "1985-08-13", "thCity": "San Francisco", "thName": "Cinema Star", "thState": "CA", "thStreet": "100 Cool Place", "thZipcode": "94016"}, {"comName": "4400 Theater Company", "movName": "How to Train Your Dragon", "movPlayDate": "2010-04-02", "movReleaseDate": "2010-03-21", "thCity": "San Francisco", "thName": "Cinema Star", "thState": "CA", "thStreet": "100 Cool Place", "thZipcode": "94016"}, {"comName": "4400 Theater Company", "movName": "Spaceballs", "movPlayDate": "2000-02-02", "movReleaseDate": "1987-06-24", "thCity": "San Francisco", "thName": "Cinema Star", "thState": "CA", "thStreet": "100 Cool Place", "thZipcode": "94016"}, {"comName": "4400 Theater Company", "movName": "The King's Speech", "movPlayDate": "2019-12-20", "movReleaseDate": "2010-11-26", "thCity": "San Francisco", "thName": "Cinema Star", "thState": "CA", "thStreet": "100 Cool Place", "thZipcode": "94016"}, {"comName": "AI Theater Company", "movName": "Calculus Returns: A ML Story", "movPlayDate": "2019-10-10", "movReleaseDate": "2019-09-19", "thCity": "Pallet Town", "thName": "ML Movies", "thState": "KS", "thStreet": "314 Pi St", "thZipcode": "31415"}, {"comName": "AI Theater Company", "movName": "Calculus Returns: A ML Story", "movPlayDate": "2019-12-30", "movReleaseDate": "2019-09-19", "thCity": "Pallet Town", "thName": "ML Movies", "thState": "KS", "thStreet": "314 Pi St", "thZipcode": "31415"}, {"comName": "AI Theater Company", "movName": "Spaceballs", "movPlayDate": "2010-04-02", "movReleaseDate": "1987-06-24", "thCity": "Pallet Town", "thName": "ML Movies", "thState": "KS", "thStreet": "314 Pi St", "thZipcode": "31415"}, {"comName": "AI Theater Company", "movName": "Spaceballs", "movPlayDate": "2023-01-23", "movReleaseDate": "1987-06-24", "thCity": "Pallet Town", "thName": "ML Movies", "thState": "KS", "thStreet": "314 Pi St", "thZipcode": "31415"}, {"comName": "AI Theater Company", "movName": "Spider-Man: Into the Spider-Verse", "movPlayDate": "2019-09-30", "movReleaseDate": "2018-12-01", "thCity": "Pallet Town", "thName": "ML Movies", "thState": "KS", "thStreet": "314 Pi St", "thZipcode": "31415"}, {"comName": "Awesome Theater Company", "movName": "4400 The Movie", "movPlayDate": "2019-10-12", "movReleaseDate": "2019-08-12", "thCity": "Austin", "thName": "ABC Theater", "thState": "TX", "thStreet": "880 Color Dr", "thZipcode": "73301"}, {"comName": "Awesome Theater Company", "movName": "Georgia Tech The Movie", "movPlayDate": "1985-08-13", "movReleaseDate": "1985-08-13", "thCity": "Austin", "thName": "ABC Theater", "thState": "TX", "thStreet": "880 Color Dr", "thZipcode": "73301"}, {"comName": "Awesome Theater Company", "movName": "The First Pokemon Movie", "movPlayDate": "2018-07-19", "movReleaseDate": "1998-07-19", "thCity": "Austin", "thName": "ABC Theater", "thState": "TX", "thStreet": "880 Color Dr", "thZipcode": "73301"}, {"comName": "EZ Theater Company", "movName": "George P Burdell's Life Story", "movPlayDate": "2019-07-14", "movReleaseDate": "1927-08-12", "thCity": "New York", "thName": "Main Movies", "thState": "NY", "thStreet": "123 Main St", "thZipcode": "10001"}, {"comName": "EZ Theater Company", "movName": "George P Burdell's Life Story", "movPlayDate": "2019-10-22", "movReleaseDate": "1927-08-12", "thCity": "New York", "thName": "Main Movies", "thState": "NY", "thStreet": "123 Main St", "thZipcode": "10001"}, {"comName": "EZ Theater Company", "movName": "How to Train Your Dragon", "movPlayDate": "2010-03-22", "movReleaseDate": "2010-03-21", "thCity": "New York", "thName": "Main Movies", "thState": "NY", "thStreet": "123 Main St", "thZipcode": "10001"}, {"comName": "EZ Theater Company", "movName": "How to Train Your Dragon", "movPlayDate": "2010-03-23", "movReleaseDate": "2010-03-21", "thCity": "New York", "thName": "Main Movies", "thState": "NY", "thStreet": "123 Main St", "thZipcode": "10001"}, {"comName": "EZ Theater Company", "movName": "Spaceballs", "movPlayDate": "1999-06-24", "movReleaseDate": "1987-06-24", "thCity": "New York", "thName": "Main Movies", "thState": "NY", "thStreet": "123 Main St", "thZipcode": "10001"}, {"comName": "EZ Theater Company", "movName": "The King's Speech", "movPlayDate": "2019-12-20", "movReleaseDate": "2010-11-26", "thCity": "New York", "thName": "Main Movies", "thState": "NY", "thStreet": "123 Main St", "thZipcode": "10001"}, {"comName": "EZ Theater Company", "movName": "4400 The Movie", "movPlayDate": "2019-08-12", "movReleaseDate": "2019-08-12", "thCity": "Atlanta", "thName": "Star Movies", "thState": "GA", "thStreet": "745 GT St", "thZipcode": "30332"}, {"comName": "EZ Theater Company", "movName": "How to Train Your Dragon", "movPlayDate": "2010-03-25", "movReleaseDate": "2010-03-21", "thCity": "Atlanta", "thName": "Star Movies", "thState": "GA", "thStreet": "745 GT St", "thZipcode": "30332"}]

        assert len(expected) == len(data)


    # def test_customer_view_mov(self):
    #     db_reset()

    #     customer_service = CustomerService()
    #     filters = {'i_creditCardNum':'111111111','i_movName': 'Spaceballs','i_movReleaseDate': '1987-06-24','i_thName': 'ML Movies','i_comName': 'AI Theater Company','i_movPlayDate': '2023-01-23'}
    #     data = customer_service.ViewMovie(filters)


def compare_movie(item1, item2):
    if item1['movName'] < item2['movName']:
        return -1
    elif item1['movName'] > item2['movName']:
        return 1
    else:
        return compare_theater_name(item1, item2)

def compare_theater_name(item1, item2):
    if item1['thName'] < item2['thName']:
        return -1
    elif item1['thName'] > item2['thName']:
        return 1
    else:
        return compare_play_date(item1, item2)

def compare_play_date(item1, item2):

    if item1['movPlayDate'] < item2['movPlayDate']:
        return -1
    elif item1['movPlayDate'] > item2['movPlayDate']:
        return 1
    else:
        return 0


