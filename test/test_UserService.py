import pytest

import functools
import datetime

import pymysql
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


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

      filters = {}

      actual = user_service.ExploreTheater(filters)

      expected = [
        {'comName':"EZ Theater Company",'thName':"Main Movies",'thStreet':"123 Main St",'thCity':"New York",'thState':'NY','thZipcode':10001},
        {'comName':"EZ Theater Company",'thName':'Star Movies','thStreet':'745 GT St','thCity':'Atlanta','thState':'GA',thZipcode:30332},
        {'comName':'4400 Theater Company','thName':'Cinema Star','thStreet':'100 Cool Place','thCity':'San Francisco','thState':'CA',94016},
        {'comName':'4400 Theater Company','thName':'Star Movies','thStreet':'4400 Rocks Ave','thCity':'Boulder','thState':'CA',80301},
        {'comName':'4400 Theater Company','thName':"Jonathan's Movies",'thStreet':'67 Pearl Dr','thCity':'Seattle','thState':'WA',98101},
        {'comName':'Awesome Theater Company','thName':'ABC Theater','thStreet':'880 Color Dr','thCity':'Austin','thState':'TX',73301},
        {'comName':'AI Theater Company','thName':'ML Movies','thStreet':'314 Pi St','thCity':'Pallet Town','thState':'KS',31415};
      ]

      assert len(actual) == len(expected)

      assert actual == expected
        