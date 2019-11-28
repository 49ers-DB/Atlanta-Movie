import pytest
import functools
import datetime
import dateutil.parser
import pymysql
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from app.services.DBService import get_conn, db_reset
from app.services.UserService import UserService


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

def test_user_filter_th():
  db_reset()
  user_service = UserService()
  'ALL', 'ALL', '', ''
  filters = {
    
        'city':'',
        'selectedState':'',
        'selectedCompany':'ALL',
        'selectedTheater':'ALL'
      }

  actual = user_service.ExploreTheater(filters)
  expected = [{"comName": "4400 Theater Company", "thCity": "San Francisco", "thName": "Cinema Star", "thState": "CA", "thStreet": "100 Cool Place", "thZipcode": "94016"}, {"comName": "4400 Theater Company", "thCity": "Seattle", "thName": "Jonathan's Movies", "thState": "WA", "thStreet": "67 Pearl Dr", "thZipcode": "98101"}, {"comName": "4400 Theater Company", "thCity": "Boulder", "thName": "Star Movies", "thState": "CA", "thStreet": "4400 Rocks Ave", "thZipcode": "80301"}, {"comName": "AI Theater Company", "thCity": "Pallet Town", "thName": "ML Movies", "thState": "KS", "thStreet": "314 Pi St", "thZipcode": "31415"}, {"comName": "Awesome Theater Company", "thCity": "Austin", "thName": "ABC Theater", "thState": "TX", "thStreet": "880 Color Dr", "thZipcode": "73301"}, {"comName": "EZ Theater Company", "thCity": "New York", "thName": "Main Movies", "thState": "NY", "thStreet": "123 Main St", "thZipcode": "10001"}, {"comName": "EZ Theater Company", "thCity": "Atlanta", "thName": "Star Movies", "thState": "GA", "thStreet": "745 GT St", "thZipcode": "30332"}]

  assert len(actual) == len(expected)
  assert sorted(actual, key=functools.cmp_to_key(compare_theater)) == sorted(expected, key=functools.cmp_to_key(compare_theater))

def test_user_visit_th():
  db_reset()
  user_service = UserService()
  username = 'thePiGuy3.14'


  filters = {
        'i_visitdate':'2019-12-24',
        'i_coname':'Awesome Theater Company',
        'i_thname':'ABC Theater'
      }

  user_service.LogVisit(username, filters)

  connection = get_conn()
  with connection.cursor() as cursor:
    cursor.execute("SELECT * FROM UserVisitTheater where username = '" + username+"'")
    data = cursor.fetchall()
    connection.commit()
  connection.close()
  assert len(data) == 1

def test_user_filter_visitHistory():
  db_reset()
  user_service = UserService()
  username = "ghcghc"
  filters = {
        'visitDate1':None,
        'visitDate2':None
        
      }
  actual = user_service.VisitHistory(username, filters)
  assert actual == ()

  visitDetails = {
    'i_visitdate':"2019-12-24",
    'i_coname':'Awesome Theater Company',
    'i_thname':'ABC Theater'
  }
  user_service.LogVisit(username, visitDetails)


  actual = user_service.VisitHistory(username, filters)
  expected = [{"comName": "Awesome Theater Company", "thCity": "Austin", "thName": "ABC Theater", "thState": "TX", "thStreet": "880 Color Dr", "thZipcode": "73301", "visitDate": "2019-12-24"}]
  assert len(actual) == len(expected)