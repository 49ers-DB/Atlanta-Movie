import pytest

import functools
import datetime
import dateutil.parser

import pymysql
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from app.services.DBService import get_conn



from app.services.UserService import UserService


class TestUserService(object):

    connection = pymysql.connect(host='localhost',
                             user='root',
                             password='1234',
                             db='moviez',
                             charset='utf8mb4',
                             port=3306,
                             cursorclass=pymysql.cursors.DictCursor)

    

    def test_Explore_Theater_NoFilters(self):
      
      user_service = UserService()

      filters = {
        'city':"",
        'selectedState':None,
        'selectedCompany':None,
        'selectedTheater':None
      }

      actual = user_service.ExploreTheater(filters)

      expected = [
        {'comName':"EZ Theater Company",'thName':"Main Movies",'thStreet':"123 Main St",'thCity':"New York",'thState':'NY','thZipcode':'10001'},
        {'comName':"EZ Theater Company",'thName':'Star Movies','thStreet':'745 GT St','thCity':'Atlanta','thState':'GA','thZipcode':'30332'},
        {'comName':'4400 Theater Company','thName':'Cinema Star','thStreet':'100 Cool Place','thCity':'San Francisco','thState':'CA','thZipcode':'94016'},
        {'comName':'4400 Theater Company','thName':'Star Movies','thStreet':'4400 Rocks Ave','thCity':'Boulder','thState':'CA','thZipcode':'80301'},
        {'comName':'4400 Theater Company','thName':"Jonathan's Movies",'thStreet':'67 Pearl Dr','thCity':'Seattle','thState':'WA','thZipcode':'98101'},
        {'comName':'Awesome Theater Company','thName':'ABC Theater','thStreet':'880 Color Dr','thCity':'Austin','thState':'TX','thZipcode':'73301'},
        {'comName':'AI Theater Company','thName':'ML Movies','thStreet':'314 Pi St','thCity':'Pallet Town','thState':'KS','thZipcode':'31415'}
      ]

      assert len(actual) == len(expected)

      assert sorted(actual, key=functools.cmp_to_key(compare_theater)) == sorted(expected, key=functools.cmp_to_key(compare_theater))


    def test_Explore_Theater_CityFilter(self):
      
      user_service = UserService()

      filters = {
        'city':"New York",
        'selectedState':None,
        'selectedCompany':None,
        'selectedTheater':None
      }

      actual = user_service.ExploreTheater(filters)

      expected = [
        {'comName':"EZ Theater Company",'thName':"Main Movies",'thStreet':"123 Main St",'thCity':"New York",'thState':'NY','thZipcode':'10001'},
      ]

      assert len(actual) == len(expected)

      assert sorted(actual, key=functools.cmp_to_key(compare_theater)) == sorted(expected, key=functools.cmp_to_key(compare_theater))

    def test_Explore_Theater_StateFilter(self):
      user_service = UserService()

      filters = {
        'city':"",
        'selectedState': "CA",
        'selectedCompany':None,
        'selectedTheater':None
      }

      actual = user_service.ExploreTheater(filters)

      expected = [
        {'comName':'4400 Theater Company','thName':'Cinema Star','thStreet':'100 Cool Place','thCity':'San Francisco','thState':'CA','thZipcode':'94016'},
        {'comName':'4400 Theater Company','thName':'Star Movies','thStreet':'4400 Rocks Ave','thCity':'Boulder','thState':'CA','thZipcode':'80301'}
      ]

      assert len(actual) == len(expected)

      assert sorted(actual, key=functools.cmp_to_key(compare_theater)) == sorted(expected, key=functools.cmp_to_key(compare_theater))





    def test_Explore_Theater_Company_Filter(self):
      
      user_service = UserService()

      filters = {
        'city':"",
        'selectedState':None,
        'selectedCompany':{'value':'4400 Theater Company'},
        'selectedTheater':None
      }

      actual = user_service.ExploreTheater(filters)

      expected = [
        
        {'comName':'4400 Theater Company','thName':'Cinema Star','thStreet':'100 Cool Place','thCity':'San Francisco','thState':'CA','thZipcode':'94016'},
        {'comName':'4400 Theater Company','thName':'Star Movies','thStreet':'4400 Rocks Ave','thCity':'Boulder','thState':'CA','thZipcode':'80301'},
        {'comName':'4400 Theater Company','thName':"Jonathan's Movies",'thStreet':'67 Pearl Dr','thCity':'Seattle','thState':'WA','thZipcode':'98101'}
        
      ]

      assert len(actual) == len(expected)

      assert sorted(actual, key=functools.cmp_to_key(compare_theater)) == sorted(expected, key=functools.cmp_to_key(compare_theater))


    def test_Explore_Theater_Theater_filter(self):
      
      user_service = UserService()

      filters = {
        'city':"",
        'selectedState':None,
        'selectedCompany':{'value':'4400 Theater Company'},
        'selectedTheater':'Star Movies'
      }

      actual = user_service.ExploreTheater(filters)

      expected = [
        
        {'comName':'4400 Theater Company','thName':'Star Movies','thStreet':'4400 Rocks Ave','thCity':'Boulder','thState':'CA','thZipcode':'80301'}
        
      ]

      assert len(actual) == len(expected)

      assert sorted(actual, key=functools.cmp_to_key(compare_theater)) == sorted(expected, key=functools.cmp_to_key(compare_theater))

    

    def test_logVisit(self):

      user_service = UserService()

      filters = {
        'i_thname':'Cinema Star',
        'i_coname':'4400 Theater Company',
        'i_visitdate': '2019-11-24T01:38:50.493Z'
      }

      date = dateutil.parser.parse(filters['i_visitdate']).date()

      user_name = 'georgep'

      length = 0

      connection = get_conn()
      with connection.cursor() as cursor:
        leng="select visitID from UserVisitTheater"
        cursor.execute(leng)
        length = cursor.fetchall()
        connection.commit()
      connection.close()

      new_id= len(length) + 1

      user_service.LogVisit(user_name, filters)

      connection = get_conn()
      with connection.cursor() as cursor:
        info = """select visitID, username, thName, comName, visitDate from UserVisitTheater where
          visitID=(%s) and username=(%s)
          and thName=(%s)
          and comName=(%s)
          and visitDate=(%s)"""
        cursor.execute(info, (new_id, user_name, filters['i_thname'], filters['i_coname'], date))
        data=cursor.fetchall()
        connection.commit()

        sql_del = """delete From UserVisitTheater where visitID = (%s)"""
        cursor.execute(sql_del, (new_id))
        connection.commit()

      connection.close()

      assert len(data) == 1




def compare_theater(item1, item2):
    if item1['comName'] < item2['comName']:
        return -1
    elif item1['comName'] > item2['comName']:
        return 1
    else:
        return compare_theater_name(item1, item2)

def compare_theater_name(item1, item2):
    
    if item1['thName'] < item2['thName']:
        return -1
    elif item1['thName'] > item2['thName']:
        return 1
    else:
        return 0